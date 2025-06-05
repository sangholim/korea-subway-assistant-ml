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
- 케이스1
  - per_device_train_batch_size = 2
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
    - 오타 발생 - 영어 문장 반복됨
- 케이스2
  - 데이터 셋에 중국어, 일본어 워딩 제거
  - skt-kogpt2-base-v2-seoul-subway-prompt-model-train.py
    - per_device_train_batch_size = 4
  - skt-kogpt2-base-v2-seoul-subway-prompt-model.py
    - max_new_tokens 제거
    - top_k 제거
  - 학습후:
    🧠 Prompt: 사당역에 대해 알려줘
    🗨️  Response: 한국어는 사당입니다.
    영어는 Sadang입니다.
    영어는 Sadang입니다.
    영어는 S
  - 후기: max_new_tokens 사이즈에 맞게 응답을 만드는데, 
         학습 데이터가 max_new_tokens 보다 작으면, 반복되거나 반복중에 단어가 잘릴수 있음.
         학습 데이터가 max_new_tokens 보다 크면, 응답 문자열이 잘릴수 있음
  

