import json
from SearchBook import book_lib, book_name
from math import cos, sin, radians, acos
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

lib_loc = {'241286552': [
    {'address': '서울특별시 강동구 고덕동길 295 (고덕2동 296)', 'closeDay': '2,4주 월요일 및 법정공휴일', 'gunguName': '강동구', 'holidayTime': '',
     'latitude': '37.55930391', 'lbiType': '공공도서관', 'libName': '고덕평생학습관', 'longitude': '127.1579066',
     'phNum': '02-6902-2600', 'satTime': '09:00~17:00', 'sidoName': '서울특별시', 'tkDay': '', 'tkNum': '',
     'url': 'http://gdllc.sen.go.kr', 'weekdayTime': '09:00~20:00'},
    {'address': '서울특별시 송파구 석촌호수로 155 (잠실동)', 'closeDay': '매주월요일+국가지정공휴일', 'gunguName': '송파구',
     'holidayTime': '09:00-22:00', 'latitude': '37.5072666662', 'lbiType': '공공도서관', 'libName': '소나무언덕2호',
     'longitude': '127.0942172981', 'phNum': '02-424-0083', 'satTime': '09:00-22:00', 'sidoName': '서울특별시',
     'tkDay': '14', 'tkNum': '5', 'url': 'http://www.splib.or.kr', 'weekdayTime': '09:00-22:00'},
    {'address': '서울특별시 중랑구 면목로 397 (면목동)', 'closeDay': '매월 첫째, 셋째 월요일,법정공휴일(일요일제외) 및 근로자의날(5월1일), 임시휴관일',
     'gunguName': '중랑구', 'holidayTime': '00:00-00:00', 'latitude': '37.5873561521', 'lbiType': '공공도서관',
     'libName': '중랑구립면목정보도서관', 'longitude': '127.0875565596', 'phNum': '02-432-4120', 'satTime': '08:00-22:00',
     'sidoName': '서울특별시', 'tkDay': '14', 'tkNum': '5', 'url': 'http://www.jungnanglib.seoul.kr/mmlib',
     'weekdayTime': '08:00-23:00'},
    {'address': '서울특별시 은평구 가좌로 7길 15', 'closeDay': '금요일,법정공휴일', 'gunguName': '은평구', 'holidayTime': '09:00-18:00',
     'latitude': '37.5859665629', 'lbiType': '공공도서관', 'libName': '응암정보도서관', 'longitude': '126.9196820594',
     'phNum': '02-308-2320', 'satTime': '09:00-18:00', 'sidoName': '서울특별시', 'tkDay': '14', 'tkNum': '5',
     'url': 'http://www.ealib.or.kr/', 'weekdayTime': '09:00-22:00'},
    {'address': '서울특별시 관악구 쑥고개로 44', 'closeDay': '매주 토/일요일/국가지정공휴일', 'gunguName': '관악구', 'holidayTime': '00:00-00:00',
     'latitude': '37.479107', 'lbiType': '작은도서관', 'libName': '청룡동 숯고을작은도서관', 'longitude': '126.941694',
     'phNum': '02-876-4083', 'satTime': '00:00-00:00', 'sidoName': '서울특별시', 'tkDay': '14', 'tkNum': '5',
     'url': 'http://lib.gwanak.go.kr/', 'weekdayTime': '10:00-18:00'},
    {'address': '서울특별시 관악구 난곡로 249', 'closeDay': '매주 토/일요일/국가지정공휴일', 'gunguName': '관악구', 'holidayTime': '00:00-00:00',
     'latitude': '37.476132', 'lbiType': '작은도서관', 'libName': '미성동 책의향기작은도서관', 'longitude': '126.915527',
     'phNum': '02-830-5312', 'satTime': '00:00-00:00', 'sidoName': '서울특별시', 'tkDay': '14', 'tkNum': '5',
     'url': 'http://lib.gwanak.go.kr/', 'weekdayTime': '10:00-18:00'},
    {'address': '부산광역시 중구 대청로 61-2', 'closeDay': '월요일', 'gunguName': '부산중구', 'holidayTime': '10:00-18:00',
     'latitude': '35.10321832', 'lbiType': '작은도서관', 'libName': '��다작은도서관', 'longitude': '129.026751',
     'phNum': '051-743-7650', 'satTime': '10:00-18:00', 'sidoName': '부산광역시', 'tkDay': '15', 'tkNum': '3',
     'url': 'https://cafe.naver.com/bosubook', 'weekdayTime': '10:00-18:00'},
    {'address': '부산광역시 연제구 황령산로 612(연산동)', 'closeDay': '매주월요일, 국가지정공휴일', 'gunguName': '연제구',
     'holidayTime': '00:00-00:00', 'latitude': '35.17414442', 'lbiType': '공공도서관', 'libName': '연제도서관',
     'longitude': '129.0829683', 'phNum': '051-665-5511', 'satTime': '09:00-18:00', 'sidoName': '부산광역시', 'tkDay': '14',
     'tkNum': '5', 'url': 'http://www.yeonje.go.kr/library/main.do', 'weekdayTime': '09:00-22:00'},
    {'address': '부산광역시 연제구 금련로 24번길33(연산동)', 'closeDay': '매주월요일, 국가지정공휴일', 'gunguName': '연제구',
     'holidayTime': '00:00-00:00', 'latitude': '35.1720557', 'lbiType': '작은도서관', 'libName': '밤골작은도서관',
     'longitude': '129.0944725', 'phNum': '051-665-4513', 'satTime': '10:00-18:00', 'sidoName': '부산광역시', 'tkDay': '14',
     'tkNum': '5', 'url': '', 'weekdayTime': '10:00-19:00'},
    {'address': '부산광역시 연제구 배산북로8(연산동)', 'closeDay': '매주월요일, 국가지정공휴일', 'gunguName': '연제구', 'holidayTime': '00:00-00:00',
     'latitude': '35.17509425', 'lbiType': '작은도서관', 'libName': '배산작은도서관', 'longitude': '129.0933137',
     'phNum': '051-665-4508', 'satTime': '10:00-18:00', 'sidoName': '부산광역시', 'tkDay': '14', 'tkNum': '5', 'url': '',
     'weekdayTime': '10:00-19:00'},
    {'address': '경상남도 양산시 물금읍 청룡로 11', 'closeDay': '법정공휴일(일요일 제외)', 'gunguName': '양산시', 'holidayTime': '00:00-00:00',
     'latitude': '35.325181', 'lbiType': '공공도서관', 'libName': '양산시립도서관', 'longitude': '128.996715',
     'phNum': '055-392-5900', 'satTime': '09:00-22:00', 'sidoName': '경상남도', 'tkDay': '21', 'tkNum': '5',
     'url': 'http://lib.yangsan.go.kr', 'weekdayTime': '09:00-22:00'}], '367603703': [
    {'address': '서울특별시 강남구 선릉로4길 30', 'closeDay': '2,4주 목요일 및 법정공휴일', 'gunguName': '강남구', 'holidayTime': '',
     'latitude': '37.48308019', 'lbiType': '공공도서관', 'libName': '개포도서관', 'longitude': '127.063867',
     'phNum': '02-3460-8200', 'satTime': '09:00~17:00', 'sidoName': '서울특별시', 'tkDay': '', 'tkNum': '',
     'url': 'http://gplib.sen.go.kr', 'weekdayTime': '09:00~20:00'},
    {'address': '서울특별시 강동구 고덕동길 295 (고덕2동 296)', 'closeDay': '2,4주 월요일 및 법정공휴일', 'gunguName': '강동구', 'holidayTime': '',
     'latitude': '37.55930391', 'lbiType': '공공도서관', 'libName': '고덕평생학습관', 'longitude': '127.1579066',
     'phNum': '02-6902-2600', 'satTime': '09:00~17:00', 'sidoName': '서울특별시', 'tkDay': '', 'tkNum': '',
     'url': 'http://gdllc.sen.go.kr', 'weekdayTime': '09:00~20:00'},
    {'address': '서울특별시 구로구 공원로 15', 'closeDay': '1,3주 수요일 및 법정공휴일', 'gunguName': '구로구', 'holidayTime': '',
     'latitude': '37.49867236', 'lbiType': '공공도서관', 'libName': '구로도서관', 'longitude': '126.8911162',
     'phNum': '02-6958-2800', 'satTime': '09:00~17:00', 'sidoName': '서울특별시', 'tkDay': '', 'tkNum': '',
     'url': 'http://grlib.sen.go.kr', 'weekdayTime': '09:00~20:00'},
    {'address': '서울특별시 관악구 신림로3길 35(신림동)', 'closeDay': '매주 화요일/국가지정공휴일', 'gunguName': '관악구',
     'holidayTime': '00:00-00:00', 'latitude': '37.467135', 'lbiType': '공공도서관', 'libName': '관악문화관도서관',
     'longitude': '126.944735', 'phNum': '02-828-5700', 'satTime': '09:00-17:00', 'sidoName': '서울특별시', 'tkDay': '14',
     'tkNum': '5', 'url': 'http://lib.gwanak.go.kr/', 'weekdayTime': '07:00-23:00'},
    {'address': '서울특별시 중랑구 면목로 397 (면목동)', 'closeDay': '매월 첫째, 셋째 월요일,법정공휴일(일요일제외) 및 근로자의날(5월1일), 임시휴관일',
     'gunguName': '중랑구', 'holidayTime': '00:00-00:00', 'latitude': '37.5873561521', 'lbiType': '공공도서관',
     'libName': '중랑구립면목정보도서관', 'longitude': '127.0875565596', 'phNum': '02-432-4120', 'satTime': '08:00-22:00',
     'sidoName': '서울특별시', 'tkDay': '14', 'tkNum': '5', 'url': 'http://www.jungnanglib.seoul.kr/mmlib',
     'weekdayTime': '08:00-23:00'},
    {'address': '서울특별시 용산구 청파로93길 27', 'closeDay': '월,법정공휴일', 'gunguName': '용산구', 'holidayTime': '09:00-17:00',
     'latitude': '37.5539248195', 'lbiType': '공공도서관', 'libName': '구립 청파도서관', 'longitude': '126.9676059172',
     'phNum': '02-714-3931', 'satTime': '09:00-17:00', 'sidoName': '서울특별시', 'tkDay': '14', 'tkNum': '3',
     'url': 'https://www.yslibrary.or.kr/cheongpa/index.do', 'weekdayTime': '09:00-21:00'},
    {'address': '서울특별시 은평구 불광천길 370 (불광천 휴게데크 위)', 'closeDay': '금요일 법정공휴일', 'gunguName': '은평구',
     'holidayTime': '09:00-18:00', 'latitude': '37.5904858592', 'lbiType': '작은도서관', 'libName': '불광천 작은도서관 (응암정보도서관 운영)',
     'longitude': '126.9144370871', 'phNum': '02-308-3117', 'satTime': '09:00-18:00', 'sidoName': '서울특별시',
     'tkDay': '14', 'tkNum': '3', 'url': '', 'weekdayTime': '09:00-18:00'},
    {'address': '서울특별시 관악구 쑥고개로 44', 'closeDay': '매주 토/일요일/국가지정공휴일', 'gunguName': '관악구', 'holidayTime': '00:00-00:00',
     'latitude': '37.479107', 'lbiType': '작은도서관', 'libName': '청룡동 숯고을작은도서관', 'longitude': '126.941694',
     'phNum': '02-876-4083', 'satTime': '00:00-00:00', 'sidoName': '서울특별시', 'tkDay': '14', 'tkNum': '5',
     'url': 'http://lib.gwanak.go.kr/', 'weekdayTime': '10:00-18:00'},
    {'address': '서울특별시 관악구 호암로 589', 'closeDay': '매주 토/일요일/국가지정공휴일', 'gunguName': '관악구', 'holidayTime': '00:00-00:00',
     'latitude': '37.470073', 'lbiType': '작은도서관', 'libName': '삼성동 샛별작은도서관', 'longitude': '126.932964',
     'phNum': '02-876-2063', 'satTime': '00:00-00:00', 'sidoName': '서울특별시', 'tkDay': '14', 'tkNum': '5',
     'url': 'http://lib.gwanak.go.kr/', 'weekdayTime': '10:00-18:00'},
    {'address': '서울특별시 중랑구 동일로114길 10 (상봉동)', 'closeDay': '매주월요일, 법정공휴일(일요일제외) 및 근로자의날(5월1일), 임시휴관일',
     'gunguName': '중랑구', 'holidayTime': '00:00-00:00', 'latitude': '37.5931272353', 'lbiType': '공공도서관',
     'libName': '중랑상봉도서관', 'longitude': '127.080932', 'phNum': '', 'satTime': '09:00-17:00', 'sidoName': '서울특별시',
     'tkDay': '14', 'tkNum': '5', 'url': 'http://www.jungnanglib.seoul.kr/sblib/', 'weekdayTime': '09:00-20:00'},
    {'address': '대전광역시 동구 새울로 68번길 23-23 (용운동)', 'closeDay': '월요일, 관공서의 공휴일', 'gunguName': '동구',
     'holidayTime': '00:00-00:00', 'latitude': '36.3257031179', 'lbiType': '공공도서관', 'libName': '용운도서관',
     'longitude': '127.4638509481', 'phNum': '042-259-7021', 'satTime': '09:00-22:00', 'sidoName': '대전광역시',
     'tkDay': '14', 'tkNum': '5', 'url': 'https://www.donggu.go.kr/dg/lib/contents/640', 'weekdayTime': '09:00-22:00'},
    {'address': '대전광역시 동구 성남로 38-5 (성남동)', 'closeDay': '월요일, 관공서의 공휴일', 'gunguName': '동구', 'holidayTime': '00:00-00:00',
     'latitude': '36.3423217291', 'lbiType': '공공도서관', 'libName': '성남도서관', 'longitude': '127.4298546861',
     'phNum': '042-259-7091', 'satTime': '09:00-18:00', 'sidoName': '대전광역시', 'tkDay': '14', 'tkNum': '5',
     'url': 'https://www.donggu.go.kr/dg/lib/contents/636', 'weekdayTime': '09:00-18:00'},
    {'address': '경기도 양평군 양평읍 양근로 240-9', 'closeDay': '신정,설,추석연휴', 'gunguName': '양평군', 'holidayTime': '08:00-00:00',
     'latitude': '37.4859108923', 'lbiType': '공공도서관', 'libName': '중앙도서관', 'longitude': '127.494309',
     'phNum': '031-770-2711', 'satTime': '08:00-00:00', 'sidoName': '경기도', 'tkDay': '14', 'tkNum': '7',
     'url': 'http://www.yplib.go.kr', 'weekdayTime': '08:00-00:00'},
    {'address': '경기도 안산시 상록구충장로 528(성포동)', 'closeDay': '매주월요일,국가지정공휴일', 'gunguName': '안산시',
     'holidayTime': '00:00-00:00', 'latitude': '37.3251413', 'lbiType': '공공도서관', 'libName': '성포도서관',
     'longitude': '126.8503677', 'phNum': '031-481-2755', 'satTime': '07:00-23:00', 'sidoName': '경기도', 'tkDay': '14',
     'tkNum': '10', 'url': 'http://lib.iansan.net', 'weekdayTime': '07:00-23:00'},
    {'address': '경기도 남양주시 별내면 청학로 86-1', 'closeDay': '매월 둘째·넷째 금요일, 1월 1일, 설날·추석 연휴(대체공휴일 포함)', 'gunguName': '남양주시',
     'holidayTime': '08:00-22:00', 'latitude': '37.7083499', 'lbiType': '공공도서관', 'libName': '별내도서관',
     'longitude': '127.1178283', 'phNum': '031-590-8808', 'satTime': '08:00-22:00', 'sidoName': '경기도', 'tkDay': '14',
     'tkNum': '20', 'url': 'http://lib.nyj.go.kr/bnae', 'weekdayTime': '08:00-22:00'},
    {'address': '서울특별시 중랑구 동일로114길 10 (상봉동)', 'closeDay': '매주월요일, 법정공휴일(일요일제외) 및 근로자의날(5월1일), 임시휴관일',
     'gunguName': '중랑구', 'holidayTime': '00:00-00:00', 'latitude': '37.5931272353', 'lbiType': '공공도서관',
     'libName': '중랑상봉도서관', 'longitude': '127.080932', 'phNum': '', 'satTime': '09:00-17:00', 'sidoName': '서울특별시',
     'tkDay': '14', 'tkNum': '5', 'url': 'http://www.jungnanglib.seoul.kr/sblib/', 'weekdayTime': '09:00-20:00'},
    {'address': '서울특별시 중랑구 동일로114길 10 (상봉동)', 'closeDay': '매주월요일, 법정공휴일(일요일제외) 및 근로자의날(5월1일), 임시휴관일',
     'gunguName': '중랑구', 'holidayTime': '00:00-00:00', 'latitude': '37.5931272353', 'lbiType': '공공도서관',
     'libName': '중랑상봉도서관', 'longitude': '127.080932', 'phNum': '', 'satTime': '09:00-17:00', 'sidoName': '서울특별시',
     'tkDay': '14', 'tkNum': '5', 'url': 'http://www.jungnanglib.seoul.kr/sblib/', 'weekdayTime': '09:00-20:00'},
    {'address': '서울특별시 중랑구 동일로114길 10 (상봉동)', 'closeDay': '매주월요일, 법정공휴일(일요일제외) 및 근로자의날(5월1일), 임시휴관일',
     'gunguName': '중랑구', 'holidayTime': '00:00-00:00', 'latitude': '37.5931272353', 'lbiType': '공공도서관',
     'libName': '중랑상봉도서관', 'longitude': '127.080932', 'phNum': '', 'satTime': '09:00-17:00', 'sidoName': '서울특별시',
     'tkDay': '14', 'tkNum': '5', 'url': 'http://www.jungnanglib.seoul.kr/sblib/', 'weekdayTime': '09:00-20:00'},
    {'address': '충청북도 음성군 음성읍 시장로 126길 29', 'closeDay': '매주월요일  국가지정공휴일', 'gunguName': '음성군',
     'holidayTime': '08:00-22:00', 'latitude': '36.9396201', 'lbiType': '공공도서관', 'libName': '음성도서관',
     'longitude': '127.6935851', 'phNum': '043-873-2977', 'satTime': '08:00-22:00', 'sidoName': '충청북도', 'tkDay': '14',
     'tkNum': '5', 'url': 'http://www.uslib.go.kr', 'weekdayTime': '08:00-22:00'},
    {'address': '충청북도 괴산군 괴산읍 읍내로 12길 38', 'closeDay': '매월 첫째, 셋째 월요일 및 일요일을 제외한 관공서의 공휴일', 'gunguName': '괴산군 괴산읍',
     'holidayTime': '00:00-00:00', 'latitude': '36.8108870373', 'lbiType': '공공도서관', 'libName': '괴산교육도서관',
     'longitude': '127.7921917366', 'phNum': '043-833-0319', 'satTime': '08:00-21:00', 'sidoName': '충청북도',
     'tkDay': '21', 'tkNum': '5', 'url': 'www.gselib.go.kr', 'weekdayTime': '08:00-21:00'},
    {'address': '충청남도 천안시 서북구 성거읍 천흥3길 3', 'closeDay': '매월 둘째/넷째 월요일, 국가지정공휴일', 'gunguName': '천안시',
     'holidayTime': '08:00-22:00', 'latitude': '36.87162843', 'lbiType': '공공도서관', 'libName': '성거도서관',
     'longitude': '127.2010113', 'phNum': '041-521-3734', 'satTime': '08:00-22:00', 'sidoName': '충청남도', 'tkDay': '14',
     'tkNum': '10', 'url': 'http://www.cheonan.go.kr/lib.do', 'weekdayTime': '08:00-22:00'},
    {'address': '경상남도 양산시 물금읍 청룡로 11', 'closeDay': '법정공휴일(일요일 제외)', 'gunguName': '양산시', 'holidayTime': '00:00-00:00',
     'latitude': '35.325181', 'lbiType': '공공도서관', 'libName': '양산시립도서관', 'longitude': '128.996715',
     'phNum': '055-392-5900', 'satTime': '09:00-22:00', 'sidoName': '경상남도', 'tkDay': '21', 'tkNum': '5',
     'url': 'http://lib.yangsan.go.kr', 'weekdayTime': '09:00-22:00'},
    {'address': '서울특별시 중랑구 동일로114길 10 (상봉동)', 'closeDay': '매주월요일, 법정공휴일(일요일제외) 및 근로자의날(5월1일), 임시휴관일',
     'gunguName': '중랑구', 'holidayTime': '00:00-00:00', 'latitude': '37.5931272353', 'lbiType': '공공도서관',
     'libName': '중랑상봉도서관', 'longitude': '127.080932', 'phNum': '', 'satTime': '09:00-17:00', 'sidoName': '서울특별시',
     'tkDay': '14', 'tkNum': '5', 'url': 'http://www.jungnanglib.seoul.kr/sblib/', 'weekdayTime': '09:00-20:00'}],
           '202725529': [
               {'address': '부산광역시 중구 동영로 87-1', 'closeDay': '월요일', 'gunguName': '부산중구', 'holidayTime': '10:00-20:00',
                'latitude': '35.1127605', 'lbiType': '작은도서관', 'libName': '고맙습니다.글마루작은도서관', 'longitude': '129.0316475',
                'phNum': '051-469-8451', 'satTime': '10:00-20:00', 'sidoName': '부산광역시', 'tkDay': '15', 'tkNum': '5',
                'url': 'http://blog.naver.com/thanks_gmr', 'weekdayTime': '10:00-20:00'},
               {'address': '부산광역시 연제구 아시아드대로22번길15(거제동)', 'closeDay': '매주일요일, 국가지정공휴일', 'gunguName': '연제구',
                'holidayTime': '00:00-00:00', 'latitude': '35.18764403', 'lbiType': '작은도서관',
                'libName': '거제2동새마을문고작은도서관', 'longitude': '129.0701317', 'phNum': '051-665-4511',
                'satTime': '10:00-14:00', 'sidoName': '부산광역시', 'tkDay': '14', 'tkNum': '5', 'url': '',
                'weekdayTime': '10:00-19:00'}], '185828019': [
        {'address': '서울특별시 영등포구 버드나루로15길 10', 'closeDay': '2,4주 월요일 및 법정공휴일', 'gunguName': '영등포구', 'holidayTime': '',
         'latitude': '37.52580934', 'lbiType': '공공도서관', 'libName': '영등포평생학습관', 'longitude': '126.9071819',
         'phNum': '02-6712-7500', 'satTime': '09:00~17:00', 'sidoName': '서울특별시', 'tkDay': '', 'tkNum': '',
         'url': 'http://ydpllc.sen.go.kr', 'weekdayTime': '09:00~20:00'},
        {'address': '서울특별시 구로구 공원로 15', 'closeDay': '1,3주 수요일 및 법정공휴일', 'gunguName': '구로구', 'holidayTime': '',
         'latitude': '37.49867236', 'lbiType': '공공도서관', 'libName': '구로도서관', 'longitude': '126.8911162',
         'phNum': '02-6958-2800', 'satTime': '09:00~17:00', 'sidoName': '서울특별시', 'tkDay': '', 'tkNum': '',
         'url': 'http://grlib.sen.go.kr', 'weekdayTime': '09:00~20:00'},
        {'address': '울산광역시 북구 아진1로 47(천곡동)', 'closeDay': '매주월요일, 법정공휴일', 'gunguName': '북구',
         'holidayTime': '09:00-18:00', 'latitude': '35.6330929', 'lbiType': '공공도서관', 'libName': '농소3동도서관',
         'longitude': '129.3355864', 'phNum': '052-241-7440', 'satTime': '09:00-18:00', 'sidoName': '울산광역시',
         'tkDay': '14', 'tkNum': '20', 'url': 'https://www.usbl.or.kr', 'weekdayTime': '09:00-22:00'},
        {'address': '경기도 양평군 양평읍 양근로 240-9', 'closeDay': '신정,설,추석연휴', 'gunguName': '양평군', 'holidayTime': '08:00-00:00',
         'latitude': '37.4859108923', 'lbiType': '공공도서관', 'libName': '중앙도서관', 'longitude': '127.494309',
         'phNum': '031-770-2711', 'satTime': '08:00-00:00', 'sidoName': '경기도', 'tkDay': '14', 'tkNum': '7',
         'url': 'http://www.yplib.go.kr', 'weekdayTime': '08:00-00:00'}], '186665407': [
        {'address': '서울특별시 은평구 가좌로 7길 15', 'closeDay': '금요일,법정공휴일', 'gunguName': '은평구', 'holidayTime': '09:00-18:00',
         'latitude': '37.5859665629', 'lbiType': '공공도서관', 'libName': '응암정보도서관', 'longitude': '126.9196820594',
         'phNum': '02-308-2320', 'satTime': '09:00-18:00', 'sidoName': '서울특별시', 'tkDay': '14', 'tkNum': '5',
         'url': 'http://www.ealib.or.kr/', 'weekdayTime': '09:00-22:00'}], '226552122': [
        {'address': '울산광역시 동구 대송로 140(화정주민센터 1층)', 'closeDay': '월요일', 'gunguName': '동구', 'holidayTime': '10:00-18:00',
         'latitude': '35.4958671115', 'lbiType': '작은도서관', 'libName': '화정작은도서관', 'longitude': '129.4225845949',
         'phNum': '052-209-3950', 'satTime': '10:00-18:00', 'sidoName': '울산광역시', 'tkDay': '14', 'tkNum': '5',
         'url': 'http//library.donggu.ulsan.kr', 'weekdayTime': '10:00-18:00'}], '367739162': [
        {'address': '서울특별시 강동구 고덕동길 295 (고덕2동 296)', 'closeDay': '2,4주 월요일 및 법정공휴일', 'gunguName': '강동구',
         'holidayTime': '', 'latitude': '37.55930391', 'lbiType': '공공도서관', 'libName': '고덕평생학습관',
         'longitude': '127.1579066', 'phNum': '02-6902-2600', 'satTime': '09:00~17:00', 'sidoName': '서울특별시',
         'tkDay': '', 'tkNum': '', 'url': 'http://gdllc.sen.go.kr', 'weekdayTime': '09:00~20:00'},
        {'address': '서울특별시 구로구 공원로 15', 'closeDay': '1,3주 수요일 및 법정공휴일', 'gunguName': '구로구', 'holidayTime': '',
         'latitude': '37.49867236', 'lbiType': '공공도서관', 'libName': '구로도서관', 'longitude': '126.8911162',
         'phNum': '02-6958-2800', 'satTime': '09:00~17:00', 'sidoName': '서울특별시', 'tkDay': '', 'tkNum': '',
         'url': 'http://grlib.sen.go.kr', 'weekdayTime': '09:00~20:00'},
        {'address': '서울특별시 양천구 목동서로 113', 'closeDay': '1,3주 목요일 및 법정공휴일', 'gunguName': '양천구', 'holidayTime': '',
         'latitude': '37.53349939', 'lbiType': '공공도서관', 'libName': '양천도서관', 'longitude': '126.8757691',
         'phNum': '02-2062-3900', 'satTime': '09:00~17:00', 'sidoName': '서울특별시', 'tkDay': '', 'tkNum': '',
         'url': 'http://yclib.sen.go.kr', 'weekdayTime': '09:00~20:00'},
        {'address': '서울특별시 영등포구 버드나루로15길 10', 'closeDay': '2,4주 월요일 및 법정공휴일', 'gunguName': '영등포구', 'holidayTime': '',
         'latitude': '37.52580934', 'lbiType': '공공도서관', 'libName': '영등포평생학습관', 'longitude': '126.9071819',
         'phNum': '02-6712-7500', 'satTime': '09:00~17:00', 'sidoName': '서울특별시', 'tkDay': '', 'tkNum': '',
         'url': 'http://ydpllc.sen.go.kr', 'weekdayTime': '09:00~20:00'},
        {'address': '서울특별시 중랑구 면목로 397 (면목동)', 'closeDay': '매월 첫째, 셋째 월요일,법정공휴일(일요일제외) 및 근로자의날(5월1일), 임시휴관일',
         'gunguName': '중랑구', 'holidayTime': '00:00-00:00', 'latitude': '37.5873561521', 'lbiType': '공공도서관',
         'libName': '중랑구립면목정보도서관', 'longitude': '127.0875565596', 'phNum': '02-432-4120', 'satTime': '08:00-22:00',
         'sidoName': '서울특별시', 'tkDay': '14', 'tkNum': '5', 'url': 'http://www.jungnanglib.seoul.kr/mmlib',
         'weekdayTime': '08:00-23:00'},
        {'address': '서울특별시 은평구 증산로5길 6', 'closeDay': '금요일,법정공휴일', 'gunguName': '은평구', 'holidayTime': '09:00-18:00',
         'latitude': '37.5828079079', 'lbiType': '공공도서관', 'libName': '증산정보도서관', 'longitude': '126.9076711057',
         'phNum': '02-307-6030', 'satTime': '09:00-18:00', 'sidoName': '서울특별시', 'tkDay': '14', 'tkNum': '5',
         'url': 'http://www.jsplib.or.kr/', 'weekdayTime': '09:00-22:00'},
        {'address': '서울특별시 은평구 가좌로 7길 15', 'closeDay': '금요일,법정공휴일', 'gunguName': '은평구', 'holidayTime': '09:00-18:00',
         'latitude': '37.5859665629', 'lbiType': '공공도서관', 'libName': '응암정보도서관', 'longitude': '126.9196820594',
         'phNum': '02-308-2320', 'satTime': '09:00-18:00', 'sidoName': '서울특별시', 'tkDay': '14', 'tkNum': '5',
         'url': 'http://www.ealib.or.kr/', 'weekdayTime': '09:00-22:00'},
        {'address': '서울특별시 중랑구 신내로15길 197 (묵동)', 'closeDay': '매월 둘째, 넷째 월요일,법정공휴일(일요일제외) 및 근로자의날(5월1일), 임시휴관일',
         'gunguName': '중랑구', 'holidayTime': '00:00-00:00', 'latitude': '37.6151557', 'lbiType': '공공도서관',
         'libName': '중랑구립정보도서관', 'longitude': '127.0869050507', 'phNum': '02-490-9113', 'satTime': '07:00-22:00',
         'sidoName': '서울특별시', 'tkDay': '14', 'tkNum': '5', 'url': 'http://www.jungnanglib.seoul.kr/jnlib',
         'weekdayTime': '07:00-23:00'},
        {'address': '서울특별시 관악구 봉천로 279-8', 'closeDay': '매주 토/일요일/국가지정공휴일', 'gunguName': '관악구',
         'holidayTime': '00:00-00:00', 'latitude': '37.467081', 'lbiType': '작은도서관', 'libName': '보라매동 다사랑작은도서관',
         'longitude': '126.944781', 'phNum': '02-876-2879', 'satTime': '00:00-00:00', 'sidoName': '서울특별시',
         'tkDay': '14', 'tkNum': '5', 'url': 'http://lib.gwanak.go.kr/', 'weekdayTime': '10:00-18:00'},
        {'address': '서울특별시 관악구 쑥고개로 44', 'closeDay': '매주 토/일요일/국가지정공휴일', 'gunguName': '관악구',
         'holidayTime': '00:00-00:00', 'latitude': '37.479107', 'lbiType': '작은도서관', 'libName': '청룡동 숯고을작은도서관',
         'longitude': '126.941694', 'phNum': '02-876-4083', 'satTime': '00:00-00:00', 'sidoName': '서울특별시',
         'tkDay': '14', 'tkNum': '5', 'url': 'http://lib.gwanak.go.kr/', 'weekdayTime': '10:00-18:00'},
        {'address': '서울특별시 관악구 양녕로6다길 7', 'closeDay': '매주 토/일요일/국가지정공휴일', 'gunguName': '관악구',
         'holidayTime': '00:00-00:00', 'latitude': '37.484166', 'lbiType': '작은도서관', 'libName': '중앙동 새싹작은도서관',
         'longitude': '126.949749', 'phNum': '02-875-9513', 'satTime': '00:00-00:00', 'sidoName': '서울특별시',
         'tkDay': '14', 'tkNum': '5', 'url': 'http://lib.gwanak.go.kr/', 'weekdayTime': '10:00-18:00'},
        {'address': '부산광역시 연제구 황령산로 612(연산동)', 'closeDay': '매주월요일, 국가지정공휴일', 'gunguName': '연제구',
         'holidayTime': '00:00-00:00', 'latitude': '35.17414442', 'lbiType': '공공도서관', 'libName': '연제도서관',
         'longitude': '129.0829683', 'phNum': '051-665-5511', 'satTime': '09:00-18:00', 'sidoName': '부산광역시',
         'tkDay': '14', 'tkNum': '5', 'url': 'http://www.yeonje.go.kr/library/main.do', 'weekdayTime': '09:00-22:00'},
        {'address': '대전광역시 동구 동산초교로 34번길 56 (홍도동)', 'closeDay': '일요일, 관공서의 공휴일', 'gunguName': '동구',
         'holidayTime': '00:00-00:00', 'latitude': '36.3490805326', 'lbiType': '공공도서관', 'libName': '홍도도서관',
         'longitude': '127.4258279099', 'phNum': '042-259-7571', 'satTime': '09:00-13:00', 'sidoName': '대전광역시',
         'tkDay': '14', 'tkNum': '5', 'url': 'https://www.donggu.go.kr/dg/kor/contents/620',
         'weekdayTime': '09:00-18:00'},
        {'address': '울산광역시 북구 동대 15길 27 (호계동)', 'closeDay': '매주월요일, 법정공휴일', 'gunguName': '북구',
         'holidayTime': '09:00-18:00', 'latitude': '35.6291873', 'lbiType': '공공도서관', 'libName': '농소1동도서관',
         'longitude': '129.3545038', 'phNum': '052-241-7430', 'satTime': '09:00-18:00', 'sidoName': '울산광역시',
         'tkDay': '14', 'tkNum': '20', 'url': 'https://www.usbl.or.kr', 'weekdayTime': '09:00-22:00'},
        {'address': '경기도 양평군 양평읍 양근로 240-9', 'closeDay': '신정,설,추석연휴', 'gunguName': '양평군', 'holidayTime': '08:00-00:00',
         'latitude': '37.4859108923', 'lbiType': '공공도서관', 'libName': '중앙도서관', 'longitude': '127.494309',
         'phNum': '031-770-2711', 'satTime': '08:00-00:00', 'sidoName': '경기도', 'tkDay': '14', 'tkNum': '7',
         'url': 'http://www.yplib.go.kr', 'weekdayTime': '08:00-00:00'},
        {'address': '경기도 안산시 상록구충장로 528(성포동)', 'closeDay': '매주월요일,국가지정공휴일', 'gunguName': '안산시',
         'holidayTime': '00:00-00:00', 'latitude': '37.3251413', 'lbiType': '공공도서관', 'libName': '성포도서관',
         'longitude': '126.8503677', 'phNum': '031-481-2755', 'satTime': '07:00-23:00', 'sidoName': '경기도',
         'tkDay': '14', 'tkNum': '10', 'url': 'http://lib.iansan.net', 'weekdayTime': '07:00-23:00'},
        {'address': '서울특별시 중랑구 동일로114길 10 (상봉동)', 'closeDay': '매주월요일, 법정공휴일(일요일제외) 및 근로자의날(5월1일), 임시휴관일',
         'gunguName': '중랑구', 'holidayTime': '00:00-00:00', 'latitude': '37.5931272353', 'lbiType': '공공도서관',
         'libName': '중랑상봉도서관', 'longitude': '127.080932', 'phNum': '', 'satTime': '09:00-17:00', 'sidoName': '서울특별시',
         'tkDay': '14', 'tkNum': '5', 'url': 'http://www.jungnanglib.seoul.kr/sblib/', 'weekdayTime': '09:00-20:00'},
        {'address': '경상남도 양산시 물금읍 청룡로 11', 'closeDay': '법정공휴일(일요일 제외)', 'gunguName': '양산시',
         'holidayTime': '00:00-00:00', 'latitude': '35.325181', 'lbiType': '공공도서관', 'libName': '양산시립도서관',
         'longitude': '128.996715', 'phNum': '055-392-5900', 'satTime': '09:00-22:00', 'sidoName': '경상남도',
         'tkDay': '21', 'tkNum': '5', 'url': 'http://lib.yangsan.go.kr', 'weekdayTime': '09:00-22:00'}], '370767707': [
        {'address': '서울특별시 양천구 목동서로 113', 'closeDay': '1,3주 목요일 및 법정공휴일', 'gunguName': '양천구', 'holidayTime': '',
         'latitude': '37.53349939', 'lbiType': '공공도서관', 'libName': '양천도서관', 'longitude': '126.8757691',
         'phNum': '02-2062-3900', 'satTime': '09:00~17:00', 'sidoName': '서울특별시', 'tkDay': '', 'tkNum': '',
         'url': 'http://yclib.sen.go.kr', 'weekdayTime': '09:00~20:00'},
        {'address': '서울특별시 동작구 솔밭로 86', 'closeDay': '매주 월요일, 법정공휴일', 'gunguName': '동작구', 'holidayTime': '00:00-00:00',
         'latitude': '37.484056', 'lbiType': '공공도서관', 'libName': '사당솔밭도서관', 'longitude': '126.967369',
         'phNum': '02-585-8411', 'satTime': '09:00-17:00', 'sidoName': '서울특별시', 'tkDay': '14', 'tkNum': '5',
         'url': 'http://lib.dongjak.go.kr/', 'weekdayTime': '09:00-22:00'},
        {'address': '서울특별시 은평구 증산로17길 51', 'closeDay': '월요일,법정공휴일', 'gunguName': '은평구', 'holidayTime': '09:00-18:00',
         'latitude': '37.591414', 'lbiType': '공공도서관', 'libName': '내를건너서숲으로도서관', 'longitude': '126.907816',
         'phNum': '02-307-6701', 'satTime': '09:00-18:00', 'sidoName': '서울특별시', 'tkDay': '14', 'tkNum': '5',
         'url': 'http://www.nslib.or.kr', 'weekdayTime': '09:00-22:00'},
        {'address': '서울특별시 은평구 통일로 972', 'closeDay': '월요일,법정공휴일', 'gunguName': '은평구', 'holidayTime': '09:00-18:00',
         'latitude': '37.6301404375', 'lbiType': '공공도서관', 'libName': '은뜨락도서관', 'longitude': '126.9199290898',
         'phNum': '02-389-7635', 'satTime': '09:00-18:00', 'sidoName': '서울특별시', 'tkDay': '14', 'tkNum': '5',
         'url': 'https://www.edlib.or.kr', 'weekdayTime': '09:00-22:00'},
        {'address': '부산광역시 남구 황령대로319번가길 147(대연동)', 'closeDay': '매주 월요일', 'gunguName': '남구',
         'holidayTime': '11:00-17:00', 'latitude': '35.1524057568', 'lbiType': '작은도서관', 'libName': '대동골문화센터작은도서관',
         'longitude': '129.0889884063', 'phNum': '051-607-3380', 'satTime': '11:00-17:00', 'sidoName': '부산광역시',
         'tkDay': '15', 'tkNum': '2', 'url': '', 'weekdayTime': '11:00-17:00'},
        {'address': '부산광역시 연제구 아시아드대로22번길15(거제동)', 'closeDay': '매주일요일, 국가지정공휴일', 'gunguName': '연제구',
         'holidayTime': '00:00-00:00', 'latitude': '35.18764403', 'lbiType': '작은도서관', 'libName': '거제2동새마을문고작은도서관',
         'longitude': '129.0701317', 'phNum': '051-665-4511', 'satTime': '10:00-14:00', 'sidoName': '부산광역시',
         'tkDay': '14', 'tkNum': '5', 'url': '', 'weekdayTime': '10:00-19:00'},
        {'address': '울산광역시 북구 동대 15길 27 (호계동)', 'closeDay': '매주월요일, 법정공휴일', 'gunguName': '북구',
         'holidayTime': '09:00-18:00', 'latitude': '35.6291873', 'lbiType': '공공도서관', 'libName': '농소1동도서관',
         'longitude': '129.3545038', 'phNum': '052-241-7430', 'satTime': '09:00-18:00', 'sidoName': '울산광역시',
         'tkDay': '14', 'tkNum': '20', 'url': 'https://www.usbl.or.kr', 'weekdayTime': '09:00-22:00'},
        {'address': '경기도 평택시 지산로 48', 'closeDay': '매월 2,4번째 월요일/국가지정공휴일', 'gunguName': '평택시',
         'holidayTime': '09:00-22:00', 'latitude': '37.078929', 'lbiType': '공공도서관', 'libName': '지산초록도서관',
         'longitude': '127.0603421919', 'phNum': '031-8024-7451', 'satTime': '09:00-22:00', 'sidoName': '경기도',
         'tkDay': '14', 'tkNum': '10', 'url': 'http://www.ptlib.go.kr', 'weekdayTime': '09:00-22:00'},
        {'address': '경기도 양평군 청운면 용두민속장터길 2', 'closeDay': '매주일,월/공휴일', 'gunguName': '양평군', 'holidayTime': '00:00-00:00',
         'latitude': '37.553631', 'lbiType': '작은도서관', 'libName': '청운작은도서관', 'longitude': '127.708314',
         'phNum': '031-775-0552', 'satTime': '09:00-18:00', 'sidoName': '경기도', 'tkDay': '14', 'tkNum': '7',
         'url': 'http://www.yplib.go.kr', 'weekdayTime': '09:00-18:00'},
        {'address': '경상남도 양산시 물금읍 청룡로 11', 'closeDay': '법정공휴일(일요일 제외)', 'gunguName': '양산시',
         'holidayTime': '00:00-00:00', 'latitude': '35.325181', 'lbiType': '공공도서관', 'libName': '양산시립도서관',
         'longitude': '128.996715', 'phNum': '055-392-5900', 'satTime': '09:00-22:00', 'sidoName': '경상남도',
         'tkDay': '21', 'tkNum': '5', 'url': 'http://lib.yangsan.go.kr', 'weekdayTime': '09:00-22:00'}], '381050458': [
        {'address': '경기도 평택시 지산로 48', 'closeDay': '매월 2,4번째 월요일/국가지정공휴일', 'gunguName': '평택시',
         'holidayTime': '09:00-22:00', 'latitude': '37.078929', 'lbiType': '공공도서관', 'libName': '지산초록도서관',
         'longitude': '127.0603421919', 'phNum': '031-8024-7451', 'satTime': '09:00-22:00', 'sidoName': '경기도',
         'tkDay': '14', 'tkNum': '10', 'url': 'http://www.ptlib.go.kr', 'weekdayTime': '09:00-22:00'}], '336807844': [
        {'address': '경상남도 창원시 진해구 충장로575', 'closeDay': '국가지정공휴일+홀수토요일', 'gunguName': '창원시',
         'holidayTime': '00:00-00:00', 'latitude': '35.1379688011', 'lbiType': '작은도서관', 'libName': '우성아파트새마을문고',
         'longitude': '128.7027352367', 'phNum': '055-547-0331', 'satTime': '10:00-13:00', 'sidoName': '경상남도',
         'tkDay': '14', 'tkNum': '3', 'url': '', 'weekdayTime': '10:00-18:00'}], '410065031': [
        {'address': '서울특별시 강남구 선릉로4길 30', 'closeDay': '2,4주 목요일 및 법정공휴일', 'gunguName': '강남구', 'holidayTime': '',
         'latitude': '37.48308019', 'lbiType': '공공도서관', 'libName': '개포도서관', 'longitude': '127.063867',
         'phNum': '02-3460-8200', 'satTime': '09:00~17:00', 'sidoName': '서울특별시', 'tkDay': '', 'tkNum': '',
         'url': 'http://gplib.sen.go.kr', 'weekdayTime': '09:00~20:00'},
        {'address': '부산광역시 연제구 황령산로 612(연산동)', 'closeDay': '매주월요일, 국가지정공휴일', 'gunguName': '연제구',
         'holidayTime': '00:00-00:00', 'latitude': '35.17414442', 'lbiType': '공공도서관', 'libName': '연제도서관',
         'longitude': '129.0829683', 'phNum': '051-665-5511', 'satTime': '09:00-18:00', 'sidoName': '부산광역시',
         'tkDay': '14', 'tkNum': '5', 'url': 'http://www.yeonje.go.kr/library/main.do', 'weekdayTime': '09:00-22:00'}],
           '431627980': [{'address': '경기도 양평군 양평읍 양근로 240-9', 'closeDay': '신정,설,추석연휴', 'gunguName': '양평군',
                          'holidayTime': '08:00-00:00', 'latitude': '37.4859108923', 'lbiType': '공공도서관',
                          'libName': '중앙도서관', 'longitude': '127.494309', 'phNum': '031-770-2711',
                          'satTime': '08:00-00:00', 'sidoName': '경기도', 'tkDay': '14', 'tkNum': '7',
                          'url': 'http://www.yplib.go.kr', 'weekdayTime': '08:00-00:00'}], '464812636': [
        {'address': '울산광역시 북구 매곡로 138-19 (매곡동)', 'closeDay': '매주월요일, 법정공휴일', 'gunguName': '북구',
         'holidayTime': '09:00-18:00', 'latitude': '35.64650566', 'lbiType': '공공도서관', 'libName': '매곡도서관',
         'longitude': '129.3588981', 'phNum': '052-241-7470', 'satTime': '09:00-18:00', 'sidoName': '울산광역시',
         'tkDay': '14', 'tkNum': '20', 'url': 'https://www.usbl.or.kr', 'weekdayTime': '09:00-22:00'}], '542280187': [
        {'address': '울산광역시 북구 아진1로 47(천곡동)', 'closeDay': '매주월요일, 법정공휴일', 'gunguName': '북구',
         'holidayTime': '09:00-18:00', 'latitude': '35.6330929', 'lbiType': '공공도서관', 'libName': '농소3동도서관',
         'longitude': '129.3355864', 'phNum': '052-241-7440', 'satTime': '09:00-18:00', 'sidoName': '울산광역시',
         'tkDay': '14', 'tkNum': '20', 'url': 'https://www.usbl.or.kr', 'weekdayTime': '09:00-22:00'}], '484627217': [
        {'address': '서울특별시 관악구 난곡로 249', 'closeDay': '매주 토/일요일/국가지정공휴일', 'gunguName': '관악구',
         'holidayTime': '00:00-00:00', 'latitude': '37.476132', 'lbiType': '작은도서관', 'libName': '미성동 책의향기작은도서관',
         'longitude': '126.915527', 'phNum': '02-830-5312', 'satTime': '00:00-00:00', 'sidoName': '서울특별시',
         'tkDay': '14', 'tkNum': '5', 'url': 'http://lib.gwanak.go.kr/', 'weekdayTime': '10:00-18:00'}], '756148221': [
        {'address': '경상북도 청도군 화양읍 청화로 79-3', 'closeDay': '매주금요일,국가지정공휴일', 'gunguName': '청도군',
         'holidayTime': '00:00-00:00', 'latitude': '35.6481840745', 'lbiType': '어린이도서관', 'libName': '청도어린이도서관',
         'longitude': '128.7363307', 'phNum': '054-370-6753', 'satTime': '09:00-17:00', 'sidoName': '경상북도',
         'tkDay': '300', 'tkNum': '57445', 'url': 'lib.cheongdo.go.kr', 'weekdayTime': '09:00-18:00'}], '819614332': [
        {'address': '서울특별시 양천구 목동서로 113', 'closeDay': '1,3주 목요일 및 법정공휴일', 'gunguName': '양천구', 'holidayTime': '',
         'latitude': '37.53349939', 'lbiType': '공공도서관', 'libName': '양천도서관', 'longitude': '126.8757691',
         'phNum': '02-2062-3900', 'satTime': '09:00~17:00', 'sidoName': '서울특별시', 'tkDay': '', 'tkNum': '',
         'url': 'http://yclib.sen.go.kr', 'weekdayTime': '09:00~20:00'}]}


def calcdistance(book_list, cur_lati, cur_long):
    global lib_loc
    # per each book
    for book in book_list:
        # per each library in a book
        for lib in book_list[book]:
            # calculate distance
            lib['distance'] = (
                    6371 *
                    acos(cos(radians(cur_lati)) *
                         cos(radians(float(lib['latitude']))) *
                         cos(radians(float(lib['longitude'])) -
                             radians(cur_long)) +
                         sin(radians(cur_lati)) *
                         sin(radians(float(lib['latitude']))))
            )
        # sort data and update
        pdata = pd.DataFrame.from_dict(book_list[book])
        sdata = pdata.sort_values("distance")
        #ldata = pdata.nsmallest(5, 'distance')
        #rdata = ldata.to_dict('records')
        rdata = sdata.to_dict('records')
        book_list[book] = rdata
    return book_list

if __name__ == '__main__':
    # calcdistance(book_lib(book_name('정의란 무엇인가', '마이클 샌델')), 37.599343, 126.932246)
    print(calcdistance(lib_loc, 37.599343, 126.932246))
    # print(json.dumps(lib_loc, ensure_ascii=False, indent=4))