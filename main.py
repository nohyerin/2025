# mbti_love_full_app.py
import streamlit as st
from textwrap import fill
import datetime

st.set_page_config(page_title="MBTI 연애 성향 & 궁합 분석기", page_icon="💖", layout="centered")

# ========== MBTI별 상세 연애 성향 ==========
# 각 항목은 여러 문단으로 구성 (문장 길이와 개행을 고려)
mbti_love_traits = {
    "INTJ": (
        "INTJ는 연애에서 ‘미래 설계’와 ‘신뢰’가 핵심이에요.\n\n"
        "감정을 거칠게 드러내기보다는 체계적이고 논리적으로 관계를 운영하려고 합니다. "
        "장기적인 목표를 공유하고 함께 성장할 수 있는 파트너에 큰 가치를 둡니다. "
        "초반에는 차갑고 거리를 두는 것처럼 보일 수 있지만, 신뢰가 쌓이면 깊고 헌신적인 모습을 보여줍니다.\n\n"
        "갈등이 생기면 감정적 대응보다 해결책을 찾는 쪽을 선호하므로, 감정의 세심한 처리가 필요합니다. "
        "상대의 감정 표현을 기다리는 성향이 있어 때로는 파트너가 소외감을 느낄 수 있으니 의식적으로 애정 표현을 늘리는 것이 좋아요."
    ),
    "INTP": (
        "INTP는 호기심과 지적 교감이 중심인 연애를 선호합니다.\n\n"
        "감정의 표현이 즉각적이지 않을 수 있으나, 대화의 깊이와 자유로운 사고를 함께 나눌 수 있는 사람과 잘 맞습니다. "
        "관계에서의 규칙이나 전통에 얽매이기보다는 두 사람이 서로의 세계를 존중하며 독립성을 유지하는 걸 중요시해요.\n\n"
        "감정 표현이 서툴 수 있어 오해가 생기기도 하지만, 진지해지면 상대를 위해 문제를 분석하고 개선하려는 태도를 보입니다. "
        "따뜻한 피드백과 꾸준한 관심이 큰 힘이 됩니다."
    ),
    "ENTJ": (
        "ENTJ는 연애에서도 목표 지향적이고 주도적인 모습을 보입니다.\n\n"
        "관계에 명확한 비전이 있고, 파트너와 함께 성장하고 성취하는 것을 중요하게 여깁니다. "
        "결단력 있고 솔직해 갈등 처리도 빠른 편이지만, 때로는 지나치게 실용적으로 보일 수 있습니다.\n\n"
        "감정 표현은 행동으로 보여주는 경우가 많아 말로 애정을 표현하는 것을 어색해할 수 있습니다. "
        "상대는 ENTJ의 리더십을 신뢰하되, 감정적 지지와 인정(칭찬)을 자주 해주면 관계가 훨씬 안정됩니다."
    ),
    "ENTP": (
        "ENTP는 연애에서 유머, 변화, 아이디어를 공유하는 것을 즐깁니다.\n\n"
        "새로운 경험과 토론을 즐기며, 상대와 지적으로 자극을 주고받는 관계를 좋아해요. "
        "즉흥적이고 활기찬 면이 매력적이지만, 가끔 일관성 부족으로 상대가 불안해할 수 있습니다.\n\n"
        "관계에 있어서 자유와 신선함을 유지하려다 보니 장기적 약속과 루틴을 만들 때 노력이 필요합니다. "
        "상대가 안정감을 원한다면 소통으로 균형을 맞추는 것이 중요합니다."
    ),
    "INFJ": (
        "INFJ는 깊은 공감과 헌신을 바탕으로 한 연애를 지향합니다.\n\n"
        "상대의 내면을 읽어주고 서포트하는 능력이 뛰어나며, 진심으로 서로를 성장시키는 파트너가 되려 합니다. "
        "겉으로는 조용하지만 감정적 친밀감을 매우 중시해 한번 신뢰하면 큰 헌신을 보입니다.\n\n"
        "상대가 상처받지 않도록 세심히 배려하는 대신, 자신도 때론 감정 표출을 통해 도움을 요청할 수 있도록 연습하면 좋습니다."
    ),
    "INFP": (
        "INFP는 이상과 가치 중심의 로맨스를 원합니다.\n\n"
        "사랑을 깊이 느끼며, 의미 있는 연결과 감정적 진실성을 중시해요. 낭만적이고 창의적인 표현을 통해 사랑을 전합니다. "
        "다만 상처를 받으면 내향적으로 물러날 수 있어 상대가 이를 알아차리고 기다려주는 인내가 필요합니다.\n\n"
        "자유와 이해를 제공해주며, 함께 가치관을 공유할 수 있는 사람이 가장 잘 맞습니다. 작은 감정에도 민감하니 반복적인 확인과 안정감이 큰 도움이 됩니다."
    ),
    "ENFJ": (
        "ENFJ는 관계에서의 조화와 배려를 최우선으로 합니다.\n\n"
        "상대의 감정에 민감하고, 필요할 때 적극적으로 보살피는 타입이라 연애에서 든든한 파트너가 됩니다. "
        "사교적이어서 연인의 사회적 관계까지 신경 써주는 성향이 강합니다.\n\n"
        "다만 상대를 배려하는 과정에서 자신의 감정이나 욕구를 묵살할 수 있으니, 가끔은 솔직하게 '나'의 필요를 표현하는 연습이 필요합니다."
    ),
    "ENFP": (
        "ENFP는 열정과 즉흥성, 감성적 풍부함으로 연애를 즐깁니다.\n\n"
        "사소한 것에서 설렘을 찾고, 함께하는 경험을 통해 관계를 깊게 만듭니다. 자유와 다양성을 존중하며 상대에게 영감을 주는 편이에요. "
        "반면 감정의 기복이 있을 수 있어 일관성 문제는 신경 써줘야 합니다.\n\n"
        "일상에 활력을 주는 파트너가 되지만, 안정감을 원하는 상대에게는 꾸준한 배려와 약속 이행이 중요합니다."
    ),
    "ISTJ": (
        "ISTJ는 안정감, 책임감, 신뢰를 바탕으로 한 연애를 추구합니다.\n\n"
        "약속을 잘 지키고 성실하게 관계를 관리하려는 태도가 강합니다. 실용적이고 현실적인 형태의 사랑을 보여주며, 큰 로맨틱한 이벤트보다 일상의 신뢰가 더 중요합니다. "
        "표현은 절제된 편이지만 행동으로 애정을 증명합니다.\n\n"
        "상대가 신뢰할 수 있고 예측 가능한 태도를 보이면 깊은 안정감을 느낍니다. 감정의 표현을 조금 더 해주면 관계가 부드럽게 흐릅니다."
    ),
    "ISFJ": (
        "ISFJ는 헌신적이고 세심한 돌봄으로 연애를 이끕니다.\n\n"
        "상대의 필요를 미리 챙기고 작은 것까지 기억하는 섬세함이 장점입니다. 갈등을 피해 조용히 맞춰주려는 경향이 있어, 때로는 자기 감정을 숨기기도 합니다. "
        "안정감과 일상적인 친절을 중요하게 생각합니다.\n\n"
        "상대가 고마움을 자주 표현해주면 ISFJ는 더 따뜻하게 반응합니다. 자신의 요구도 가끔은 직접 말하는 것이 건강한 관계에 도움이 됩니다."
    ),
    "ESTJ": (
        "ESTJ는 명확한 구조와 실천력을 가진 연애 스타일입니다.\n\n"
        "관계에서의 역할과 책임을 분명히 하며 효율적으로 문제를 해결하려는 태도가 강합니다. 상대에게 신뢰받고 존경받는 것을 중요시해요. "
        "감정보다 사실과 결과를 우선하는 듯 보일 수 있지만, 안정적인 보호자 역할을 잘 해냅니다.\n\n"
        "상대가 감성적 지지를 원할 때는 의도적으로 다정함을 보여주는 연습이 필요할 수 있습니다."
    ),
    "ESFJ": (
        "ESFJ는 따뜻하고 사교적인 돌봄형 연인이에요.\n\n"
        "상대의 행복을 자신의 기쁨으로 삼고, 관계 유지에 필요한 실질적인 배려를 자주 보여줍니다. 풍부한 사회적 네트워크로 인해 연애에서도 활발한 활동을 이끕니다. "
        "때로는 타인의 기대에 맞추느라 자신의 감정을 억누를 수 있어요.\n\n"
        "상대가 진심으로 감사를 표현하면 ESFJ는 더 크게 헌신합니다. 서로의 감정과 한계를 존중하는 대화를 꾸준히 하는 것이 중요합니다."
    ),
    "ISTP": (
        "ISTP는 자유롭고 실용적인 연애를 선호합니다.\n\n"
        "감정 표현은 절제된 편이지만, 행동으로는 신뢰할 수 있는 파트너가 됩니다. 즉흥적인 데이트나 활동적인 취미를 공유하면 돈독해지는 타입입니다. "
        "관계에서 과도한 감정적 요구나 집착을 부담스러워할 수 있으니, 적당한 거리 유지가 필요합니다.\n\n"
        "상대의 자율성을 존중하고 자신도 그러한 자율성을 기대합니다. 안정과 모험의 균형을 맞추면 좋은 관계가 됩니다."
    ),
    "ISFP": (
        "ISFP는 부드럽고 감성적인 분위기로 사랑을 표현합니다.\n\n"
        "작은 제스처와 섬세한 배려를 통해 애정을 전하며, 예술적이고 감각적인 경험을 함께 나누는 것을 좋아합니다. "
        "자기 표현은 낭만적이면서도 내향적일 수 있어, 상대가 이 부분을 이해해주는 것이 중요합니다.\n\n"
        "감정이 예민하므로 비난보다는 부드러운 소통이 효과적입니다. 서로의 공간을 존중하면서 친밀감을 키우는 스타일이에요."
    ),
    "ESTP": (
        "ESTP는 활발하고 현실적인 방식으로 연애를 즐깁니다.\n\n"
        "액션과 경험을 통해 친밀감을 쌓으며, 즉흥적이고 모험적인 데이트를 선호합니다. 재치와 유머로 관계를 활기차게 만드는 능력이 있죠. "
        "감정적으로는 직접적이고 솔직하지만, 깊은 약속을 요구할 때는 주저할 수 있습니다.\n\n"
        "상대가 함께 활동을 즐기고 유연함을 보이면 호흡이 잘 맞습니다. 장기적 안정감이 필요하다면 꾸준한 신뢰 쌓기가 필요합니다."
    ),
    "ESFP": (
        "ESFP는 즐거움과 감각적 경험을 통해 사랑을 표현합니다.\n\n"
        "밝고 사교적이며 분위기를 잘 살리는 타입으로, 상대와 함께 있는 순간을 최대한 즐기려 합니다. "
        "감정 표현이 풍부하고 즉각적이라 상대에게 따뜻함을 느끼게 합니다. 하지만 때로는 계획성 부족으로 실용적 문제에서 충돌이 생길 수 있어요.\n\n"
        "상대가 함께 웃고 즐길 수 있는 순간을 자주 만들어주면 ESFP는 관계에 크게 헌신합니다."
    ),
}

