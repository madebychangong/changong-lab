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

    # 운세 타입
    extra = result_data.get('extra_info', {})
    fortune_type = extra.get('fortune_type', 'overall')

    # 운세 타입별 프롬프트
    fortune_prompts = {
        'overall': '종합적인 성격과 운세',
        'love': '연애 성향과 인연운',
        'money': '재물운과 금전 관리 성향',
        'career': '직업 적성과 진로 방향'
    }
    fortune_focus = fortune_prompts.get(fortune_type, fortune_prompts['overall'])

    prompt = f"""당신은 사주와 MBTI를 결합해 해석하는 전문가입니다.

[분석 데이터]
- 일주: {ilju}
- MBTI: {mbti}
- 타이틀: {title}
- 키워드: {', '.join(keywords)}
- 강한 오행: {max_ohaeng}
- 약한 오행: {min_ohaeng}
- 일주 특성: {ilju_desc}
- MBTI 특성: {mbti_desc}

[요청 운세: {fortune_focus}]

[작성 지침]
1. 친근한 말투로 작성 (MZ세대 타겟)
2. "{fortune_focus}"에 집중해서 분석
3. 각 항목 1-2문장으로 간결하게

[출력 형식 - JSON으로만 응답]
{{
    "core_message": "{fortune_focus}에 대한 핵심 분석 (2-3문장)",
    "strength_tip": "이 운세에서의 강점이나 조언",
    "weakness_tip": "주의할 점이나 보완할 부분",
    "today_message": "오늘의 한마디"
}}

JSON만 출력하세요."""

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

    ilju = result_data.get('ilju', '')
    mbti = result_data.get('mbti', '')
    extra = result_data.get('extra_info', {})
    fortune_type = extra.get('fortune_type', 'overall')
    max_oh = result_data['ohaeng']['max']

    # 운세 타입별 핵심 메시지
    core_messages = {
        'overall': f"{ilju}일주에 {mbti}인 당신은 {max_oh}의 기운이 강해요. 독특한 조합으로 자신만의 길을 개척하는 타입!",
        'love': f"{mbti}답게 연애에서도 자기 스타일이 확실해요. {max_oh} 기운이 강해서 감정 표현도 솔직한 편이에요.",
        'money': f"{ilju}일주는 재물 관리에 꽤 실속파예요. {mbti}의 성격과 합쳐져서 계획적인 소비 습관을 가질 수 있어요.",
        'career': f"{ilju}의 기운과 {mbti}의 성격이 합쳐져서 꽤 독특한 직업 적성을 가지고 있어요. 창의력과 분석력 모두 갖춘 타입!"
    }

    strength_tips = {
        'overall': f"{max_oh} 에너지가 넘치니까 새로운 도전에 적극적이에요",
        'love': "솔직한 감정 표현이 장점이에요. 자신감 있게 다가가세요",
        'money': "실속 있는 소비 습관이 있어요. 그대로 유지하면 좋겠어요",
        'career': "자기만의 방식으로 일 처리하는 게 강점이에요"
    }

    weakness_tips = {
        'overall': "가끔은 쉬어가면서 에너지를 충전하세요",
        'love': "상대방의 속도도 맞춰주면 더 좋은 관계가 될 거예요",
        'money': "가끔 충동 소비 조심하면 좋겠어요",
        'career': "팀워크가 필요할 때는 양보도 필요해요"
    }

    today_messages = [
        "오늘 하루도 당신답게 보내세요",
        "작은 것 하나라도 이루면 성공한 하루예요",
        "자신을 믿으세요. 분명 잘 될 거예요",
        "오늘은 평소보다 조금 더 여유를 가져보세요"
    ]

    return {
        "core_message": core_messages.get(fortune_type, core_messages['overall']),
        "strength_tip": strength_tips.get(fortune_type, strength_tips['overall']),
        "weakness_tip": weakness_tips.get(fortune_type, weakness_tips['overall']),
        "today_message": random.choice(today_messages)
    }
