import json
from datasets import Dataset

# Load your orign JSON dataset, after save json dataset
with open("./datasets/korea_subway_station.json", "r", encoding="utf-8") as f:
    data = json.load(f)

dataset = Dataset.from_list(data['DATA'])

all_conversations = []

for station in dataset:
    message = {
        "prompt": f"{station['station_nm']}역에 대해 알려줘",
        "response":(
            f"한국어는 {station['station_nm']}입니다.\n"
            f"영어는 {station['station_nm_eng']}입니다.\n"
        )
    }
    all_conversations.append(message)

with open("./datasets/korea_subway_station_prompt_train.json", "w", encoding="utf-8") as f:
    json.dump(all_conversations, f, ensure_ascii=False, indent=2)