# ========== MBTI 궁합 데이터 ==========
# 각 MBTI에 대해 '추천 상대 목록' (순서: 가장 잘 맞는 순). 각 항목은 (타입, 핵심이유)
mbti_compatibility = {
    "INTJ": [
        ("ENTP", "아이디어 충돌과 교감 → 지적 자극을 주고받음"),
        ("INFJ", "가치관과 진지한 헌신의 방식이 잘 맞음"),
        ("INTP", "서로의 독립성을 존중하며 깊은 대화를 나눔"),
    ],
    "INTP": [
        ("ENTJ", "논리적 보완 → 계획 실행을 도와줌"),
        ("ENFP", "호기심과 자유를 함께 즐김"),
        ("INTJ", "공유된 지적 관심사와 독립성"),
    ],
    "ENTJ": [
        ("INTP", "아이디어와 실행의 훌륭한 조합"),
        ("ENFJ", "지적 리더십과 정서적 관리의 균형"),
        ("ENTP", "도전과 흥미를 주는 관계"),
    ],
    "ENTP": [
        ("INFJ", "상대의 안정감과 ENTP의 활력이 균형을 이룸"),
        ("INTJ", "서로 생각을 자극하는 파트너"),
        ("ENFP", "공통된 모험심과 즉흥성"),
    ],
    "INFJ": [
        ("ENFP", "감정적 깊이와 활력의 보완"),
        ("INTJ", "가치관 및 장기 비전의 공감"),
        ("INFP", "감성적 공감과 이상 추구의 공유"),
    ],
    "INFP": [
        ("ENFJ", "외향적 지지와 내면적 이상주의의 균형"),
        ("INFJ", "깊은 감정적 연결과 가치공유"),
        ("INTP", "지적 자유와 감성적 이해"),
    ],
    "ENFJ": [
        ("INFP", "감성적 풍부함과 헌신의 조화"),
        ("ENTJ", "리더십과 관계 운영의 균형"),
        ("ENFP", "열정과 사회적 에너지의 공감"),
    ],
    "ENFP": [
        ("INFJ", "감성적 깊이와 영감의 상호 보완"),
        ("INTP", "자유로우면서도 지적인 자극"),
        ("ENFJ", "사교적 지원과 열정의 결합"),
    ],
    "ISTJ": [
        ("ESFJ", "실용적 배려와 안정감으로 잘 맞음"),
        ("ISFJ", "상호 책임감과 헌신"),
        ("ESTJ", "구조와 예측 가능성 공유"),
    ],
    "ISFJ": [
        ("ISTJ", "안정감과 신뢰의 상호 보완"),
        ("ESFJ", "따뜻함과 돌봄의 공동체"),
        ("INFP", "서로의 섬세함을 이해하는 조합"),
    ],
    "ESTJ": [
        ("ISFJ", "효율성과 헌신의 조화"),
        ("ISTJ", "비슷한 가치와 책임감"),
        ("ESFJ", "사회적 안정감과 실용성"),
    ],
    "ESFJ": [
        ("ISFJ", "서로를 챙기는 배려의 관계"),
        ("ISTJ", "안정감과 실천력의 결합"),
        ("ENFJ", "사회적 영향력과 따뜻함의 결합"),
    ],
    "ISTP": [
        ("ESFP", "모험과 감각적 즐거움의 조화"),
        ("ISFP", "조용한 감성 공유"),
        ("ESTP", "활동적이고 현실적인 파트너"),
    ],
    "ISFP": [
        ("ISTP", "서로의 자유와 감성을 존중"),
        ("ESFP", "상대의 에너지로 감정이 살아남"),
        ("INFP", "감성적 공감 및 이상적 공유"),
    ],
    "ESTP": [
        ("ISFP", "활동적 경험과 감성적 안정 보완"),
        ("ISTP", "실용적 재미와 즉흥성"),
        ("ESFP", "모험적 유사성"),
    ],
    "ESFP": [
        ("ISTP", "실제적 활동과 즐거움의 조화"),
        ("ISFP", "감성적 연결과 즐거움"),
        ("ESTP", "즉흥적 즐거움을 함께 함"),
    ],
}

