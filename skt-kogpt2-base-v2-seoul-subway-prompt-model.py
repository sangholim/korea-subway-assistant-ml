from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os
from dotenv import load_dotenv
from huggingface_hub import login
# Load .env file variables into environment
load_dotenv()

login(token=os.getenv("HF_TOKEN"))

# Path to your trained model or pre-trained checkpoint
model_path = "./skt-kogpt2-base-v2-korea-subway-station-model"  # Change to your path or model ID

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

# Important: set pad_token to eos_token (same as during training)
tokenizer.pad_token = tokenizer.eos_token

# Move model to MPS or CPU
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
model.to(device)

# 🔍 Inference function
def generate_response(prompt):
    input_text = prompt.strip()  # don't need BOS if not used in training

    # Tokenize and move to device
    input_ids = tokenizer.encode(input_text, return_tensors="pt").to(device)

    # Generate output
    with torch.no_grad():
        output_ids = model.generate(
            input_ids,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
            max_new_tokens=11,
            temperature=0.8,
            top_p=0.95,
            do_sample=True,
            early_stopping=True
        )

    # Decode and clean response
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    # Remove prompt from output if it gets copied
    return output_text.replace(prompt, "").strip()

# 🧪 Example usage
prompt = "사당역에 대해 알려줘"
response = generate_response(prompt)

print(f"🧠 Prompt: {prompt}")
print(f"🗨️  Response: {response}")