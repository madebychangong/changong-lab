"""
사주 + MBTI 결합 결과 생성 모듈
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.mbti_data import MBTI_DATA
from data.ilju_data import ILJU_DATA

# 오행 + MBTI 조합 해석 템플릿
OHAENG_MBTI_COMBINATIONS = {
    # 목(木) + MBTI 조합
    ('목', 'E'): '나무처럼 뻗어나가는 성장 에너지가 외향성과 만나 주변을 이끄는 리더형.',
    ('목', 'I'): '내면에서 조용히 성장하는 큰 나무. 겉으론 조용하지만 꾸준히 위로 자람.',
    ('목', 'N'): '가능성을 향해 뻗어가는 나뭇가지처럼, 미래와 아이디어를 향한 끝없는 성장.',
    ('목', 'S'): '뿌리 깊은 나무처럼 현실에 단단히 발 딛고 한 걸음씩 성장함.',
    ('목', 'T'): '곧은 나무처럼 원칙적이고 논리적. 타협 없이 자신의 길을 감.',
    ('목', 'F'): '숲처럼 타인을 품어주는 따뜻함. 함께 성장하려는 마음.',
    ('목', 'J'): '계획된 방향으로 꾸준히 자라는 나무. 목표를 향한 체계적 성장.',
    ('목', 'P'): '덩굴처럼 유연하게 뻗어가는 적응력. 기회를 향해 자유롭게 성장.',

    # 화(火) + MBTI 조합
    ('화', 'E'): '활활 타오르는 불꽃이 외향성과 만나 주변을 환하게 밝히는 에너지.',
    ('화', 'I'): '속에서 타오르는 촛불. 겉은 조용하지만 내면엔 뜨거운 열정.',
    ('화', 'N'): '영감의 불꽃. 직관과 창의성이 타올라 새로운 것을 만들어냄.',
    ('화', 'S'): '따뜻한 난로불. 현실에서 주변을 따뜻하게 감싸는 실용적 열정.',
    ('화', 'T'): '단련의 불. 날카로운 논리로 핵심을 꿰뚫는 뜨거운 분석력.',
    ('화', 'F'): '사랑의 불꽃. 감정이 풍부하고 열정적으로 타인을 대함.',
    ('화', 'J'): '통제된 불. 열정을 목표를 향해 체계적으로 태움.',
    ('화', 'P'): '자유로운 불꽃. 순간의 열정에 충실하며 변화무쌍.',

    # 토(土) + MBTI 조합
    ('토', 'E'): '너른 대지가 외향성과 만나 모든 것을 포용하는 중심적 존재.',
    ('토', 'I'): '깊은 땅속의 광물. 겉으론 드러나지 않지만 내면에 보물을 품음.',
    ('토', 'N'): '씨앗을 품은 땅. 가능성과 아이디어를 키워내는 비옥한 상상력.',
    ('토', 'S'): '단단한 대지. 현실에 발 딛고 실용적으로 일을 처리.',
    ('토', 'T'): '바위 같은 원칙. 논리적이고 한번 정하면 흔들리지 않음.',
    ('토', 'F'): '어머니 대지. 타인을 품어주고 보살피는 따뜻한 포용력.',
    ('토', 'J'): '정돈된 정원. 체계적으로 관리하고 안정을 추구.',
    ('토', 'P'): '유연한 흙. 상황에 따라 형태를 바꾸며 적응.',

    # 금(金) + MBTI 조합
    ('금', 'E'): '빛나는 보석이 외향성과 만나 주목받고 영향력을 행사.',
    ('금', 'I'): '숨겨진 금맥. 겉으론 드러나지 않지만 내면에 빛나는 가치.',
    ('금', 'N'): '다듬어지는 보석. 직관으로 본질을 꿰뚫고 가능성을 깎아냄.',
    ('금', 'S'): '실용적인 도구. 현실에서 날카롭게 문제를 해결.',
    ('금', 'T'): '단단한 강철. 논리적이고 냉철하며 원칙에 철저.',
    ('금', 'F'): '따뜻한 보석. 날카로움 속에 감춰진 섬세한 감성.',
    ('금', 'J'): '정교한 시계. 정확하고 체계적으로 움직임.',
    ('금', 'P'): '유연한 금속. 상황에 따라 형태를 바꾸지만 본질은 유지.',

    # 수(水) + MBTI 조합
    ('수', 'E'): '흐르는 강물이 외향성과 만나 세상 곳곳을 적시며 영향력 확대.',
    ('수', 'I'): '깊은 바다. 겉은 고요하지만 내면엔 무한한 깊이.',
    ('수', 'N'): '구름이 되는 물. 상상력이 자유롭게 흘러 어디든 갈 수 있음.',
    ('수', 'S'): '실용적인 빗물. 현실에서 필요한 곳에 스며들어 도움.',
    ('수', 'T'): '차가운 얼음. 냉철한 분석력으로 감정에 흔들리지 않음.',
    ('수', 'F'): '따뜻한 온천. 깊은 감성으로 타인의 마음을 어루만짐.',
    ('수', 'J'): '운하의 물. 정해진 방향으로 체계적으로 흐름.',
    ('수', 'P'): '자유로운 시냇물. 상황에 따라 유연하게 흘러감.',
}

# 오행 과다/부족 해석
OHAENG_ANALYSIS = {
    '목': {
        'excess': '성장과 확장 에너지가 넘침. 이상이 높고 도전적이지만 현실과 괴리될 수 있음.',
        'lack': '성장과 시작의 에너지가 부족. 새로운 도전보다 안정을 추구하는 경향.'
    },
    '화': {
        'excess': '열정과 표현 에너지가 넘침. 감정 기복이 있고 급할 수 있음.',
        'lack': '열정과 표현이 억제됨. 내면의 열을 밖으로 표출하기 어려움.'
    },
    '토': {
        'excess': '안정과 중재 에너지가 넘침. 신중하지만 느리고 변화를 거부할 수 있음.',
        'lack': '중심과 안정감이 부족. 흔들리기 쉽고 방향을 잡기 어려움.'
    },
    '금': {
        'excess': '결단과 원칙 에너지가 넘침. 날카롭지만 냉정하고 융통성이 부족할 수 있음.',
        'lack': '결단력과 추진력이 부족. 상황을 정리하고 마무리하는 힘이 약함.'
    },
    '수': {
        'excess': '지혜와 유연함이 넘침. 생각이 깊지만 우유부단하고 감정적일 수 있음.',
        'lack': '깊은 사고와 유연함이 부족. 직관보다 눈에 보이는 것을 중시.'
    }
}


def generate_keywords(ilju_info, mbti_info, max_ohaeng):
    """결과 키워드 3개 생성"""
    keywords = []

    # 일주 키워드에서 1개
    if ilju_info and ilju_info.get('keywords'):
        keywords.append(ilju_info['keywords'][0])

    # MBTI 키워드에서 1개
    if mbti_info and mbti_info.get('keywords'):
        keywords.append(mbti_info['keywords'][0])

    # 오행 기반 키워드 1개
    ohaeng_keywords = {
        '목': '성장지향',
        '화': '열정가',
        '토': '안정추구',
        '금': '완벽주의',
        '수': '지혜로움'
    }
    keywords.append(ohaeng_keywords.get(max_ohaeng, '균형'))

    return keywords


def generate_title(ilju_info, mbti_info, max_ohaeng):
    """결과 타이틀 생성"""
    ohaeng_titles = {
        '목': '성장하는',
        '화': '빛나는',
        '토': '든든한',
        '금': '빛나는',
        '수': '깊은'
    }

    ohaeng_word = ohaeng_titles.get(max_ohaeng, '')
    mbti_name = mbti_info.get('name', '') if mbti_info else ''

    return f"{ohaeng_word} {mbti_name}"


def get_combined_result(saju_result, mbti_type, gender):
    """
    사주와 MBTI를 결합한 최종 결과 생성

    Args:
        saju_result: calculate_saju() 함수의 반환값
        mbti_type: MBTI 유형 (예: 'INTJ')
        gender: 성별 ('male' 또는 'female')

    Returns:
        dict: 결합된 분석 결과
    """
    mbti_type = mbti_type.upper()
    ilju = saju_result['ilju']

    # 기본 데이터 가져오기
    ilju_info = ILJU_DATA.get(ilju, {})
    mbti_info = MBTI_DATA.get(mbti_type, {})

    # 오행 분석
    ohaeng = saju_result['ohaeng']
    max_ohaeng = saju_result['max_ohaeng']
    min_ohaeng = saju_result['min_ohaeng']
    day_ohaeng = saju_result['day_gan_ohaeng']

    # MBTI 개별 문자 추출
    mbti_e = mbti_type[0]  # E or I
    mbti_n = mbti_type[1]  # N or S
    mbti_t = mbti_type[2]  # T or F
    mbti_j = mbti_type[3]  # J or P

    # 조합 해석 생성
    combination_texts = []
    for letter in [mbti_e, mbti_n, mbti_t, mbti_j]:
        key = (day_ohaeng, letter)
        if key in OHAENG_MBTI_COMBINATIONS:
            combination_texts.append(OHAENG_MBTI_COMBINATIONS[key])

    # 오행 과다/부족 분석
    excess_analysis = OHAENG_ANALYSIS.get(max_ohaeng, {}).get('excess', '')
    lack_analysis = OHAENG_ANALYSIS.get(min_ohaeng, {}).get('lack', '')

    # 키워드 및 타이틀 생성
    keywords = generate_keywords(ilju_info, mbti_info, max_ohaeng)
    title = generate_title(ilju_info, mbti_info, max_ohaeng)

    # 결과 조합
    result = {
        # 기본 정보
        'ilju': ilju,
        'ilju_name': ilju_info.get('name', ilju),
        'mbti': mbti_type,
        'mbti_name': mbti_info.get('name', mbti_type),
        'gender': gender,

        # 핵심 결과
        'title': title,
        'keywords': keywords,

        # 사주 분석
        'saju': {
            'year_ganji': saju_result['year_ganji'],
            'month_ganji': saju_result['month_ganji'],
            'day_ganji': saju_result['day_ganji'],
            'hour_ganji': saju_result.get('hour_ganji'),
            'ilju_description': ilju_info.get('description', ''),
            'ilju_personality': ilju_info.get('personality', ''),
            'ilju_strength': ilju_info.get('strength', ''),
            'ilju_weakness': ilju_info.get('weakness', ''),
        },

        # 오행 분석
        'ohaeng': {
            'counts': ohaeng,
            'max': max_ohaeng,
            'min': min_ohaeng,
            'day_ohaeng': day_ohaeng,
            'excess_analysis': excess_analysis,
            'lack_analysis': lack_analysis,
        },

        # MBTI 분석
        'mbti_info': {
            'description': mbti_info.get('description', ''),
            'strength': mbti_info.get('strength', ''),
            'weakness': mbti_info.get('weakness', ''),
        },

        # 결합 분석
        'combination': {
            'texts': combination_texts,
            'summary': generate_combination_summary(ilju_info, mbti_info, max_ohaeng, min_ohaeng)
        },

        # 공유용 데이터
        'share': {
            'title': f"나는 '{title}' 유형!",
            'description': f"{ilju}일주 × {mbti_type} | #{' #'.join(keywords)}",
        }
    }

    return result


def generate_combination_summary(ilju_info, mbti_info, max_ohaeng, min_ohaeng):
    """사주와 MBTI 결합 요약문 생성"""
    ilju_keyword = ilju_info.get('keywords', [''])[0] if ilju_info else ''
    mbti_keyword = mbti_info.get('keywords', [''])[0] if mbti_info else ''

    summaries = {
        '목': f"성장을 향한 끝없는 의지가 {mbti_keyword} 성향과 만나 도전적인 삶을 살아감.",
        '화': f"타오르는 열정이 {mbti_keyword} 성향과 결합하여 주변을 밝히는 존재.",
        '토': f"중심을 잡는 안정감이 {mbti_keyword} 성향과 어우러져 신뢰받는 사람.",
        '금': f"날카로운 분별력이 {mbti_keyword} 성향과 만나 완벽을 추구함.",
        '수': f"깊은 지혜가 {mbti_keyword} 성향과 결합하여 통찰력 있는 판단을 함.",
    }

    return summaries.get(max_ohaeng, f"{ilju_keyword}과 {mbti_keyword}이 어우러진 독특한 조합.")