# 기본 MBTI 목록 정렬
MBTI_LIST = list(mbti_love_traits.keys())
MBTI_LIST.sort()

# ========== 헬퍼 함수 ==========
def summarize_text(text: str, width: int = 80) -> str:
    """긴 텍스트를 width 기준으로 줄바꿈 처리해 깔끔하게 보여주기"""
    paragraphs = text.split("\n\n")
    wrapped = "\n\n".join(fill(p, width=width) for p in paragraphs)
    return wrapped

def compatibility_score(primary: str, other: str) -> int:
    """
    간단한 궁합 점수 매기기 (정성적)
    - 매칭 리스트에 있으면 높은 점수, 아니면 중간/낮음
    이 함수는 UI용 점수 시뮬레이션입니다.
    """
    top_list = [t for t, _ in mbti_compatibility.get(primary, [])]
    if other == primary:
        return 70  # 같은 유형: 이해는 쉽지만 단점도 공유
    if other in top_list:
        # score based on position
        idx = top_list.index(other)
        return 90 - idx * 8  # 90, 82, 74 ...
    # 기본: 55 ~ 70
    return 60

def generate_pair_analysis(me: str, partner: str) -> str:
    """나와 상대 MBTI에 따른 쌍방 설명과 행동 팁을 반환"""
    my_trait = mbti_love_traits.get(me, "")
    partner_trait = mbti_love_traits.get(partner, "")
    score = compatibility_score(me, partner)
    # 간단한 상호작용 조언 (정성적)
    advice_lines = []
    # If partner is listed in my top compatibilities
    top_for_me = [t for t, _ in mbti_compatibility.get(me, [])]
    top_for_partner = [t for t, _ in mbti_compatibility.get(partner, [])]
    if partner in top_for_me and me in top_for_partner:
        relation = "상호보완적 관계 — 서로의 강점을 잘 채워줄 수 있어요."
    elif partner in top_for_me:
        relation = "내게는 잘 맞는 타입 — 당신의 스타일이 파트너에게는 도전이 될 수 있어요."
    elif me in top_for_partner:
        relation = "파트너에게는 잘 맞는 타입 — 상대의 기대를 이해하려는 노력이 필요해요."
    else:
        relation = "서로 다른 점이 분명하지만, 노력과 이해로 안정적인 관계를 만들 수 있어요."
    advice_lines.append(relation)

    # 구체적 팁 (예시 패턴)
    tips = []
    tips.append(f"- {me} 입장에서: {mbti_love_traits.get(me).split('.')[0]}...")
    tips.append(f"- {partner} 입장에서: {mbti_love_traits.get(partner).split('.')[0]}...")
    # 맞춤형 행동 팁 (간단 규칙)
    if score >= 85:
        tips.append("서로의 차이를 장점으로 활용하세요. 정기적인 깊은 대화가 관계를 더 단단하게 합니다.")
    elif score >= 70:
        tips.append("의사소통 규칙(예: 감정 체크인, 기대치 명확화)을 만들어 갈등을 줄이세요.")
    else:
        tips.append("서로 다른 요구와 표현 방식을 인정하고, 작은 약속부터 신뢰를 쌓아가세요.")

    # 조합해서 반환
    analysis = (
        f"=== 요약 점수: {score}/100 ===\n\n"
        f"{relation}\n\n"
        f"---\n\n"
        f"당신({me})의 연애 성향 요약:\n{summarize_text(my_trait, width=80)}\n\n"
        f"상대({partner})의 연애 성향 요약:\n{summarize_text(partner_trait, width=80)}\n\n"
        "추천 팁:\n" + "\n".join(tips)
    )
    return analysis

