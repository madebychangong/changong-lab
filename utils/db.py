"""
Supabase 데이터베이스 연결
결제 완료된 결과를 저장하고 고유 URL로 접근 가능하게 함
"""

import os
import json
import uuid

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


def generate_result_id(result_data=None):
    """UUID 생성"""
    return str(uuid.uuid4())


def save_premium_result(result_id, result_data, product_type, payment_key=None):
    """
    유료 결과 저장 (pay_orders 테이블)

    Args:
        result_id: UUID
        result_data: 전체 결과 데이터
        product_type: 'yearly' (2026년 운세) 또는 'compatibility' (궁합)
        payment_key: 결제 키 (토스페이먼츠 paymentKey)

    Returns:
        bool: 저장 성공 여부
    """
    supabase = get_supabase()
    if not supabase:
        return False

    try:
        # data 컬럼에 결과와 product_type 함께 저장
        data_to_save = {
            'result': result_data,
            'product_type': product_type
        }

        row = {
            'id': result_id,
            'data': data_to_save,
            'payment_key': payment_key
        }

        supabase.table('pay_orders').insert(row).execute()
        return True

    except Exception as e:
        print(f"결과 저장 실패: {e}")
        return False


def get_premium_result(result_id):
    """
    저장된 유료 결과 조회

    Args:
        result_id: UUID

    Returns:
        dict or None: 결과 데이터
    """
    supabase = get_supabase()
    if not supabase:
        return None

    try:
        response = supabase.table('pay_orders').select('*').eq('id', result_id).execute()

        if response.data and len(response.data) > 0:
            row = response.data[0]
            data = row['data']

            # data가 문자열이면 파싱
            if isinstance(data, str):
                data = json.loads(data)

            return {
                'id': row['id'],
                'result_data': data.get('result', {}),
                'product_type': data.get('product_type', 'yearly'),
                'created_at': row['created_at']
            }

        return None

    except Exception as e:
        print(f"결과 조회 실패: {e}")
        return None


def check_payment_exists(payment_key):
    """결제 키로 이미 처리된 결제인지 확인"""
    supabase = get_supabase()
    if not supabase:
        return False

    try:
        response = supabase.table('pay_orders').select('id').eq('payment_key', payment_key).execute()
        return len(response.data) > 0
    except:
        return False
