import json
from datasets import Dataset

# Load your orign JSON dataset, after save json dataset
with open("./datasets/korea_subway_station.json", "r", encoding="utf-8") as f:
    data = json.load(f)

dataset = Dataset.from_list(data['DATA'])

all_conversations = []

# Prompt templates
prompt_templates = [
    "{}에 대해 알려줘",
    "{}은 어디에 있어?",
    "{} 이름의 뜻은 뭐야?",
    "{}에 대해 설명해줘",
    "{}의 외국어 이름이 뭐야?",
    "{}을 영어로 뭐라고 해?",
    "{} 역에 대해 자세히 알려줘"
]

for station in dataset:
    for prompt_template in prompt_templates:
        prompt = prompt_template.format(station['station_nm'])
        response = (
            f"한국어는 {station['station_nm']}입니다.\n"
            f"영어는 {station['station_nm_eng']}입니다.\n"
        )
        all_conversations.append({"prompt":prompt, "response":response})

with open("./datasets/korea_subway_station_prompt_train.json", "w", encoding="utf-8") as f:
    json.dump(all_conversations, f, ensure_ascii=False, indent=2)