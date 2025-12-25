from flask import Flask, render_template, request, jsonify, redirect, url_for
from utils.saju_calculator import calculate_saju
from utils.result_generator import get_combined_result
from utils.gemini_client import generate_styled_result
from utils.db import save_premium_result, get_premium_result, generate_result_id
import os
import json

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

        # 운세 타입
        fortune_type = request.form.get('fortune_type', 'overall')  # overall, love, money, career

        extra_info = {
            'fortune_type': fortune_type
        }

        # 사주 계산
        saju_result = calculate_saju(
            birth_year, birth_month, birth_day,
            birth_hour, is_lunar
        )

        # 결합 결과 생성
        result = get_combined_result(saju_result, mbti, gender)

        # 추가 정보 저장
        result['extra_info'] = extra_info

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


@app.route('/premium/<result_id>')
def premium_result(result_id):
    """저장된 유료 결과 조회"""
    saved = get_premium_result(result_id)

    if not saved:
        return render_template('error.html', error='결과를 찾을 수 없습니다')

    result_data = saved['result_data']
    product_type = saved['product_type']

    if product_type == 'yearly':
        return render_template('premium_yearly.html', result=result_data, result_id=result_id)
    elif product_type == 'compatibility':
        return render_template('premium_compatibility.html', result=result_data, result_id=result_id)

    return render_template('error.html', error='잘못된 결과 유형입니다')


@app.route('/api/payment/prepare', methods=['POST'])
def prepare_payment():
    """결제 준비 - 결과 데이터를 세션에 임시 저장"""
    try:
        data = request.get_json()
        product_type = data.get('product_type')  # 'yearly' or 'compatibility'
        result_data = data.get('result_data')

        # 고유 ID 생성
        result_id = generate_result_id(result_data)

        return jsonify({
            'success': True,
            'result_id': result_id,
            'product_type': product_type
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/payment/complete', methods=['POST'])
def complete_payment():
    """결제 완료 후 결과 저장"""
    try:
        data = request.get_json()
        result_id = data.get('result_id')
        result_data = data.get('result_data')
        product_type = data.get('product_type')
        payment_id = data.get('payment_id')  # 토스페이먼츠 결제 ID

        # DB에 저장
        success = save_premium_result(result_id, result_data, product_type, payment_id)

        if success:
            return jsonify({
                'success': True,
                'result_url': f'/premium/{result_id}'
            })
        else:
            return jsonify({'error': '결과 저장 실패'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Vercel serverless 함수용
app = app
