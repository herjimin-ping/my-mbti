import streamlit as st

# 포켓몬 공식 아트워크 이미지 URL 생성 함수 (도감번호 기반)
def get_image_url(dex_number: int) -> str:
    return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{dex_number}.png"

# MBTI별 추천 포켓몬 데이터 (도감번호 포함)
mbti_pokemon = {
    "INTJ": {
        "desc": "논리적이고 전략적인 사고를 하는 INTJ에게는 강력한 지능형 포켓몬이 어울려요.",
        "pokemons": [
            {"name": "메타그로스", "dex": 376, "desc": "치밀한 전략과 압도적인 힘을 겸비한 강철/에스퍼 타입. 완벽주의적인 INTJ와 잘 어울려요."},
            {"name": "다크라이", "dex": 491, "desc": "혼자만의 세계에서 깊이 사고하는 신비로운 포켓몬. 통찰력 있는 INTJ와 닮았어요."},
        ],
    },
    "INTP": {
        "desc": "탐구심이 강하고 독창적인 INTP에게는 신비롭고 개성 강한 포켓몬이 어울려요.",
        "pokemons": [
            {"name": "팬텀", "dex": 94, "desc": "장난기 넘치고 예측 불가능한 사고를 즐기는 유령/독 타입. 엉뚱한 발상을 좋아하는 INTP와 닮았어요."},
            {"name": "네이티오", "dex": 178, "desc": "조용히 미래를 통찰하는 신비로운 에스퍼/비행 타입."},
        ],
    },
    "ENTJ": {
        "desc": "타고난 리더십과 추진력을 가진 ENTJ에게는 카리스마 넘치는 포켓몬이 어울려요.",
        "pokemons": [
            {"name": "리자몽", "dex": 6, "desc": "압도적인 카리스마와 힘으로 무리를 이끄는 불꽃/비행 타입."},
            {"name": "갸라도스", "dex": 130, "desc": "강력한 파워로 목표를 밀어붙이는 리더형 포켓몬."},
        ],
    },
    "ENTP": {
        "desc": "창의적이고 논쟁을 즐기는 ENTP에게는 재치있고 변화무쌍한 포켓몬이 어울려요.",
        "pokemons": [
            {"name": "조로아크", "dex": 571, "desc": "환영으로 상대를 속이는 재치있는 악 타입. 새로운 아이디어를 좋아하는 ENTP와 닮았어요."},
            {"name": "치리치노", "dex": 573, "desc": "영리하고 임기응변에 강한 포켓몬."},
        ],
    },
    "INFJ": {
        "desc": "깊은 통찰력과 이상을 가진 INFJ에게는 신비롭고 지혜로운 포켓몬이 어울려요.",
        "pokemons": [
            {"name": "뮤츠", "dex": 150, "desc": "깊은 내면의 힘과 고뇌를 가진 에스퍼 타입. 이상주의적인 INFJ와 잘 맞아요."},
            {"name": "라티오스", "dex": 381, "desc": "타인과 깊은 유대감을 나누는 온화한 드래곤/에스퍼 포켓몬."},
        ],
    },
    "INFP": {
        "desc": "따뜻한 감성과 이상을 품은 INFP에게는 순수하고 신비로운 포켓몬이 어울려요.",
        "pokemons": [
            {"name": "뮤", "dex": 151, "desc": "순수하고 무한한 가능성을 가진 신비로운 포켓몬."},
            {"name": "세레비", "dex": 251, "desc": "시간을 초월한 따뜻한 유대감을 상징하는 포켓몬."},
        ],
    },
    "ENFJ": {
        "desc": "타인을 이끌고 돌보는 ENFJ에게는 카리스마 있고 배려심 깊은 포켓몬이 어울려요.",
        "pokemons": [
            {"name": "루카리오", "dex": 448, "desc": "타인의 감정을 잘 읽고 이끄는 강철/격투 타입."},
            {"name": "라이코", "dex": 243, "desc": "카리스마와 따뜻한 리더십을 가진 전설의 포켓몬."},
        ],
    },
    "ENFP": {
        "desc": "열정적이고 사교적인 ENFP에게는 밝고 에너지 넘치는 포켓몬이 어울려요.",
        "pokemons": [
            {"name": "피카츄", "dex": 25, "desc": "활발하고 사랑받는 에너지 넘치는 포켓몬."},
            {"name": "메가니움", "dex": 154, "desc": "밝고 따뜻한 에너지를 가진 풀 타입."},
        ],
    },
    "ISTJ": {
        "desc": "성실하고 원칙적인 ISTJ에게는 단단하고 신뢰할 수 있는 포켓몬이 어울려요.",
        "pokemons": [
            {"name": "보스로라", "dex": 306, "desc": "단단한 갑옷으로 무장한 강철 타입. 원칙을 중시하는 ISTJ와 잘 맞아요."},
            {"name": "한카리아스", "dex": 635, "desc": "묵묵히 맡은 역할을 해내는 강철/드래곤 타입."},
        ],
    },
    "ISFJ": {
        "desc": "헌신적이고 배려심 깊은 ISFJ에게는 든든하고 따뜻한 포켓몬이 어울려요.",
        "pokemons": [
            {"name": "잠만보", "dex": 143, "desc": "느긋하지만 든든하게 곁을 지켜주는 노말 타입."},
            {"name": "라프라스", "dex": 131, "desc": "다정하고 헌신적인 성격으로 남을 태워주는 물/얼음 타입."},
        ],
    },
    "ESTJ": {
        "desc": "체계적이고 실행력이 강한 ESTJ에게는 강력하고 조직적인 포켓몬이 어울려요.",
        "pokemons": [
            {"name": "핫삼", "dex": 212, "desc": "체계적이고 강력한 실행력을 가진 강철/벌레 타입."},
            {"name": "니드킹", "dex": 34, "desc": "강한 힘과 카리스마로 무리를 통솔하는 독/땅 타입."},
        ],
    },
    "ESFJ": {
        "desc": "다정하고 사교적인 ESFJ에게는 사랑스럽고 친화력 좋은 포켓몬이 어울려요.",
        "pokemons": [
            {"name": "픽시", "dex": 36, "desc": "다정하고 사교적인 페어리 타입."},
            {"name": "이브이", "dex": 133, "desc": "누구와도 잘 어울리는 사랑스러운 포켓몬."},
        ],
    },
    "ISTP": {
        "desc": "손재주가 좋고 실용적인 ISTP에게는 실전에 강한 포켓몬이 어울려요.",
        "pokemons": [
            {"name": "헤라크로스", "dex": 214, "desc": "실전에 강하고 힘이 넘치는 벌레/격투 타입."},
            {"name": "리오르", "dex": 447, "desc": "냉철하고 침착하게 실력을 쌓아가는 격투 타입."},
        ],
    },
    "ISFP": {
        "desc": "예술적 감각이 뛰어나고 온화한 ISFP에게는 우아하고 아름다운 포켓몬이 어울려요.",
        "pokemons": [
            {"name": "밀로틱", "dex": 350, "desc": "아름답고 온화한 성격의 물 타입."},
            {"name": "라플레시아", "dex": 45, "desc": "화려하고 개성 있는 매력을 가진 풀 타입."},
        ],
    },
    "ESTP": {
        "desc": "모험을 즐기고 즉흥적인 ESTP에게는 열정적이고 다이내믹한 포켓몬이 어울려요.",
        "pokemons": [
            {"name": "부스터", "dex": 136, "desc": "열정적이고 즉흥적인 불꽃 타입."},
            {"name": "초염몽", "dex": 392, "desc": "빠르고 화끈한 액션을 보여주는 불꽃/격투 타입."},
        ],
    },
    "ESFP": {
        "desc": "밝고 사교적이며 무대를 즐기는 ESFP에게는 화려하고 매력적인 포켓몬이 어울려요.",
        "pokemons": [
            {"name": "파이리", "dex": 4, "desc": "밝고 사랑스러운 불꽃 타입."},
            {"name": "치코리타", "dex": 152, "desc": "귀엽고 사랑받는 매력적인 풀 타입."},
        ],
    },
}

st.set_page_config(page_title="MBTI 포켓몬 추천", page_icon="🎮", layout="centered")

st.title("🎮 MBTI 포켓몬 추천 웹앱")
st.write("당신의 MBTI를 선택하면 어울리는 포켓몬을 이미지와 함께 추천해드려요!")

mbti_list = list(mbti_pokemon.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

if st.button("포켓몬 추천 받기 ✨"):
    data = mbti_pokemon[selected_mbti]
    st.subheader(f"🔎 {selected_mbti} 유형 설명")
    st.write(data["desc"])

    st.subheader("✅ 추천 포켓몬")
    cols = st.columns(len(data["pokemons"]))
    for col, p in zip(cols, data["pokemons"]):
        with col:
            st.markdown(f"<h3 style='text-align: center;'>🐾 {p['name']}</h3>", unsafe_allow_html=True)
            st.image(get_image_url(p["dex"]), use_container_width=True)
            st.write(p["desc"])

    st.success(f"{selected_mbti} 유형에게는 위 포켓몬들이 잘 어울려요!")

st.caption("이미지 출처: PokeAPI 공식 스프라이트 저장소 · Made with Streamlit ❤️")
