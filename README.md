# korea-subway-assistant-ml
한국 지하철 도우미 머신러닝 프로젝트

# 필요
- 허깅 페이스 계정

# dataset 변환
- seoul_subway_prompt_dataset.py

# 지하철 도우미1
- prompt 를 입력하면, 올바른 학습된 데이터를 출력한다.
- model: skt/kogpt2-base-v2
- model 훈련: skt-kogpt2-base-v2-seoul-subway-prompt-model-train.py
- model 테스트: skt-kogpt2-base-v2-seoul-subway-prompt-model.py
- 기대
  - prompt: 서울역역에 대해 알려줘. 
  - Response: 한국어는 서울역입니다.
    영어는 Seoul Station입니다.
    중국어는 首尔입니다.
    일본어는 ソウル입니다.
- 학습후: 
  - prompt: 서울역역에 대해 알려줘. 
  - Response: 한국어는 서울역입니다.
    영어는 Seoul Station입니다.
    중국어는 首尔站입니다.
    일본어는 ソ입니다.
    일본어는 ソ입니다.
    일본어는 ソク입니다.
    일본어는 ソヨク입니다.
- 오타 발생 - 중국어, 일본어 (중국어, 일본어를 학습시키거나, 데이터셋에서 예외해야할듯)
