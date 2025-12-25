"""
Gemini API 클라이언트
결과 텍스트에 다양한 표현을 입히는 역할
"""

import os
import json
import random
import requests

# 환경 변수에서 API 키 가져오기 (Vercel에서 설정)
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"


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

[작성 지침]
1. 친근하고 재미있는 말투 (MZ세대 타겟)
2. 긍정적이면서도 현실적인 조언
3. 과하게 길지 않게 (각 항목 1-2문장)

[출력 형식 - JSON으로만 응답]
{{
    "greeting": "첫인사 (예: 오, 꽤 독특한 조합이네요!)",
    "core_message": "핵심 성격 한줄 요약",
    "strength_tip": "강점 활용 팁",
    "weakness_tip": "약점 보완 조언",
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
    """AI 실패 시 폴백 콘텐츠"""

    # 다양한 인사말 풀
    greetings = [
        "흥미로운 조합이네요!",
        "꽤 독특한 기운을 가지고 계시네요.",
        "재미있는 결과가 나왔어요!",
        "오, 이런 조합은 흔치 않아요.",
        "당신만의 특별한 에너지가 보여요."
    ]

    # 오늘의 메시지 풀
    today_messages = [
        "오늘은 새로운 시도가 좋은 결과를 가져올 거예요.",
        "주변 사람들에게 먼저 다가가 보세요.",
        "작은 성취에도 스스로를 칭찬해주세요.",
        "오늘 하루, 당신의 강점에 집중해보세요.",
        "예상치 못한 곳에서 기회가 올 수 있어요."
    ]

    # 강점/약점 팁
    ohaeng_tips = {
        '목': {
            'strength': "성장하려는 의지가 강점이에요. 새로운 도전을 두려워하지 마세요.",
            'weakness': "너무 앞만 보고 달리지 말고, 가끔은 쉬어가는 것도 필요해요."
        },
        '화': {
            'strength': "뜨거운 열정이 매력이에요. 그 에너지로 주변을 밝혀주세요.",
            'weakness': "감정이 앞설 때는 심호흡 한 번. 차분함이 힘이 될 거예요."
        },
        '토': {
            'strength': "묵직한 안정감이 강점이에요. 사람들이 당신을 믿고 의지해요.",
            'weakness': "변화를 두려워하지 마세요. 새로운 것도 당신의 것이 될 수 있어요."
        },
        '금': {
            'strength': "날카로운 판단력이 강점이에요. 결정이 필요할 때 빛을 발해요.",
            'weakness': "가끔은 완벽하지 않아도 괜찮아요. 과정도 소중하니까요."
        },
        '수': {
            'strength': "깊은 통찰력이 매력이에요. 남들이 못 보는 걸 보는 눈이 있어요.",
            'weakness': "생각이 많을 땐 일단 움직여보세요. 행동이 답을 줄 때도 있어요."
        }
    }

    max_oh = result_data['ohaeng']['max']
    min_oh = result_data['ohaeng']['min']

    return {
        "greeting": random.choice(greetings),
        "core_message": result_data['combination']['summary'],
        "strength_tip": ohaeng_tips.get(max_oh, {}).get('strength', '당신의 강점을 믿으세요.'),
        "weakness_tip": ohaeng_tips.get(min_oh, {}).get('weakness', '약점도 극복할 수 있어요.'),
        "today_message": random.choice(today_messages),
        "emoji": "✨"
    }
