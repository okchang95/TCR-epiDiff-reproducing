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


class TCR(BaseModel):
    cdr3: str


class TCRResponse(BaseModel):
    input_cdr3: str
    epitope: str


app = FastAPI()


@app.post("/tcr")
def get_tcr(tcr: TCR):
    """
    tcr 서열을 입력받아서 epitope generation을 수행하고, 결과를 반환
    """
    tcr_sequence = tcr.cdr3

    # TODO: inference logic 추가
    # generated_epitope = epitope_generation(tcr_sequence)
    generated_epitope = "not implemented"

    result = {"input_cdr3": tcr_sequence, "epitope": generated_epitope}

    return TCRResponse(**result)
