"""
MBTI 16유형 데이터
"""

MBTI_DATA = {
    'INTJ': {
        'name': '전략가',
        'keywords': ['독립적', '전략적', '완벽주의'],
        'description': '모든 것에 계획이 있는 사색가. 혼자 있는 시간을 즐기며 깊이 있는 사고를 추구함.',
        'strength': '논리적 분석력, 장기적 비전',
        'weakness': '감정 표현 부족, 타인에게 냉정해 보임',
        'energy': 'I', 'info': 'N', 'decision': 'T', 'lifestyle': 'J'
    },
    'INTP': {
        'name': '논리술사',
        'keywords': ['분석적', '호기심', '독창적'],
        'description': '끝없는 지적 호기심의 소유자. 이론과 아이디어의 세계에 빠져듦.',
        'strength': '창의적 문제해결, 객관적 분석',
        'weakness': '실행력 부족, 현실감각 약함',
        'energy': 'I', 'info': 'N', 'decision': 'T', 'lifestyle': 'P'
    },
    'ENTJ': {
        'name': '통솔자',
        'keywords': ['리더십', '결단력', '효율추구'],
        'description': '타고난 리더. 목표를 정하면 거침없이 밀어붙이는 추진력 보유.',
        'strength': '카리스마, 조직 장악력',
        'weakness': '독단적, 감정 무시 경향',
        'energy': 'E', 'info': 'N', 'decision': 'T', 'lifestyle': 'J'
    },
    'ENTP': {
        'name': '변론가',
        'keywords': ['논쟁', '창의적', '도전적'],
        'description': '지적 스파링을 즐기는 아이디어 뱅크. 불가능을 가능으로 만드는 발상력.',
        'strength': '순발력, 다양한 관점',
        'weakness': '마무리 약함, 논쟁 과열',
        'energy': 'E', 'info': 'N', 'decision': 'T', 'lifestyle': 'P'
    },
    'INFJ': {
        'name': '옹호자',
        'keywords': ['이상주의', '통찰력', '헌신적'],
        'description': '조용하지만 강한 신념의 소유자. 타인의 감정을 꿰뚫어 보는 능력.',
        'strength': '공감 능력, 비전 제시',
        'weakness': '번아웃 취약, 이상과 현실 괴리',
        'energy': 'I', 'info': 'N', 'decision': 'F', 'lifestyle': 'J'
    },
    'INFP': {
        'name': '중재자',
        'keywords': ['이상적', '창의적', '감성적'],
        'description': '내면의 가치를 중시하는 몽상가. 예술적 감수성과 깊은 감정.',
        'strength': '창작 능력, 진정성',
        'weakness': '현실 도피, 우유부단',
        'energy': 'I', 'info': 'N', 'decision': 'F', 'lifestyle': 'P'
    },
    'ENFJ': {
        'name': '선도자',
        'keywords': ['카리스마', '이타적', '영향력'],
        'description': '사람을 이끄는 천부적 재능. 타인의 성장을 돕는 것에서 보람을 느낌.',
        'strength': '설득력, 공동체 형성',
        'weakness': '자기희생 과다, 간섭',
        'energy': 'E', 'info': 'N', 'decision': 'F', 'lifestyle': 'J'
    },
    'ENFP': {
        'name': '활동가',
        'keywords': ['열정적', '자유로운', '긍정적'],
        'description': '가능성을 보는 자유로운 영혼. 새로운 것에 대한 끝없는 호기심.',
        'strength': '에너지, 적응력',
        'weakness': '산만함, 깊이 부족',
        'energy': 'E', 'info': 'N', 'decision': 'F', 'lifestyle': 'P'
    },
    'ISTJ': {
        'name': '현실주의자',
        'keywords': ['신뢰', '책임감', '체계적'],
        'description': '한 번 맡으면 끝까지 해내는 책임감. 전통과 규칙을 중시.',
        'strength': '신뢰성, 꼼꼼함',
        'weakness': '융통성 부족, 변화 거부',
        'energy': 'I', 'info': 'S', 'decision': 'T', 'lifestyle': 'J'
    },
    'ISFJ': {
        'name': '수호자',
        'keywords': ['헌신적', '따뜻한', '세심한'],
        'description': '묵묵히 타인을 챙기는 따뜻한 수호자. 실질적인 도움을 주는 것을 좋아함.',
        'strength': '배려심, 실행력',
        'weakness': '거절 못함, 자기표현 약함',
        'energy': 'I', 'info': 'S', 'decision': 'F', 'lifestyle': 'J'
    },
    'ESTJ': {
        'name': '경영자',
        'keywords': ['조직적', '실용적', '결단력'],
        'description': '질서와 효율을 추구하는 관리자. 원칙을 세우고 지키는 것을 중시.',
        'strength': '실행력, 조직 관리',
        'weakness': '고집, 감정 배려 부족',
        'energy': 'E', 'info': 'S', 'decision': 'T', 'lifestyle': 'J'
    },
    'ESFJ': {
        'name': '집정관',
        'keywords': ['사교적', '협력적', '친절한'],
        'description': '모임의 중심에서 분위기를 이끄는 사람. 조화와 협력을 중시.',
        'strength': '친화력, 배려심',
        'weakness': '눈치 과다, 갈등 회피',
        'energy': 'E', 'info': 'S', 'decision': 'F', 'lifestyle': 'J'
    },
    'ISTP': {
        'name': '장인',
        'keywords': ['분석적', '실용적', '탐구적'],
        'description': '손으로 직접 해봐야 직성이 풀리는 장인. 문제의 원인을 파헤침.',
        'strength': '위기 대처, 실용적 해결',
        'weakness': '감정 표현 서툼, 무뚝뚝',
        'energy': 'I', 'info': 'S', 'decision': 'T', 'lifestyle': 'P'
    },
    'ISFP': {
        'name': '모험가',
        'keywords': ['예술적', '온화한', '자유로운'],
        'description': '겉은 조용하지만 내면은 열정적인 예술가. 순간을 즐기는 감각파.',
        'strength': '미적 감각, 공감 능력',
        'weakness': '장기 계획 약함, 갈등 회피',
        'energy': 'I', 'info': 'S', 'decision': 'F', 'lifestyle': 'P'
    },
    'ESTP': {
        'name': '사업가',
        'keywords': ['활동적', '현실적', '대담한'],
        'description': '일단 저지르고 보는 행동파. 스릴과 도전을 즐김.',
        'strength': '순발력, 위기 대처',
        'weakness': '충동적, 인내심 부족',
        'energy': 'E', 'info': 'S', 'decision': 'T', 'lifestyle': 'P'
    },
    'ESFP': {
        'name': '연예인',
        'keywords': ['사교적', '즉흥적', '낙천적'],
        'description': '파티의 중심, 분위기 메이커. 현재를 즐기는 낙천주의자.',
        'strength': '에너지, 적응력',
        'weakness': '장기 계획 약함, 깊이 부족',
        'energy': 'E', 'info': 'S', 'decision': 'F', 'lifestyle': 'P'
    }
}

def get_mbti_info(mbti_type):
    """MBTI 유형 정보 반환"""
    return MBTI_DATA.get(mbti_type.upper(), None)
