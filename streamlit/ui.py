"""
### Cursor Agent로 생성한 코드 ###
streamlit 실행 명령어:
```bash
streamlit run streamlit/ui.py
```
"""

import streamlit as st
import requests

# 페이지 설정
st.set_page_config(
    page_title="TCR Epitope Prediction",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# FastAPI 서버 URL 설정
API_BASE_URL = st.sidebar.text_input(
    "FastAPI 서버 URL",
    value="http://localhost:8000",
    help="FastAPI 서버가 실행 중인 URL을 입력하세요",
)

# 제목 및 설명
st.title("🧬 TCR Epitope Prediction")
st.markdown("---")
st.markdown(
    """
    이 도구는 TCR (T-cell Receptor)의 CDR3 서열을 입력받아 예측된 epitope를 반환합니다.
    """
)

# 입력 섹션
st.subheader("📥 입력")

# CDR3 입력 필드
cdr3_input = st.text_input(
    "CDR3 서열", placeholder="예: CASSLGQYEQYF", help="TCR의 CDR3 서열을 입력하세요"
)

# 제출 버튼
submit_button = st.button("🔍 예측 실행", type="primary", use_container_width=True)

st.markdown("---")

# 결과 섹션
st.subheader("📤 결과")

if submit_button:
    if not cdr3_input or cdr3_input.strip() == "":
        st.error("⚠️ CDR3 서열을 입력해주세요.")
    else:
        with st.spinner("예측 중..."):
            try:
                # FastAPI 엔드포인트 호출
                response = requests.post(
                    f"{API_BASE_URL}/tcr",
                    json={"cdr3": cdr3_input.strip()},
                    timeout=30,
                )

                if response.status_code == 200:
                    result = response.json()

                    # 결과 표시
                    st.success("✅ 예측 완료!")

                    # 결과 카드
                    st.markdown("### 예측 결과")

                    col_result1, col_result2 = st.columns(2)

                    with col_result1:
                        st.metric("입력 CDR3", result.get("input_cdr3", "N/A"))

                    with col_result2:
                        st.metric("예측 Epitope", result.get("epitope", "N/A"))

                    # 상세 정보
                    with st.expander("📋 상세 정보 보기"):
                        st.json(result)

                else:
                    st.error(f"❌ 오류 발생: {response.status_code}")
                    st.text(f"응답: {response.text}")

            except requests.exceptions.ConnectionError:
                st.error(
                    f"❌ FastAPI 서버에 연결할 수 없습니다.\n\n"
                    f"서버가 실행 중인지 확인하고, URL이 올바른지 확인해주세요.\n"
                    f"현재 설정된 URL: `{API_BASE_URL}`"
                )
                st.info(
                    "💡 FastAPI 서버를 실행하려면:\n"
                    "```bash\n"
                    "uvicorn src.main:app --reload\n"
                    "```"
                )

            except requests.exceptions.Timeout:
                st.error("⏱️ 요청 시간이 초과되었습니다. 다시 시도해주세요.")

            except Exception as e:
                st.error(f"❌ 예상치 못한 오류가 발생했습니다: {str(e)}")

else:
    st.info("👈 위에서 CDR3 서열을 입력하고 '예측 실행' 버튼을 클릭하세요.")

# 사이드바에 추가 정보
st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ 사용 방법")
st.sidebar.markdown(
    """
    1. FastAPI 서버가 실행 중인지 확인하세요
    2. CDR3 서열을 입력하세요
    3. '예측 실행' 버튼을 클릭하세요
    4. 결과를 확인하세요
    """
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📝 참고")
st.sidebar.markdown(
    """
    - CDR3 서열은 T-cell Receptor의 
      Complementarity Determining Region 3를 의미합니다
    - Epitope는 항원과 결합하는 특정 부위를 의미합니다
    """
)
