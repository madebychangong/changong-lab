"""
사주 계산 모듈
korean_lunar_calendar 라이브러리를 활용한 만세력 계산
"""

from korean_lunar_calendar import KoreanLunarCalendar
from datetime import date

# 천간 (10개)
CHEONGAN = ['갑', '을', '병', '정', '무', '기', '경', '신', '임', '계']

# 지지 (12개)
JIJI = ['자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해']

# 천간 오행
CHEONGAN_OHAENG = {
    '갑': '목', '을': '목',
    '병': '화', '정': '화',
    '무': '토', '기': '토',
    '경': '금', '신': '금',
    '임': '수', '계': '수'
}

# 지지 오행
JIJI_OHAENG = {
    '자': '수', '축': '토',
    '인': '목', '묘': '목',
    '진': '토', '사': '화',
    '오': '화', '미': '토',
    '신': '금', '유': '금',
    '술': '토', '해': '수'
}

# 시간대별 지지 매핑
HOUR_TO_JIJI = {
    '23-01': '자', '01-03': '축', '03-05': '인', '05-07': '묘',
    '07-09': '진', '09-11': '사', '11-13': '오', '13-15': '미',
    '15-17': '신', '17-19': '유', '19-21': '술', '21-23': '해'
}

# 일주 60갑자
SIXTY_GANJI = []
for i in range(60):
    SIXTY_GANJI.append(CHEONGAN[i % 10] + JIJI[i % 12])


def get_hour_jiji(hour_str):
    """시간 문자열을 지지로 변환"""
    if not hour_str:
        return None

    try:
        hour = int(hour_str)
        if 23 <= hour or hour < 1:
            return '자'
        elif 1 <= hour < 3:
            return '축'
        elif 3 <= hour < 5:
            return '인'
        elif 5 <= hour < 7:
            return '묘'
        elif 7 <= hour < 9:
            return '진'
        elif 9 <= hour < 11:
            return '사'
        elif 11 <= hour < 13:
            return '오'
        elif 13 <= hour < 15:
            return '미'
        elif 15 <= hour < 17:
            return '신'
        elif 17 <= hour < 19:
            return '유'
        elif 19 <= hour < 21:
            return '술'
        elif 21 <= hour < 23:
            return '해'
    except:
        return None


def calculate_year_ganji(year):
    """연주(년간지) 계산"""
    # 1984년이 갑자년 기준
    base_year = 1984
    index = (year - base_year) % 60
    if index < 0:
        index += 60
    return CHEONGAN[index % 10], JIJI[index % 12]


def calculate_day_ganji(year, month, day):
    """일주 간지 계산 (기준일로부터 계산)"""
    # 1900년 1월 1일은 갑진일 (index 40)
    base_date = date(1900, 1, 1)
    target_date = date(year, month, day)
    diff = (target_date - base_date).days
    index = (diff + 40) % 60
    gan = CHEONGAN[index % 10]
    ji = JIJI[index % 12]
    return gan, ji


def calculate_month_ganji(year, month, year_gan):
    """월주 간지 계산"""
    # 월지: 1월=인, 2월=묘, 3월=진...
    month_ji_list = ['인', '묘', '진', '사', '오', '미', '신', '유', '술', '해', '자', '축']
    month_ji = month_ji_list[(month - 1) % 12]

    # 월간: 연간에 따라 결정 (갑기년 병인월, 을경년 무인월...)
    year_gan_idx = CHEONGAN.index(year_gan)
    base_gan_idx = (year_gan_idx % 5) * 2 + 2  # 인월 천간 시작점
    month_gan_idx = (base_gan_idx + month - 1) % 10
    month_gan = CHEONGAN[month_gan_idx]

    return month_gan, month_ji


def calculate_saju(year, month, day, hour='', is_lunar=False):
    """
    사주팔자 계산 메인 함수

    Args:
        year: 출생 연도
        month: 출생 월
        day: 출생 일
        hour: 출생 시간 (0-23, 빈 문자열이면 시주 제외)
        is_lunar: 음력 여부

    Returns:
        dict: 사주 정보
    """
    calendar = KoreanLunarCalendar()

    # 음력이면 양력으로 변환
    if is_lunar:
        calendar.setLunarDate(year, month, day, False)
        solar_date = calendar.SolarIsoFormat()
        year, month, day = map(int, solar_date.split('-'))

    # 연주 계산
    year_gan, year_ji = calculate_year_ganji(year)
    year_ganji = year_gan + year_ji

    # 월주 계산
    month_gan, month_ji = calculate_month_ganji(year, month, year_gan)
    month_ganji = month_gan + month_ji

    # 일주 계산 (핵심!)
    day_gan, day_ji = calculate_day_ganji(year, month, day)
    day_ganji = day_gan + day_ji
    ilju = day_ganji

    # 시주 (선택)
    hour_ji = get_hour_jiji(hour) if hour else None
    hour_gan = None
    if hour_ji:
        # 시간 천간 계산 (일간 기준)
        day_gan_idx = CHEONGAN.index(day_gan)
        hour_ji_idx = JIJI.index(hour_ji)
        hour_gan_idx = (day_gan_idx * 2 + hour_ji_idx) % 10
        hour_gan = CHEONGAN[hour_gan_idx]

    # 오행 분석
    ohaeng_count = {'목': 0, '화': 0, '토': 0, '금': 0, '수': 0}

    for gan in [year_gan, month_gan, day_gan, hour_gan]:
        if gan:
            ohaeng_count[CHEONGAN_OHAENG[gan]] += 1

    for ji in [year_ji, month_ji, day_ji, hour_ji]:
        if ji:
            ohaeng_count[JIJI_OHAENG[ji]] += 1

    # 가장 강한 오행, 가장 약한 오행
    max_ohaeng = max(ohaeng_count, key=ohaeng_count.get)
    min_ohaeng = min(ohaeng_count, key=ohaeng_count.get)

    return {
        'year_ganji': year_ganji,
        'month_ganji': month_ganji,
        'day_ganji': day_ganji,
        'ilju': ilju,
        'day_gan': day_gan,
        'day_ji': day_ji,
        'hour_ganji': (hour_gan + hour_ji) if hour_gan else None,
        'ohaeng': ohaeng_count,
        'max_ohaeng': max_ohaeng,
        'min_ohaeng': min_ohaeng,
        'day_gan_ohaeng': CHEONGAN_OHAENG[day_gan],
        'day_ji_ohaeng': JIJI_OHAENG[day_ji]
    }
