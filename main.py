import streamlit as st
st.title('경아의 첫 웹앱!')
st.write('만나서 반가워요!!🤖')
import streamlit as st
import random

# MBTI별 추천 포켓몬 데이터
mbti_pokemon = {
    "INTJ": {
        "pokemons": [
            {"name": "메타그로스", "desc": "치밀한 전략과 강력한 힘을 겸비한 강철/에스퍼 타입. 완벽주의적인 INTJ와 잘 어울려요."},
            {"name": "이상해꽃", "desc": "차분하고 안정적인 전략가형. 조용히 강력한 힘을 숨기고 있어요."},
        ],
        "desc": "논리적이고 전략적인 사고를 하는 INTJ에게는 강력한 지능형 포켓몬이 어울려요."
    },
    "INTP": {
        "pokemons": [
            {"name": "슈바르고", "desc": "복잡한 구조와 독특한 사고방식을 가진 강철/에스퍼 타입. 호기심 많은 INTP와 닮았어요."},
            {"name": "무장조", "desc": "분석적이고 독립적인 성향의 강철 포켓몬."},
        ],
        "desc": "탐구심이 강하고 독창적인 INTP에게는 독특하고 분석적인 포켓몬이 어울려요."
    },
    "ENTJ": {
        "pokemons": [
            {"name": "misdreavus 대신 리자몽", "desc": "카리스마 넘치고 강력한 리더형 포켓몬. 목표 지향적인 ENTJ와 완벽히 어울려요."},
            {"name": "갸라도스", "desc": "압도적인 카리스마와 힘을 가진 리더형 포켓몬."},
        ],
        "desc": "타고난 리더십과 추진력을 가진 ENTJ에게는 강력한 카리스마형 포켓몬이 어울려요."
    },
    "ENTP": {
        "pokemons": [
            {"name": "조로아크", "desc": "재치있고 변화무쌍한 성격의 악 타입. 새로운 아이디어를 좋아하는 ENTP와 닮았어요."},
            {"name": "치렌", "desc": "영리하고 임기응변에 강한 포켓몬."},
        ],
        "desc": "창의적이고 논쟁을 즐기는 ENTP에게는 재치있고 변화무쌍한 포켓몬이 어울려요."
    },
    "INFJ": {
        "pokemons": [
            {"name": "뮤츠", "desc": "깊은 통찰력과 신비로운 힘을 가진 에스퍼 타입. 이상주의적인 INFJ와 잘 맞아요."},
            {"name": "라티오스", "desc": "온화하지만 깊은 유대감을 중시하는 드래곤/에스퍼 포켓몬."},
        ],
        "desc": "깊은 통찰력과 이상을 가진 INFJ에게는 신비롭고 지혜로운 포켓몬이 어울려요."
    },
    "INFP": {
        "pokemons": [
            {"name": "뮤", "desc": "순수하고 신비로운 에너지를 가진 포켓몬. 감성적인 INFP와 닮았어요."},
            {"name": "세레비", "desc": "따뜻하고 시간을 초월한 유대감을 상징하는 포켓몬."},
        ],
        "desc": "따뜻한 감성과 이상을 품은 INFP에게는 순수하고 신비로운 포켓몬이 어울려요."
    },
    "ENFJ": {
        "pokemons": [
            {"name": "루카리오", "desc": "타인의 감정을 잘 읽고 이끄는 강철/격투 타입. 사람들을 이끄는 ENFJ와 잘 맞아요."},
            {"name": "라이코", "desc": "카리스마와 따뜻한 리더십을 가진 전설의 포켓몬."},
        ],
        "desc": "타인을 이끌고 돌보는 ENFJ에게는 카리스마 있고 배려심 깊은 포켓몬이 어울려요."
    },
    "ENFP": {
        "pokemons": [
            {"name": "메가니움", "desc": "밝고 따뜻한 에너지를 가진 풀 타입. 사교적이고 열정적인 ENFP와 닮았어요."},
            {"name": "피카츄", "desc": "활발하고 사랑받는 에너지 넘치는 포켓몬."},
        ],
        "desc": "열정적이고 사교적인 ENFP에게는 밝고 에너지 넘치는 포켓몬이 어울려요."
    },
    "ISTJ": {
        "pokemons": [
            {"name": "강철톤", "desc": "단단하고 신뢰할 수 있는 강철 타입. 원칙을 중시하는 ISTJ와 잘 맞아요."},
            {"name": "한카리아스", "desc": "묵묵히 자기 역할을 해내는 강철/드래곤 타입."},
        ],
        "desc": "성실하고 원칙적인 ISTJ에게는 단단하고 신뢰할 수 있는 포켓몬이 어울려요."
    },
    "ISFJ": {
        "pokemons": [
            {"name": "라플레시아 대신 잠만보", "desc": "느긋하지만 든든하게 지켜주는 노말 타입. 배려심 많은 ISFJ와 닮았어요."},
            {"name": "치리치노", "desc": "따뜻하고 헌신적인 성격의 포켓몬."},
        ],
        "desc": "헌신적이고 배려심 깊은 ISFJ에게는 든든하고 따뜻한 포켓몬이 어울려요."
    },
    "ESTJ": {
        "pokemons": [
            {"name": "핫삼", "desc": "체계적이고 강력한 실행력을 가진 강철/벌레 타입. 조직적인 ESTJ와 잘 맞아요."},
            {"name": "딱구리 진화형 대신 딱정곤", "desc": "규율과 효율을 중시하는 강철 타입."},
        ],
        "desc": "체계적이고 실행력이 강한 ESTJ에게는 강력하고 조직적인 포켓몬이 어울려요."
    },
    "ESFJ": {
        "pokemons": [
            {"name": "핑크리 대신 픽시", "desc": "다정하고 사교적인 페어리 타입. 사람들과의 관계를 중시하는 ESFJ와 닮았어요."},
            {"name": "이브이", "desc": "누구와도 잘 어울리는 사랑스러운 포켓몬."},
        ],
        "desc": "다정하고 사교적인 ESFJ에게는 사랑스럽고 친화력 좋은 포켓몬이 어울려요."
    },
    "ISTP": {
        "pokemons": [
            {"name": "루카리오 대신 게라오스", "desc": "실전에 강하고 손재주 좋은 격투 타입. 실용적인 ISTP와 잘 맞아요."},
            {"name": "쟈랑고", "desc": "냉철하고 효율적인 강철/에스퍼 타입."},
        ],
        "desc": "손재주가 좋고 실용적인 ISTP에게는 실전에 강한 포켓몬이 어울려요."
    },
    "ISFP": {
        "pokemons": [
            {"name": "이상해꽃 대신 라란티스", "desc": "예술적이고 우아한 풀/유령 타입. 감성적인 ISFP와 닮았어요."},
            {"name": "밀로틱", "desc": "아름답고 온화한 성격의 물 타입."},
        ],
        "desc": "예술적 감각이 뛰어나고 온화한 ISFP에게는 우아하고 아름다운 포켓몬이 어울려요."
    },
    "ESTP": {
        "pokemons": [
            {"name": "부스터", "desc": "열정적이고 즉흥적인 불 타입. 모험을 즐기는 ESTP와 잘 맞아요."},
            {"name": "윤겔라 대신 번치코", "desc": "빠르고 화끈한 액션을 보여주는 포켓몬."},
        ],
        "desc": "모험을 즐기고 즉흥적인 ESTP에게는 열정적이고 다이내믹한 포켓몬이 어울려요."
    },
    "ESFP": {
        "pokemons": [
            {"name": "치코리타 대신 파이리", "desc": "밝고 사랑스러운 불 타입. 무대를 즐기는 ESFP와 닮았어요."},
            {"name": "폴리곤 대신 뮤르크", "desc": "화려하고 매력적인 포켓몬."},
        ],
        "desc": "밝고 사교적이며 무대를 즐기는 ESFP에게는 화려하고 매력적인 포켓몬이 어울려요."
    },
}

st.set_page_config(page_title="MBTI 포켓몬 추천", page_icon="🎮", layout="centered")

st.title("🎮 MBTI 포켓몬 추천 웹앱")
st.write("당신의 MBTI를 선택하면 어울리는 포켓몬을 추천해드려요!")

mbti_list = list(mbti_pokemon.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

if st.button("포켓몬 추천 받기 ✨"):
    data = mbti_pokemon[selected_mbti]
    st.subheader(f"🔎 {selected_mbti} 유형 설명")
    st.write(data["desc"])

    st.subheader("✅ 추천 포켓몬")
    for p in data["pokemons"]:
        with st.container():
            st.markdown(f"### 🐾 {p['name']}")
            st.write(p["desc"])
            st.markdown("---")

    st.success(f"{selected_mbti} 유형에게는 위 포켓몬들이 잘 어울려요!")

st.caption("Made with Streamlit ❤️")
