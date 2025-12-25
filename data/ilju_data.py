"""
60갑자 일주 데이터
일주(日柱)는 사주에서 가장 중요한 '나 자신'을 나타내는 기둥
"""

ILJU_DATA = {
    # 갑(甲) 일간 - 큰 나무, 우두머리, 리더십
    '갑자': {
        'name': '갑자(甲子)',
        'element': '목/수',
        'keywords': ['야망', '불안', '도전'],
        'description': '물 위에 떠있는 큰 나무. 뿌리가 불안정하여 항상 새로운 것을 찾아 나섬. 잠재력이 크나 기반이 약함.',
        'personality': '겉으론 당당하지만 속으론 불안함을 안고 있음. 끊임없이 성장하려는 의지.',
        'strength': '추진력, 성장 의지',
        'weakness': '기반 부족, 불안정'
    },
    '갑인': {
        'name': '갑인(甲寅)',
        'element': '목/목',
        'keywords': ['자존심', '당당함', '독립'],
        'description': '숲속의 제왕. 목 기운이 강하여 자존심이 세고 독립적. 남에게 지기 싫어함.',
        'personality': '당당하고 리더십이 있으나 고집이 셈. 자기 길을 간다.',
        'strength': '리더십, 추진력',
        'weakness': '고집, 타협 어려움'
    },
    '갑진': {
        'name': '갑진(甲辰)',
        'element': '목/토',
        'keywords': ['포부', '변화', '성장'],
        'description': '용틀임하는 나무. 큰 꿈을 품고 도약을 준비함. 변화의 시기에 강함.',
        'personality': '스케일이 크고 야망이 있음. 때를 기다릴 줄 앎.',
        'strength': '비전, 잠재력',
        'weakness': '조급함, 현실과 괴리'
    },
    '갑오': {
        'name': '갑오(甲午)',
        'element': '목/화',
        'keywords': ['열정', '화려함', '주목'],
        'description': '태양 아래 빛나는 나무. 외향적이고 화려함을 추구. 주목받고 싶어함.',
        'personality': '표현력이 좋고 열정적. 감정 기복이 있을 수 있음.',
        'strength': '표현력, 열정',
        'weakness': '급함, 감정 기복'
    },
    '갑신': {
        'name': '갑신(甲申)',
        'element': '목/금',
        'keywords': ['긴장', '극복', '날카로움'],
        'description': '도끼와 마주한 나무. 항상 긴장 속에 살며 역경을 이겨내는 힘이 있음.',
        'personality': '예민하고 날카로움. 위기를 기회로 바꾸는 능력.',
        'strength': '위기 대처, 결단력',
        'weakness': '긴장, 스트레스 취약'
    },
    '갑술': {
        'name': '갑술(甲戌)',
        'element': '목/토',
        'keywords': ['외로움', '원칙', '고독'],
        'description': '가을 산의 고목. 원칙을 중시하고 홀로 서는 힘이 있음.',
        'personality': '독립적이고 원칙주의적. 외로움을 감수할 줄 앎.',
        'strength': '신념, 독립심',
        'weakness': '고독, 융통성 부족'
    },

    # 을(乙) 일간 - 풀, 덩굴, 유연함
    '을축': {
        'name': '을축(乙丑)',
        'element': '목/토',
        'keywords': ['인내', '끈기', '실속'],
        'description': '겨울을 버티는 풀. 겉으론 약해 보이나 강인한 생존력 보유.',
        'personality': '실속 있고 끈기 있음. 느리지만 확실히 성취.',
        'strength': '인내심, 현실감각',
        'weakness': '느린 진행, 소극적'
    },
    '을묘': {
        'name': '을묘(乙卯)',
        'element': '목/목',
        'keywords': ['섬세함', '예민함', '감성'],
        'description': '봄의 꽃과 풀. 섬세하고 예술적 감각이 뛰어남.',
        'personality': '감수성이 풍부하고 섬세함. 평화를 추구.',
        'strength': '예술성, 섬세함',
        'weakness': '예민함, 상처 잘 받음'
    },
    '을사': {
        'name': '을사(乙巳)',
        'element': '목/화',
        'keywords': ['영리함', '처세', '변화'],
        'description': '불 속에서 피어나는 풀. 영리하고 상황 적응력이 뛰어남.',
        'personality': '눈치 빠르고 사교적. 변화에 민감.',
        'strength': '적응력, 사교성',
        'weakness': '변덕, 일관성 부족'
    },
    '을미': {
        'name': '을미(乙未)',
        'element': '목/토',
        'keywords': ['온화함', '배려', '희생'],
        'description': '정원의 화초. 온화하고 타인을 배려하는 마음이 큼.',
        'personality': '부드럽고 헌신적. 갈등을 피하려 함.',
        'strength': '배려심, 조화',
        'weakness': '우유부단, 자기희생'
    },
    '을유': {
        'name': '을유(乙酉)',
        'element': '목/금',
        'keywords': ['미적감각', '날카로움', '세련됨'],
        'description': '가위에 다듬어진 화초. 미적 감각이 뛰어나고 세련됨.',
        'personality': '까다롭고 완벽주의적. 아름다움을 추구.',
        'strength': '미적 감각, 분별력',
        'weakness': '까다로움, 비판적'
    },
    '을해': {
        'name': '을해(乙亥)',
        'element': '목/수',
        'keywords': ['지혜', '유연함', '적응'],
        'description': '물가의 풀. 지혜롭고 상황에 따라 유연하게 대처.',
        'personality': '총명하고 적응력이 좋음. 깊은 생각을 함.',
        'strength': '지혜, 유연성',
        'weakness': '우유부단, 결단력 부족'
    },

    # 병(丙) 일간 - 태양, 밝음, 열정
    '병자': {
        'name': '병자(丙子)',
        'element': '화/수',
        'keywords': ['내면갈등', '열정', '고민'],
        'description': '물 위에 비친 태양. 겉은 밝으나 속에 깊은 고민이 있음.',
        'personality': '밝아 보이지만 내면에 갈등이 있음. 감정과 이성 사이 고민.',
        'strength': '통찰력, 깊은 사고',
        'weakness': '내면 갈등, 우울'
    },
    '병인': {
        'name': '병인(丙寅)',
        'element': '화/목',
        'keywords': ['활력', '정열', '발전'],
        'description': '숲을 밝히는 태양. 에너지가 넘치고 주변을 밝게 함.',
        'personality': '활기차고 긍정적. 리더십과 열정이 넘침.',
        'strength': '열정, 리더십',
        'weakness': '성급함, 과욕'
    },
    '병진': {
        'name': '병진(丙辰)',
        'element': '화/토',
        'keywords': ['포부', '지배력', '위엄'],
        'description': '하늘의 태양과 땅의 용. 큰 뜻을 품고 세상을 움직이려 함.',
        'personality': '야망이 크고 지배력이 있음. 큰 그림을 그림.',
        'strength': '비전, 추진력',
        'weakness': '오만, 현실 무시'
    },
    '병오': {
        'name': '병오(丙午)',
        'element': '화/화',
        'keywords': ['극렬함', '순수', '정열'],
        'description': '한낮의 태양. 가장 뜨거운 열정과 순수함을 지님.',
        'personality': '정열적이고 솔직함. 감정 표현이 강렬.',
        'strength': '열정, 솔직함',
        'weakness': '급함, 과격함'
    },
    '병신': {
        'name': '병신(丙申)',
        'element': '화/금',
        'keywords': ['날카로움', '명석함', '긴장'],
        'description': '칼날 위의 햇빛. 명석하고 날카로운 판단력.',
        'personality': '머리가 좋고 분석적. 긴장감 속에 살 때가 있음.',
        'strength': '명석함, 분석력',
        'weakness': '냉정함, 긴장'
    },
    '병술': {
        'name': '병술(丙戌)',
        'element': '화/토',
        'keywords': ['따뜻함', '신뢰', '헌신'],
        'description': '저녁 노을. 따뜻하고 헌신적인 마음을 지님.',
        'personality': '의리 있고 따뜻함. 타인을 위해 헌신.',
        'strength': '신뢰성, 헌신',
        'weakness': '고집, 보수적'
    },

    # 정(丁) 일간 - 촛불, 섬세함, 따뜻함
    '정축': {
        'name': '정축(丁丑)',
        'element': '화/토',
        'keywords': ['인내', '내면의빛', '꾸준함'],
        'description': '어둠 속 촛불. 묵묵히 자기 역할을 함.',
        'personality': '조용하지만 꾸준함. 내면의 열정을 간직.',
        'strength': '인내, 성실',
        'weakness': '눈에 안 띔, 답답함'
    },
    '정묘': {
        'name': '정묘(丁卯)',
        'element': '화/목',
        'keywords': ['온화함', '배려', '감성'],
        'description': '봄날의 촛불. 따뜻하고 감성적인 성격.',
        'personality': '부드럽고 배려심이 깊음. 예술적 감각.',
        'strength': '따뜻함, 감성',
        'weakness': '소심, 의존적'
    },
    '정사': {
        'name': '정사(丁巳)',
        'element': '화/화',
        'keywords': ['영리함', '재치', '변화'],
        'description': '타오르는 촛불. 영리하고 변화무쌍함.',
        'personality': '재치 있고 눈치 빠름. 상황 파악이 빠름.',
        'strength': '영리함, 적응력',
        'weakness': '변덕, 일관성 부족'
    },
    '정미': {
        'name': '정미(丁未)',
        'element': '화/토',
        'keywords': ['섬세함', '예술성', '꿈'],
        'description': '여름밤의 촛불. 섬세하고 낭만적인 감성.',
        'personality': '예술적이고 감수성 풍부. 이상을 추구.',
        'strength': '창의성, 감성',
        'weakness': '비현실적, 예민'
    },
    '정유': {
        'name': '정유(丁酉)',
        'element': '화/금',
        'keywords': ['세련됨', '날카로움', '미적감각'],
        'description': '보석을 비추는 촛불. 세련되고 안목이 높음.',
        'personality': '까다롭고 미적 감각이 뛰어남. 완벽 추구.',
        'strength': '안목, 세련됨',
        'weakness': '까다로움, 예민'
    },
    '정해': {
        'name': '정해(丁亥)',
        'element': '화/수',
        'keywords': ['지혜', '깊이', '갈등'],
        'description': '바다 위 촛불. 깊은 지혜와 내면의 갈등.',
        'personality': '생각이 깊고 철학적. 감정과 이성 사이 고민.',
        'strength': '지혜, 통찰력',
        'weakness': '우유부단, 갈등'
    },

    # 무(戊) 일간 - 산, 묵직함, 중심
    '무자': {
        'name': '무자(戊子)',
        'element': '토/수',
        'keywords': ['고독', '깊이', '재능'],
        'description': '물가의 산. 겉은 무거우나 속에 깊은 감성과 재능.',
        'personality': '묵직하면서도 감성적. 깊은 내면을 가짐.',
        'strength': '깊이, 재능',
        'weakness': '고독, 표현 부족'
    },
    '무인': {
        'name': '무인(戊寅)',
        'element': '토/목',
        'keywords': ['포용', '성장', '넓음'],
        'description': '나무가 자라는 산. 포용력이 크고 성장을 돕는 성격.',
        'personality': '마음이 넓고 타인을 품어줌. 어른스러움.',
        'strength': '포용력, 안정감',
        'weakness': '느림, 변화 거부'
    },
    '무진': {
        'name': '무진(戊辰)',
        'element': '토/토',
        'keywords': ['중후함', '야망', '거대함'],
        'description': '큰 산. 스케일이 크고 묵직한 존재감.',
        'personality': '중후하고 야망이 큼. 신뢰감을 줌.',
        'strength': '신뢰성, 규모',
        'weakness': '느림, 고집'
    },
    '무오': {
        'name': '무오(戊午)',
        'element': '토/화',
        'keywords': ['따뜻함', '활력', '낙관'],
        'description': '햇볕 드는 산. 따뜻하고 활기찬 성격.',
        'personality': '밝고 낙관적. 주변에 온기를 줌.',
        'strength': '긍정성, 활력',
        'weakness': '게으름, 안일함'
    },
    '무신': {
        'name': '무신(戊申)',
        'element': '토/금',
        'keywords': ['영리함', '현실감각', '실속'],
        'description': '보물이 든 산. 현실 감각이 뛰어나고 영리함.',
        'personality': '실속 있고 계산적. 손해 보지 않음.',
        'strength': '현실감각, 영리함',
        'weakness': '계산적, 냉정'
    },
    '무술': {
        'name': '무술(戊戌)',
        'element': '토/토',
        'keywords': ['고집', '원칙', '신뢰'],
        'description': '가을 산. 원칙을 지키고 신뢰를 중시.',
        'personality': '고집스럽지만 신뢰할 수 있음. 한결같음.',
        'strength': '신뢰성, 원칙',
        'weakness': '고집, 융통성 없음'
    },

    # 기(己) 일간 - 논밭, 순응, 수용
    '기축': {
        'name': '기축(己丑)',
        'element': '토/토',
        'keywords': ['성실', '꼼꼼', '현실적'],
        'description': '겨울 논밭. 성실하고 꼼꼼하게 준비.',
        'personality': '착실하고 현실적. 실속을 챙김.',
        'strength': '성실함, 현실감각',
        'weakness': '소심함, 느림'
    },
    '기묘': {
        'name': '기묘(己卯)',
        'element': '토/목',
        'keywords': ['온화함', '섬세함', '감성'],
        'description': '봄의 논밭. 온화하고 섬세한 감성.',
        'personality': '부드럽고 배려심이 깊음. 조화를 추구.',
        'strength': '배려심, 섬세함',
        'weakness': '우유부단, 소극적'
    },
    '기사': {
        'name': '기사(己巳)',
        'element': '토/화',
        'keywords': ['영리함', '적응력', '재치'],
        'description': '볕 드는 논밭. 영리하고 상황 대처가 빠름.',
        'personality': '눈치 빠르고 영리함. 사교적.',
        'strength': '적응력, 영리함',
        'weakness': '변덕, 피상적'
    },
    '기미': {
        'name': '기미(己未)',
        'element': '토/토',
        'keywords': ['인내', '수용', '배려'],
        'description': '여름의 논밭. 무엇이든 받아들이는 포용력.',
        'personality': '인내심이 강하고 수용적. 갈등을 피함.',
        'strength': '포용력, 인내',
        'weakness': '피동적, 자기주장 약함'
    },
    '기유': {
        'name': '기유(己酉)',
        'element': '토/금',
        'keywords': ['세련됨', '현실감각', '분별력'],
        'description': '추수하는 논밭. 현실 감각이 뛰어나고 분별력 있음.',
        'personality': '실속 있고 세련됨. 헛된 것을 싫어함.',
        'strength': '현실감각, 분별력',
        'weakness': '계산적, 냉정'
    },
    '기해': {
        'name': '기해(己亥)',
        'element': '토/수',
        'keywords': ['지혜', '유연함', '깊이'],
        'description': '물가의 논밭. 깊은 지혜와 유연한 사고.',
        'personality': '생각이 깊고 유연함. 적응력이 좋음.',
        'strength': '지혜, 유연성',
        'weakness': '우유부단, 결단력 부족'
    },

    # 경(庚) 일간 - 바위/금속, 강함, 결단
    '경자': {
        'name': '경자(庚子)',
        'element': '금/수',
        'keywords': ['날카로움', '영리함', '차가움'],
        'description': '물속의 보검. 날카롭고 영리하지만 차가움.',
        'personality': '머리가 좋고 냉철함. 감정 표현이 서툼.',
        'strength': '영리함, 분석력',
        'weakness': '냉정함, 고독'
    },
    '경인': {
        'name': '경인(庚寅)',
        'element': '금/목',
        'keywords': ['긴장', '도전', '극복'],
        'description': '나무를 베는 도끼. 항상 긴장 속에서 도전.',
        'personality': '도전적이고 과감함. 역경을 돌파하는 힘.',
        'strength': '돌파력, 결단',
        'weakness': '갈등, 충돌'
    },
    '경진': {
        'name': '경진(庚辰)',
        'element': '금/토',
        'keywords': ['위엄', '야망', '지배력'],
        'description': '구름 위의 보검. 위엄 있고 야망이 큼.',
        'personality': '당당하고 리더십이 있음. 지배욕이 강함.',
        'strength': '리더십, 카리스마',
        'weakness': '독단적, 거만'
    },
    '경오': {
        'name': '경오(庚午)',
        'element': '금/화',
        'keywords': ['열정', '갈등', '격렬함'],
        'description': '불에 달궈지는 쇠. 열정과 갈등이 공존.',
        'personality': '열정적이지만 내면 갈등이 있음. 극단적일 때가 있음.',
        'strength': '열정, 행동력',
        'weakness': '급함, 갈등'
    },
    '경신': {
        'name': '경신(庚申)',
        'element': '금/금',
        'keywords': ['강함', '결단', '냉철'],
        'description': '단단한 바위. 강하고 결단력이 있음.',
        'personality': '단호하고 냉철함. 타협을 모름.',
        'strength': '결단력, 강인함',
        'weakness': '냉정함, 융통성 없음'
    },
    '경술': {
        'name': '경술(庚戌)',
        'element': '금/토',
        'keywords': ['의리', '원칙', '고집'],
        'description': '가을 산의 바위. 의리 있고 원칙을 지킴.',
        'personality': '한번 정하면 끝까지 감. 신뢰할 수 있음.',
        'strength': '의리, 신뢰성',
        'weakness': '고집, 변화 거부'
    },

    # 신(辛) 일간 - 보석, 세련됨, 예민함
    '신축': {
        'name': '신축(辛丑)',
        'element': '금/토',
        'keywords': ['숨겨진빛', '인내', '실속'],
        'description': '흙 속의 보석. 드러나지 않지만 가치가 있음.',
        'personality': '겉으론 평범해 보이나 내면에 빛이 있음. 실속적.',
        'strength': '잠재력, 인내',
        'weakness': '눈에 안 띔, 소극적'
    },
    '신묘': {
        'name': '신묘(辛卯)',
        'element': '금/목',
        'keywords': ['섬세함', '갈등', '예민'],
        'description': '꽃에 비친 보석. 섬세하지만 내면 갈등이 있음.',
        'personality': '예민하고 섬세함. 외유내강.',
        'strength': '섬세함, 미적감각',
        'weakness': '예민함, 상처 잘 받음'
    },
    '신사': {
        'name': '신사(辛巳)',
        'element': '금/화',
        'keywords': ['빛남', '화려함', '긴장'],
        'description': '불에 비친 보석. 화려하게 빛나지만 긴장감.',
        'personality': '주목받기를 좋아하고 화려함. 민감.',
        'strength': '매력, 표현력',
        'weakness': '긴장, 피로'
    },
    '신미': {
        'name': '신미(辛未)',
        'element': '금/토',
        'keywords': ['세련됨', '품격', '고고함'],
        'description': '정원의 보석. 세련되고 품격이 있음.',
        'personality': '고상하고 품위 있음. 속물적인 것을 싫어함.',
        'strength': '품격, 세련됨',
        'weakness': '까다로움, 고고함'
    },
    '신유': {
        'name': '신유(辛酉)',
        'element': '금/금',
        'keywords': ['완벽', '날카로움', '미'],
        'description': '다듬어진 보석. 완벽을 추구하고 날카로움.',
        'personality': '완벽주의적이고 까다로움. 미적 감각 뛰어남.',
        'strength': '완벽성, 미적감각',
        'weakness': '예민함, 비판적'
    },
    '신해': {
        'name': '신해(辛亥)',
        'element': '금/수',
        'keywords': ['지혜', '세련됨', '깊이'],
        'description': '바다의 진주. 깊은 지혜와 세련됨을 겸비.',
        'personality': '총명하고 세련됨. 깊은 생각을 함.',
        'strength': '지혜, 우아함',
        'weakness': '고독, 속마음 안 보임'
    },

    # 임(壬) 일간 - 바다/강, 자유로움, 지혜
    '임자': {
        'name': '임자(壬子)',
        'element': '수/수',
        'keywords': ['깊이', '지혜', '자유'],
        'description': '깊은 바다. 무한한 깊이와 지혜를 지님.',
        'personality': '생각이 깊고 자유로움. 흐르는 물처럼 유연.',
        'strength': '지혜, 유연성',
        'weakness': '방향성 없음, 산만'
    },
    '임인': {
        'name': '임인(壬寅)',
        'element': '수/목',
        'keywords': ['창의력', '성장', '흐름'],
        'description': '숲을 적시는 강물. 창의적이고 성장을 돕는 힘.',
        'personality': '창의적이고 포용력이 있음. 새로운 것을 만듦.',
        'strength': '창의력, 포용력',
        'weakness': '방향성 없음, 우유부단'
    },
    '임진': {
        'name': '임진(壬辰)',
        'element': '수/토',
        'keywords': ['잠재력', '변화', '도약'],
        'description': '구름 속 용. 엄청난 잠재력과 변화의 힘.',
        'personality': '스케일이 크고 변화무쌍함. 대기만성형.',
        'strength': '잠재력, 변화력',
        'weakness': '불안정, 예측 불가'
    },
    '임오': {
        'name': '임오(壬午)',
        'element': '수/화',
        'keywords': ['갈등', '열정', '복잡'],
        'description': '태양 아래 바다. 열정과 냉철함이 공존.',
        'personality': '감정과 이성 사이에서 갈등. 복잡한 내면.',
        'strength': '균형감, 다양성',
        'weakness': '갈등, 에너지 소모'
    },
    '임신': {
        'name': '임신(壬申)',
        'element': '수/금',
        'keywords': ['영리함', '날카로움', '냉철'],
        'description': '칼을 씻는 물. 영리하고 냉철한 판단력.',
        'personality': '머리가 좋고 분석적. 손해 보지 않음.',
        'strength': '영리함, 분석력',
        'weakness': '계산적, 냉정'
    },
    '임술': {
        'name': '임술(壬戌)',
        'element': '수/토',
        'keywords': ['포용', '신뢰', '안정'],
        'description': '제방 안의 물. 안정을 추구하고 신뢰를 줌.',
        'personality': '안정적이고 신뢰할 수 있음. 책임감.',
        'strength': '신뢰성, 안정',
        'weakness': '보수적, 모험 회피'
    },

    # 계(癸) 일간 - 비/이슬, 섬세함, 적응
    '계축': {
        'name': '계축(癸丑)',
        'element': '수/토',
        'keywords': ['인내', '숨은실력', '준비'],
        'description': '겨울의 이슬. 묵묵히 준비하는 숨은 실력자.',
        'personality': '드러내지 않지만 실력이 있음. 인내심 강함.',
        'strength': '인내, 실력',
        'weakness': '눈에 안 띔, 느림'
    },
    '계묘': {
        'name': '계묘(癸卯)',
        'element': '수/목',
        'keywords': ['감성', '섬세함', '성장'],
        'description': '봄비. 섬세하고 감성적이며 성장을 돕는 힘.',
        'personality': '감수성이 풍부하고 배려심이 깊음.',
        'strength': '감성, 배려심',
        'weakness': '예민함, 약해보임'
    },
    '계사': {
        'name': '계사(癸巳)',
        'element': '수/화',
        'keywords': ['영리함', '변화', '긴장'],
        'description': '증발하는 물. 영리하고 변화에 민감.',
        'personality': '눈치 빠르고 적응력이 좋음. 긴장감 있음.',
        'strength': '영리함, 적응력',
        'weakness': '불안정, 긴장'
    },
    '계미': {
        'name': '계미(癸未)',
        'element': '수/토',
        'keywords': ['섬세함', '배려', '감성'],
        'description': '여름비. 섬세하고 감성적. 타인을 살핌.',
        'personality': '부드럽고 배려심이 깊음. 감정이 풍부.',
        'strength': '배려심, 감성',
        'weakness': '우유부단, 의존적'
    },
    '계유': {
        'name': '계유(癸酉)',
        'element': '수/금',
        'keywords': ['세련됨', '영리함', '냉철'],
        'description': '맑은 이슬. 세련되고 영리하며 분별력 있음.',
        'personality': '머리가 좋고 세련됨. 냉철한 판단.',
        'strength': '영리함, 세련됨',
        'weakness': '냉정함, 까다로움'
    },
    '계해': {
        'name': '계해(癸亥)',
        'element': '수/수',
        'keywords': ['자유', '깊이', '흐름'],
        'description': '바다로 가는 물. 자유롭고 깊은 내면.',
        'personality': '자유로운 영혼. 깊은 생각과 직관.',
        'strength': '자유로움, 직관력',
        'weakness': '방향성 없음, 산만'
    }
}


def get_ilju_info(ilju):
    """일주 정보 반환"""
    return ILJU_DATA.get(ilju, None)