# ========== Streamlit UI ==========
st.title("💖 MBTI 연애 성향 & 궁합 분석기")
st.write("당신의 MBTI를 선택하면 자세한 연애 성향을 보여주고, 상대 MBTI와의 궁합을 분석해줘요.")
st.write("---")

# 레이아웃: 왼쪽에 내 MBTI 선택, 오른쪽에 상대 MBTI 선택
col1, col2 = st.columns([1, 1])
with col1:
    my_mbti = st.selectbox("내 MBTI 선택", MBTI_LIST, index=MBTI_LIST.index("INFP") if "INFP" in MBTI_LIST else 0)
with col2:
    partner_mbti = st.selectbox("상대 MBTI 선택 (궁합 확인용)", ["— 선택 안함 —"] + MBTI_LIST, index=0)

st.markdown("---")

# 상세 연애성향 표시
st.subheader(f"🔎 {my_mbti}의 자세한 연애 성향")
st.markdown(summarize_text(mbti_love_traits[my_mbti], width=80).replace("\n", "  \n"))

# 확장 섹션: 성향 세부 (장점 / 주의점 / 데이트 팁)
with st.expander("더 보기 — 장점 · 주의점 · 데이트 팁"):
    st.write("**장점**")
    # 장점/주의점/데이트팁을 자동 추출하는 간단한 heuristic (여기선 요약 문장 사용)
    trait_text = mbti_love_traits[my_mbti]
    # 간단한 bullet 생성 (문장 첫 문장 등)
    sentences = [s.strip() for s in trait_text.split(". ") if s]
    for i, s in enumerate(sentences[:5]):
        st.write(f"- {s.strip()}.")
    st.write("**주의할 점**")
    st.write("- 감정 표현의 방식이 상대와 충돌할 수 있음. 서로의 스타일을 존중하세요.")
    st.write("**데이트 아이디어**")
    default_date_ideas = {
        "INTJ": "조용한 카페에서 장기 계획 이야기하기 / 전시회 방문",
        "ENFP": "즉흥 드라이브 / 작고 색다른 체험 클래스",
        "ISFP": "작은 미술관·소풍 / 손수 만든 선물 주기",
    }
    st.write(f"- 예시: {default_date_ideas.get(my_mbti, '함께 하는 활동으로 친밀감 쌓기(취미 공유, 짧은 여행 등)')}")

