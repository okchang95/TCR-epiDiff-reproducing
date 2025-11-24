# TCR-epiDiff reproducing

### 목표
- 학습 및 개선점 파악을 위한 TCR-epiDiff 논문 재현
- 모델의 재현성을 위해 서버 또는 툴로서 제공하는 방법을 고민


### 디렉토리 구성
```sh
.
├── app/ # fastapi app (모델 inference 서버)
├── data/ # training dataset
├── docs/ # 개발 기록, 문서
├── images/ # 컨텐츠이미지
├── notebook/ # 실험 노트북
├── requirements/ # 의존성 관리
├── src/ # preprocessing, train, eval, model 등의 코드
├── streamlit/ # streamlit ui (front-side)
└── README.md
```