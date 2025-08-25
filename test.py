import streamlit as st
from datetime import datetime

# 진단 문항 리스트
questions = [
    {
        "question": "햇빛에 노출되면 피부가 어떻게 되나요?",
        "options": ["빨갛게 타거나 화상을 입어요", "갈색으로 그을려요"]
    },
    {
        "question": "어떤 액세서리가 더 잘 어울리나요?",
        "options": ["은색", "금색"]
    },
    {
        "question": "밝은 색 옷이 잘 어울리나요, 어두운 색 옷이 잘 어울리나요?",
        "options": ["밝은 색", "어두운 색"]
    },
    {
        "question": "눈동자 색은 어떤가요?",
        "options": ["밝은 갈색 또는 회색, 녹색", "짙은 갈색 또는 검정"]
    },
    {
        "question": "혈관 색이 어떤가요? (팔목 기준)",
        "options": ["푸른빛에 가깝다", "초록빛에 가깝다"]
    },
    {
        "question": "화이트 셔츠를 입었을 때 느낌은?",
        "options": ["깔끔하고 얼굴이 밝아보인다", "창백하거나 떠보이는 느낌"]
    },
    {
        "question": "피부 베이스는 어떤 색이 잘 어울리나요?",
        "options": ["핑크 베이스", "옐로우 베이스"]
    },
    {
        "question": "볼터치 색상 중 어떤 게 더 자연스러워요?",
        "options": ["장밋빛, 핑크 계열", "오렌지, 코랄 계열"]
    },
    {
        "question": "피부톤이 어떤가요?",
        "options": ["밝고 투명한 느낌", "노란기나 어두운 톤"]
    },
    {
        "question": "입술에 어떤 색이 자연스럽게 어울리나요?",
        "options": ["로즈핑크, 푸시아", "살구, 브릭, 코랄"]
    }
]

# 진단 함수
def diagnose_personal_color(answers):
    """
    웜톤 선택지: 1점 (두 번째 보기)
    쿨톤 선택지: 0점 (첫 번째 보기)
    """
    score = sum(answers)
    if score >= 8:
        tone = "🍂 가을 웜톤"
        description = "딥하고 안정적인 컬러가 잘 어울려요. 브라운, 올리브그린, 버건디, 카멜 등의 색상 추천!"
    elif 5 <= score <= 7:
        tone = "🌸 봄 웜톤"
        description = "화사하고 따뜻한 색상이 잘 어울립니다. 코랄, 살구, 아이보리, 연한 골드 계열 추천!"
    elif 3 <= score <= 4:
        tone = "🌷 여름 쿨톤"
        description = "부드럽고 은은한 색상이 잘 어울립니다. 로즈핑크, 소프트블루, 연보라 계열 추천!"
    else:
        tone = "❄️ 겨울 쿨톤"
        description = "선명하고 강렬한 컬러가 잘 어울립니다. 푸시아, 네이비, 와인, 블랙 등 추천!"
    
    return tone, description

# Streamlit 앱 설정
st.set_page_config(page_title="퍼스널컬러 진단", page_icon="🎨")

# 앱 제목
st.title("🎨 나의 퍼스널컬러는?")

st.markdown("10개의 질문을 통해 퍼스널컬러를 진단해보세요!")

# 사용자 응답 저장 리스트
answers = []

# 질문 루프
for idx, q in enumerate(questions):
    st.markdown(f"**Q{idx+1}. {q['question']}**")
    choice = st.radio("", q["options"], key=f"q{idx}")
    answers.append(q["options"].index(choice))  # 첫 번째 보기 = 0점, 두 번째 보기 = 1점

# 제출 버튼
if st.button("🎯 진단하기"):
    tone, description = diagnose_personal_color(answers)
    st.success(f"**당신의 퍼스널컬러는: {tone}**")
    st.markdown(description)
    st.balloons()

