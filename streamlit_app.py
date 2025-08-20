import streamlit as st

st.title("🏫 우리 응원 카드")
st.write("응원을 보내드리겟습니다 !")
# streamlit_app.py

import streamlit as st
import random

# --- 1. 교사 응원 문구 리스트 (하얀선생님 화이팅 🩷) ---
# 교사들이 공감하고 힘을 얻을 만한 문구들로 구성합니다.
QUOTES = [
    "이주원바보",
    "박지우바보",
    "엄마아빠 화이팅",
    "수아 보구시퍼",
    "이대형선생님 화이탱",
    "전서연 바보임ㅋㅋㅋㅋㅋㅋ안 먹는다고 100번 말했는데 진짜 안 먹은 적 2번임",
    "수아 아푸지마라",
    "세호선생님 화이팅 💚",
    "이하얀선생님 화이팅 🩷",
    "박지우는 안 화이팅 ㅋ"
]

# --- 2. 앱 기본 설정 ---
# 웹 브라우저 탭에 표시될 제목과 아이콘을 설정합니다.
st.set_page_config(page_title="교사용 응원 카드", page_icon="💌")

# --- 3. 세션 상태(Session State) 초기화 ---
# Streamlit은 스크립트를 위에서 아래로 다시 실행하므로, 변수 값을 유지하려면 세션 상태를 사용해야 합니다.
# 'current_quote'와 'previous_quote'가 세션에 없으면 초기화합니다.
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = "버튼을 눌러 오늘의 응원을 확인하세요!"
if 'previous_quote' not in st.session_state:
    st.session_state.previous_quote = None


# --- 4. 앱 UI 구성 ---

# 앱의 메인 제목을 표시합니다.
st.title("💌 응원 카드")
st.write("---") # 구분선

# 메인 응원 문구를 표시할 영역
# st.info()를 사용해 시각적으로 강조합니다.
st.info(f"**{st.session_state.current_quote}**")

# 버튼들을 가로로 나란히 배치하기 위해 컬럼을 사용합니다.
col1, col2 = st.columns(2)

# 첫 번째 컬럼: '오늘의 응원 받기' 버튼
with col1:
    if st.button("✨ 오늘의 응원 받기", use_container_width=True, type="primary"):
        # 기존의 현재 문구를 '이전 문구'로 저장합니다.
        # 단, 초기 메시지("버튼을 눌러...")는 저장하지 않습니다.
        if st.session_state.current_quote != "버튼을 눌러 오늘의 응원을 확인하세요!":
            st.session_state.previous_quote = st.session_state.current_quote

        # QUOTES 리스트에서 새로운 문구를 무작위로 선택합니다.
        new_quote = random.choice(QUOTES)

        # 만약 새로 뽑은 문구가 현재 문구와 같다면, 다를 때까지 다시 뽑습니다.
        # 리스트에 문구가 1개만 있는 경우 무한 루프에 빠질 수 있으므로, 문구 개수가 1보다 클 때만 실행합니다.
        while new_quote == st.session_state.current_quote and len(QUOTES) > 1:
            new_quote = random.choice(QUOTES)

        # 선택된 새로운 문구를 현재 문구로 업데이트합니다.
        st.session_state.current_quote = new_quote
        # st.rerun()을 호출하여 화면을 즉시 새로고침하고 변경된 문구를 표시합니다.
        st.rerun()

# 두 번째 컬럼: '최근 응원 문구 다시 보기' 버튼
with col2:
    if st.button("history 최근 응원 다시 보기", use_container_width=True):
        # '이전 문구'가 저장되어 있는지 확인합니다.
        if st.session_state.previous_quote:
            # 이전 문구가 있다면 st.success()를 이용해 다른 색상으로 표시합니다.
            st.success(f"**최근 응원:** {st.session_state.previous_quote}")
        else:
            # 이전 문구가 없다면 안내 메시지를 표시합니다.
            st.warning("아직 이전 응원 기록이 없어요.")

