"""
Gemini API 클라이언트
결과 텍스트에 다양한 표현을 입히는 역할
"""

import os
import json
import random
import requests

# 환경 변수에서 API 키 가져오기 (Vercel에서 설정)
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'AIzaSyCFAzIttkt74whEynpY11g5yrPxZjCaFJY')
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"


def generate_styled_result(result_data):
    """
    고정된 분석 데이터를 바탕으로 AI가 다양한 표현으로 꾸며줌

    Args:
        result_data: get_combined_result()의 반환값

    Returns:
        dict: AI가 생성한 추가 텍스트가 포함된 결과
    """
    if not GEMINI_API_KEY:
        # API 키 없으면 기본 템플릿 사용
        return add_default_styling(result_data)

    try:
        # 프롬프트 생성
        prompt = create_prompt(result_data)

        # Gemini API 호출
        response = call_gemini_api(prompt)

        if response:
            # AI 응답 파싱 및 결과에 추가
            styled_content = parse_gemini_response(response)
            result_data['ai_styled'] = styled_content
        else:
            result_data['ai_styled'] = get_fallback_content(result_data)

    except Exception as e:
        print(f"Gemini API 오류: {e}")
        result_data['ai_styled'] = get_fallback_content(result_data)

    return result_data


def create_prompt(result_data):
    """분석 결과를 바탕으로 Gemini 프롬프트 생성"""

    ilju = result_data['ilju']
    mbti = result_data['mbti']
    title = result_data['title']
    keywords = result_data['keywords']
    max_ohaeng = result_data['ohaeng']['max']
    min_ohaeng = result_data['ohaeng']['min']
    ilju_desc = result_data['saju'].get('ilju_description', '')
    mbti_desc = result_data['mbti_info'].get('description', '')

    # 추가 질문 정보
    extra = result_data.get('extra_info', {})
    concern = extra.get('concern', '')
    status = extra.get('status', '')
    social_style_val = extra.get('social_style', '')
    work_style_val = extra.get('work_style', '')

    # 관심사 한글 변환
    concern_map = {
        'love': '연애/인간관계',
        'career': '진로/취업',
        'money': '재물/금전운',
        'health': '건강/컨디션',
        'growth': '자기계발'
    }
    concern_kr = concern_map.get(concern, '')

    # 상황 한글 변환
    status_map = {
        'start': '새로운 시작을 앞두고 있음',
        'maintain': '현재 상황 유지 중',
        'change': '변화가 필요하다고 느낌',
        'choice': '선택의 기로에 있음'
    }
    status_kr = status_map.get(status, '')

    # 사회 성향 텍스트
    social_map = {
        'alone': '혼자가 더 편함',
        'together': '함께가 더 좋음',
        'balance': '상황에 따라 다름'
    }
    social_style = social_map.get(social_style_val, '')

    # 일 스타일 텍스트
    work_map = {
        'planned': '계획적인 성향',
        'spontaneous': '즉흥적인 성향',
        'flexible': '유연한 성향'
    }
    planning_style = work_map.get(work_style_val, '')

    prompt = f"""당신은 사주와 MBTI를 결합해 해석하는 전문가입니다.
아래 분석 데이터를 바탕으로 사용자에게 전달할 메시지를 작성해주세요.

[분석 데이터]
- 일주: {ilju}
- MBTI: {mbti}
- 타이틀: {title}
- 키워드: {', '.join(keywords)}
- 강한 오행: {max_ohaeng}
- 약한 오행: {min_ohaeng}
- 일주 특성: {ilju_desc}
- MBTI 특성: {mbti_desc}

[사용자 관심사 및 상황]
- 주요 관심사: {concern_kr}
- 현재 상황: {status_kr}
- 사회성향: {social_style}
- 계획성향: {planning_style}

[작성 지침]
1. 친근하고 재미있는 말투 (MZ세대 타겟, ㅋㅋ, ㄹㅇ 등 적절히 사용)
2. 긍정적이면서도 현실적인 조언
3. 과하게 길지 않게 (각 항목 1-2문장)
4. concern_advice는 반드시 "{concern_kr}" 관련 구체적 조언으로 작성

[출력 형식 - JSON으로만 응답]
{{
    "greeting": "첫인사 (예: 오, 꽤 독특한 조합이네요!)",
    "core_message": "핵심 성격 한줄 요약",
    "strength_tip": "강점 활용 팁",
    "weakness_tip": "약점 보완 조언",
    "concern_advice": "{concern_kr}에 대한 맞춤 조언 (2-3문장)",
    "today_message": "오늘의 한마디 (운세 스타일)",
    "emoji": "이 유형을 나타내는 이모지 1개"
}}

JSON만 출력하고 다른 텍스트는 포함하지 마세요."""

    return prompt


def call_gemini_api(prompt):
    """Gemini API 호출"""

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }],
        "generationConfig": {
            "temperature": 0.9,  # 다양한 표현을 위해 높게 설정
            "maxOutputTokens": 500,
        }
    }

    url = f"{GEMINI_API_URL}?key={GEMINI_API_KEY}"

    response = requests.post(url, headers=headers, json=data, timeout=10)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Gemini API 에러: {response.status_code} - {response.text}")
        return None


def parse_gemini_response(response):
    """Gemini 응답에서 JSON 추출"""

    try:
        text = response['candidates'][0]['content']['parts'][0]['text']

        # JSON 부분만 추출 (```json ... ``` 형태일 수 있음)
        if '```json' in text:
            text = text.split('```json')[1].split('```')[0]
        elif '```' in text:
            text = text.split('```')[1].split('```')[0]

        return json.loads(text.strip())

    except (KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"응답 파싱 오류: {e}")
        return None


