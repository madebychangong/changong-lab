from flask import Flask, render_template, request, jsonify
from utils.saju_calculator import calculate_saju
from utils.result_generator import get_combined_result
from utils.gemini_client import generate_styled_result
import os

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')

@app.route('/')
def home():
    """메인 랜딩 페이지"""
    return render_template('index.html')

@app.route('/input')
def input_page():
    """사용자 정보 입력 페이지"""
    return render_template('input.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """사주 + MBTI 분석 처리"""
    try:
        # 입력 데이터 받기
        birth_year = int(request.form.get('birth_year'))
        birth_month = int(request.form.get('birth_month'))
        birth_day = int(request.form.get('birth_day'))
        birth_hour = request.form.get('birth_hour', '')
        is_lunar = request.form.get('is_lunar') == 'true'
        gender = request.form.get('gender')
        mbti = request.form.get('mbti', '').upper()

        # 사주 계산
        saju_result = calculate_saju(
            birth_year, birth_month, birth_day,
            birth_hour, is_lunar
        )

        # 결합 결과 생성
        result = get_combined_result(saju_result, mbti, gender)

        # AI 스타일링 추가 (Gemini)
        result = generate_styled_result(result)

        return render_template('result.html', result=result)

    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    """API 엔드포인트 (향후 확장용)"""
    try:
        data = request.get_json()

        saju_result = calculate_saju(
            data['birth_year'],
            data['birth_month'],
            data['birth_day'],
            data.get('birth_hour', ''),
            data.get('is_lunar', False)
        )

        result = get_combined_result(
            saju_result,
            data['mbti'],
            data['gender']
        )

        # AI 스타일링 추가
        result = generate_styled_result(result)

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Vercel serverless 함수용
app = app
