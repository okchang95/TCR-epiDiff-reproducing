"""
uvicorn 실행 명령어:
```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

streamlit 실행 명령어:
```bash
streamlit run streamlit/ui.py
```
"""

from fastapi import FastAPI
from pydantic import BaseModel


class EPI(BaseModel):
    epitope: str


class TCRResponse(BaseModel):
    input_epitope: str
    tcr: str


app = FastAPI()


@app.post("/tcr")
def get_tcr(epitope: EPI) -> TCRResponse:
    """
    epitope sequence를 입력받아서 tcr sequence를 generation
    """
    epitope_sequence = epitope.epitope

    # TODO: inference logic 추가
    # generated_tcr = tcr_generation(epitope_sequence)
    generated_tcr = "not implemented"

    result = {"input_epitope": epitope_sequence, "tcr": generated_tcr}

    return TCRResponse(**result)