st.markdown("---")

# 궁합 분석 (상대 MBTI 선택 시)
if partner_mbti != "— 선택 안함 —":
    st.subheader("💑 쌍방 궁합 분석")
    pair_analysis = generate_pair_analysis(my_mbti, partner_mbti)
    # 보기 좋게 코드 블록 스타일로 보여주기
    st.code(pair_analysis, line_numbers=False)
    st.markdown("---")
    # 상호 추천 사유
    st.subheader("🔍 궁합 세부: 추천/주의 사유")
    # show compatibility list for my_mbti
    my_top = mbti_compatibility.get(my_mbti, [])
    st.write(f"**{my_mbti}에게 특히 잘 맞는 타입들(상위 3)**")
    for t, reason in my_top:
        st.write(f"- **{t}** — {reason}")
    # show reciprocal
    partner_top = mbti_compatibility.get(partner_mbti, [])
    st.write(f"\n**{partner_mbti}에게 특히 잘 맞는 타입들(상위 3)**")
    for t, reason in partner_top:
        st.write(f"- **{t}** — {reason}")

    # 다운로드: 결과 요약 텍스트
    summary_text = (
        f"MBTI 연애 성향 & 궁합 분석\n"
        f"날짜: {datetime.date.today().isoformat()}\n\n"
        f"나: {my_mbti}\n"
        f"상대: {partner_mbti}\n\n"
        f"{pair_analysis}\n\n"
        "※ 이 분석은 일반적 성향과 심리적 경향을 기반으로 한 안내입니다. 실제 관계에서는 개별적 차이가 큽니다."
    )
    st.download_button("결과 요약 다운로드 (.txt)", data=summary_text, file_name=f"mbti_couple_{my_mbti}_{partner_mbti}.txt")
