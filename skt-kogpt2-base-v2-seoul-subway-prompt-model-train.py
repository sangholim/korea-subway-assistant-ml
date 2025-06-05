import json
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments,
    DataCollatorForLanguageModeling,
)
import torch
import os
from dotenv import load_dotenv
from huggingface_hub import login

# Load .env file variables into environment
load_dotenv()

login(token=os.getenv("HF_TOKEN"))

dataset_file_path = "./datasets/korea_subway_station_prompt_train.json"

# model
if torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

print("Using device:", device)
model_name = "skt/kogpt2-base-v2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
# Fix: define a pad token
tokenizer.pad_token = tokenizer.eos_token  # Common practice for GPT2
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

# dataset 파일 객체로 로딩
with open(dataset_file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

dataset = Dataset.from_list(data)

# dataset 파일 읽고 토큰화
def tokenize(example):
    full_text = example["prompt"] + "\n" + example["response"]
    tokenized = tokenizer(
        full_text,
        truncation=True,
        max_length=512,
        padding="max_length",
    )
    tokenized["labels"] = tokenized["input_ids"].copy()
    return tokenized

tokenized_dataset = dataset.map(tokenize, batched=False)

# 5. Data collator (handles padding dynamically)
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False
)

# 6. Training arguments
training_args = TrainingArguments(
    output_dir="./skt-kogpt2-base-v2-korea-subway-station-train-output",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,  # small batch size due to Mac CPU limits
    save_steps=500,
    save_total_limit=2,
    logging_steps=100,
    logging_dir="./logs",
    report_to="none"
)

# 7. Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
)

# 8. Start training
trainer.train()

# 9. Save the fine-tuned model
trainer.save_model("./skt-kogpt2-base-v2-korea-subway-station-model")