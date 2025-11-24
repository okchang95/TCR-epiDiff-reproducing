1. hpc에 jupyter 서버 실행할 세팅
```bash
# HPC 가상환경에서 반드시 해야 하는 것 (커널 등록용)
# ✔ 1. 가상환경 생성

# 예: conda 또는 venv

conda create -n myenv python=3.10
conda activate myenv

# ✔ 2. ipykernel, jupyterlab 설치

pip install ipykernel # (이게 커널 역할을 하는 python 인터프리터)
pip install jupyterlab # 웹 기반의 대화형 개발 환경. notebook 후속버전

# ✔ 3. Jupyter에 커널 등록
# 원격 HPC에서 커널을 Jupyter에 알려주는 과정.

python -m ipykernel install --user --name myenv --display-name "Python (myenv)"

# 이제 VSCode Remote-SSH / Jupyter Notebook / JupyterLab에서
# “Python (myenv)”라는 커널을 선택할 수 있게 됨.
```

2. hpc에서 jupyter 서버 실행
```bash
jupyter lab --no-browser --port=8888
```

3. 로컬에서 포트포워딩
```bash
ssh -p 2222 -L 8888:localhost:8888 <username>@<server-ip>
```

4. 로컬 브라우저에서 접속 
```bash
jupyter에서 http://localhost:8888 입력, 비밀번호 입력해서 연결
```