else:
    # 전체 궁합 추천 (내 MBTI 기준 top 5)
    st.subheader("💡 전체 궁합 추천 (당신 기준)")
    with st.expander("내 MBTI와 잘 맞는 추천 타입 보기"):
        top_list = mbti_compatibility.get(my_mbti, [])
        if top_list:
            st.write("**추천 톱(간단 이유)**")
            for idx, (t, reason) in enumerate(top_list, start=1):
                st.write(f"{idx}. **{t}** — {reason}")
        else:
            st.write("추천 데이터가 없습니다.")

    # 버튼: 전체 MBTI와의 모의 점수 계산
    if st.button("전체 MBTI와 모의 궁합 점수 보기"):
        st.write("내 MBTI와 다른 유형들의 간단 점수(정성적 시뮬레이션)")
        scores = []
        for t in MBTI_LIST:
            sc = compatibility_score(my_mbti, t)
            scores.append((t, sc))
        # 정렬: 점수 내림차순
        scores.sort(key=lambda x: x[1], reverse=True)
        # 표로 출력 (상위 10개)
        st.write("상위 10 결과 (최고부터)")
        for t, sc in scores[:10]:
            # 설명 한 줄: 이유가 목록에 있으면 받아오기
            reasons = {k: v for k, v in mbti_compatibility.get(my_mbti, [])}
            reason_text = reasons.get(t, "서로 다른 점을 이해하고 맞춰가면 좋은 관계가 될 수 있어요.")
            st.write(f"- **{t}**: 점수 {sc}/100 — {reason_text}")

st.markdown("---")
st.caption("※ 이 앱은 MBTI의 일반적 특성을 참고해 만든 가이드입니다. 개인차가 크니 참고용으로 활용하세요. Made with ❤️")

