"""
Supabase 데이터베이스 연결
결제 완료된 결과를 저장하고 고유 URL로 접근 가능하게 함
"""

import os
import json
import hashlib
from datetime import datetime

# Supabase 설정 (환경 변수에서 가져옴)
SUPABASE_URL = os.environ.get('SUPABASE_URL', '')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY', '')

# Supabase 클라이언트 (lazy loading)
_supabase = None

def get_supabase():
    """Supabase 클라이언트 반환"""
    global _supabase

    if not SUPABASE_URL or not SUPABASE_KEY:
        return None

    if _supabase is None:
        try:
            from supabase import create_client
            _supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        except Exception as e:
            print(f"Supabase 연결 실패: {e}")
            return None

    return _supabase


def generate_result_id(result_data):
    """결과 데이터로 고유 ID 생성"""
    unique_str = f"{result_data.get('ilju', '')}-{result_data.get('mbti', '')}-{datetime.now().isoformat()}"
    return hashlib.sha256(unique_str.encode()).hexdigest()[:12]


def save_premium_result(result_id, result_data, product_type, payment_id=None):
    """
    유료 결과 저장

    Args:
        result_id: 고유 결과 ID
        result_data: 전체 결과 데이터
        product_type: 'yearly' (2026년 운세) 또는 'compatibility' (궁합)
        payment_id: 결제 ID (토스페이먼츠 등)

    Returns:
        bool: 저장 성공 여부
    """
    supabase = get_supabase()
    if not supabase:
        return False

    try:
        data = {
            'id': result_id,
            'result_data': json.dumps(result_data, ensure_ascii=False),
            'product_type': product_type,
            'payment_id': payment_id,
            'created_at': datetime.now().isoformat()
        }

        supabase.table('premium_results').insert(data).execute()
        return True

    except Exception as e:
        print(f"결과 저장 실패: {e}")
        return False


def get_premium_result(result_id):
    """
    저장된 유료 결과 조회

    Args:
        result_id: 고유 결과 ID

    Returns:
        dict or None: 결과 데이터
    """
    supabase = get_supabase()
    if not supabase:
        return None

    try:
        response = supabase.table('premium_results').select('*').eq('id', result_id).execute()

        if response.data and len(response.data) > 0:
            row = response.data[0]
            return {
                'id': row['id'],
                'result_data': json.loads(row['result_data']),
                'product_type': row['product_type'],
                'created_at': row['created_at']
            }

        return None

    except Exception as e:
        print(f"결과 조회 실패: {e}")
        return None


def check_payment_exists(payment_id):
    """결제 ID로 이미 처리된 결제인지 확인"""
    supabase = get_supabase()
    if not supabase:
        return False

    try:
        response = supabase.table('premium_results').select('id').eq('payment_id', payment_id).execute()
        return len(response.data) > 0
    except:
        return False