def add_default_styling(result_data):
    """API 키 없을 때 기본 스타일링"""
    result_data['ai_styled'] = get_fallback_content(result_data)
    return result_data


def get_fallback_content(result_data):
    """AI 실패 시 폴백 콘텐츠 - MZ감성 버전"""

    ilju = result_data.get('ilju', '')
    mbti = result_data.get('mbti', '')
    extra = result_data.get('extra_info', {})
    concern = extra.get('concern', 'growth')

    # 다양한 인사말 풀 (MZ감성)
    greetings = [
        f"오 대박... {ilju}에 {mbti}라니 🤯",
        f"잠깐, 이 조합 실화...? ㄹㅇ 특이하네요",
        f"헐 {mbti}인데 {ilju}일주...? 흥미롭다 흥미로워",
        f"와 이거 꽤 레어한 조합인데요?",
        f"음... 뭔가 있어 보이는 조합이에요 ㅎㅎ"
    ]

    # 오늘의 메시지 풀 (운세 스타일 + MZ)
    today_messages = [
        "오늘은 일단 저지르세요. 결과는 나중에 생각해도 됨 ㅋㅋ",
        "누가 뭐래도 오늘 하루는 내가 주인공임",
        "작은 거라도 하나 이루면 그걸로 성공한 하루예요",
        "오늘 만나는 사람 중에 인연이 있을지도...?",
        "그냥 맛있는 거 먹어요. 그게 답임",
        "평소에 못 했던 말, 오늘은 해도 될 듯",
        "sns 좀 쉬고 나한테 집중하는 하루 어때요"
    ]

    # MBTI별 이모지
    mbti_emojis = {
        'INTJ': '🧠', 'INTP': '🔬', 'ENTJ': '👔', 'ENTP': '💡',
        'INFJ': '🌙', 'INFP': '🦋', 'ENFJ': '🌟', 'ENFP': '🎨',
        'ISTJ': '📋', 'ISFJ': '🤗', 'ESTJ': '📊', 'ESFJ': '💝',
        'ISTP': '🔧', 'ISFP': '🎸', 'ESTP': '🎯', 'ESFP': '🎭'
    }

    # 강점/약점 팁 (MZ 말투)
    ohaeng_tips = {
        '목': {
            'strength': "성장 욕구 미쳤음 ㅋㅋ 새로운 거 도전하면 무조건 잘할 타입",
            'weakness': "근데 가끔은 쉬어도 됨... 번아웃 조심해요 제발"
        },
        '화': {
            'strength': "열정 MAX! 그 에너지 진짜 부럽다... 주변 사람들 다 챙기는 스타일",
            'weakness': "화나면 일단 물 한 잔 마시고 3초 세기. 진심임"
        },
        '토': {
            'strength': "믿음직함 그 자체. 주변에서 다 당신한테 기대는 이유가 있음",
            'weakness': "변화도 나쁘지 않아요... 새로운 거 해보는 것도 꿀잼일 수 있음"
        },
        '금': {
            'strength': "결정 장애? 그런 거 없음. 딱딱 판단하는 거 진짜 멋있어요",
            'weakness': "완벽 안 해도 됨. 80%만 해도 상위권이에요 ㄹㅇ"
        },
        '수': {
            'strength': "남들이 못 보는 거 보는 눈 있음. 그 통찰력 믿으세요",
            'weakness': "생각 그만하고 일단 해보세요. 행동이 답 줄 때도 있음"
        }
    }

    max_oh = result_data['ohaeng']['max']
    min_oh = result_data['ohaeng']['min']

    # 핵심 메시지도 더 캐주얼하게
    core_messages = [
        f"{max_oh}의 기운이 넘치는 당신, {mbti}답게 세상 똑부러지게 살아가는 중",
        f"겉으론 {mbti}인데 속은 {ilju}의 기운이 숨어있는 반전매력 보유자",
        f"이성적인 {mbti} 같지만 사실 {max_oh} 에너지로 움직이는 사람"
    ]

    # 관심사별 조언
    concern_advices = {
        'love': f"{mbti}인 당신, 연애에서는 솔직함이 무기예요. 근데 {max_oh} 기운이 강해서 가끔 너무 직진할 수도 있으니 속도 조절 필요! 상대방 반응 보면서 천천히 가도 괜찮아요.",
        'career': f"진로 고민 중이라면? {ilju}의 기운 + {mbti} 조합은 꽤 괜찮은 커리어 운이에요. 특히 {max_oh} 에너지가 강하니까 그쪽 분야 노려보는 것도 방법!",
        'money': f"재물운? {ilju}일주는 실속파라 돈 관리 잘할 타입이에요 ㅋㅋ 근데 {mbti}답게 가끔 충동구매 주의... 특히 스트레스 받을 때!",
        'health': f"컨디션 관리가 고민이라면, {max_oh} 에너지 과다일 수 있어요. {mbti}는 번아웃 오기 전까지 모르는 타입이니까... 쉴 때 확실히 쉬세요 제발!",
        'growth': f"자기계발 욕구 뿜뿜! {ilju}의 성실함 + {mbti}의 분석력이면 뭘 해도 잘할 타입이에요. 근데 너무 많이 벌리지 말고 하나씩 집중하는 게 포인트!"
    }

    return {
        "greeting": random.choice(greetings),
        "core_message": random.choice(core_messages),
        "strength_tip": ohaeng_tips.get(max_oh, {}).get('strength', '당신의 강점을 믿으세요!'),
        "weakness_tip": ohaeng_tips.get(min_oh, {}).get('weakness', '약점도 매력이 될 수 있어요'),
        "concern_advice": concern_advices.get(concern, concern_advices['growth']),
        "today_message": random.choice(today_messages),
        "emoji": mbti_emojis.get(mbti, '✨')
    }
