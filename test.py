import streamlit as st
from datetime import datetime

# 별자리 판별 함수
def get_zodiac(month, day):
    zodiac_dates = [
        ((1, 20), (2, 18), "물병자리"),
        ((2, 19), (3, 20), "물고기자리"),
        ((3, 21), (4, 19), "양자리"),
        ((4, 20), (5, 20), "황소자리"),
        ((5, 21), (6, 21), "쌍둥이자리"),
        ((6, 22), (7, 22), "게자리"),
        ((7, 23), (8, 22), "사자자리"),
        ((8, 23), (9, 22), "처녀자리"),
        ((9, 23), (10, 22), "천칭자리"),
        ((10, 23), (11, 22), "전갈자리"),
        ((11, 23), (12, 21), "사수자리"),
        ((12, 22), (1, 19), "염소자리"),
    ]
    for start, end, zodiac in zodiac_dates:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return zodiac
    return "알 수 없음"

# 수비학 숫자 계산
def get_life_path_number(birthdate):
    digits = [int(d) for d in birthdate.strftime("%Y%m%d")]
    total = sum(digits)
    while total > 9:
        total = sum(int(d) for d in str(total))
    return total

# 별자리별 성향
zodiac_traits = {
    "양자리": "도전적이고 열정적이며 사랑에서 직진하는 스타일.",
    "황소자리": "안정적이고 느긋하며 깊은 신뢰를 바탕으로 한 사랑을 추구.",
    "쌍둥이자리": "재미와 지적 대화를 중시하며 다채로운 연애를 즐김.",
    "게자리": "가족적이고 헌신적이며 따뜻한 감정을 아낌없이 표현.",
    "사자자리": "자신감 있고 드라마틱한 사랑을 하며 주도적인 태도를 보임.",
    "처녀자리": "섬세하고 현실적인 연애관을 가지며 진정성 있는 관계를 원함.",
    "천칭자리": "균형과 조화를 중시하며 로맨틱하고 세련된 사랑을 지향.",
    "전갈자리": "강렬하고 열정적인 사랑을 하며 깊은 유대감을 원함.",
    "사수자리": "자유롭고 모험적인 연애를 즐기며 솔직함을 중시.",
    "염소자리": "책임감 있고 신중하며 안정된 관계를 최우선으로 생각.",
    "물병자리": "독창적이고 자유로운 연애관을 가지며 친구 같은 사랑을 추구.",
    "물고기자리": "감성적이고 헌신적이며 상대방을 따뜻하게 감싸줌."
}

# 수비학 성향
numerology_traits = {
    1: "주도적이고 리더십 있는 연애. 자신이 관계를 이끌어가려는 성향.",
    2: "배려심 깊고 감정 교류에 민감. 조화로운 사랑을 추구.",
    3: "즐겁고 활발한 연애. 대화와 웃음을 중요시.",
    4: "안정과 신뢰를 중시하는 성향. 오래가는 사랑을 선호.",
    5: "자유와 모험을 즐기는 연애. 변화를 원함.",
    6: "가정적이고 책임감 있는 사랑. 헌신적인 파트너.",
    7: "사색적이고 신비로운 연애. 깊은 정신적 유대 추구.",
    8: "현실적이고 목표 지향적인 사랑. 물질적 안정도 중요시.",
    9: "헌신적이고 이상주의적인 사랑. 희생을 아끼지 않음."
}

# 궁합 결과 생성
def compatibility(zodiac1, num1, zodiac2, num2):
    messages = []

    # 별자리 궁합 간단 매칭
    zodiac_compat = {
        "양자리": ["사자자리", "사수자리", "쌍둥이자리"],
        "황소자리": ["처녀자리", "염소자리", "게자리"],
        "쌍둥이자리": ["천칭자리", "물병자리", "양자리"],
        "게자리": ["전갈자리", "물고기자리", "황소자리"],
        "사자자리": ["양자리", "사수자리", "천칭자리"],
        "처녀자리": ["황소자리", "염소자리", "전갈자리"],
        "천칭자리": ["쌍둥이자리", "물병자리", "사자자리"],
        "전갈자리": ["게자리", "물고기자리", "처녀자리"],
        "사수자리": ["양자리", "사자자리", "물병자리"],
        "염소자리": ["황소자리", "처녀자리", "물고기자리"],
        "물병자리": ["쌍둥이자리", "천칭자리", "사수자리"],
        "물고기자리": ["게자리", "전갈자리", "염소자리"],
    }

    if zodiac2 in zodiac_compat.get(zodiac1, []):
        messages.append(f"별자리 궁합: {zodiac1}와 {zodiac2}는 서로 잘 맞는 별자리입니다! 자연스럽게 끌리고 조화를 이루는 관계예요.")
    else:
        messages.append(f"별자리 궁합: {zodiac1}와 {zodiac2}는 서로 다른 점이 많지만, 노력한다면 성장하는 관계가 될 수 있어요.")

    # 수비학 궁합
    if num1 == num2:
        messages.append("수비학 궁합: 두 사람의 인생 경로 숫자가 같아 비슷한 리듬과 가치관을 공유합니다.")
    elif abs(num1 - num2) == 1:
        messages.append("수비학 궁합: 두 사람은 서로를 보완하며 자극하는 관계입니다.")
    else:
        messages.append("수비학 궁합: 가치관 차이가 있을 수 있지만, 배려와 이해로 조화를 이룰 수 있어요.")

    # 잘 맞는 부분 상세
    good_points = {
        "대화 스타일": "서로가 솔직하게 대화할 수 있어 오해가 적고, 즐겁게 대화를 이어갈 수 있음.",
        "감정 표현": "감정을 진솔하게 나누어 깊은 유대감을 형성할 수 있음.",
        "가치관": "서로의 삶의 방향성이 비슷해 장기적인 관계에도 안정감을 줌.",
        "연애 속도": "연애의 속도가 잘 맞아 서로에게 부담 없이 자연스럽게 다가감."
    }

    messages.append("두 사람이 잘 맞는 부분:")
    for key, val in good_points.items():
        messages.append(f"- {key}: {val}")

    return "\n".join(messages)

# Streamlit 앱
st.title("✨ 별자리 + 수비학 연애 궁합 앱 ✨")

st.header("본인 정보 입력")
name1 = st.text_input("이름 (본인)")
gender1 = st.radio("성별 (본인)", ["남성", "여성"], key="g1")
birth1 = st.date_input("생년월일 (본인)", datetime(2000,1,1))

st.header("상대방 정보 입력")
name2 = st.text_input("이름 (상대방)")
gender2 = st.radio("성별 (상대방)", ["남성", "여성"], key="g2")
birth2 = st.date_input("생년월일 (상대방)", datetime(2000,1,1))

if st.button("궁합 보기"):
    zodiac1 = get_zodiac(birth1.month, birth1.day)
    zodiac2 = get_zodiac(birth2.month, birth2.day)
    num1 = get_life_path_number(birth1)
    num2 = get_life_path_number(birth2)

    st.subheader(f"🌟 {name1}님의 연애 성향")
    st.write(f"별자리({zodiac1}): {zodiac_traits[zodiac1]}")
    st.write(f"수비학 숫자({num1}): {numerology_traits[num1]}")

    st.subheader(f"🌟 {name2}님의 연애 성향")
    st.write(f"별자리({zodiac2}): {zodiac_traits[zodiac2]}")
    st.write(f"수비학 숫자({num2}): {numerology_traits[num2]}")

    st.subheader("💖 두 사람의 궁합")
    st.write(compatibility(zodiac1, num1, zodiac2, num2))
