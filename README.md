
# 나라장터 용역 입찰공고 모니터링 대시보드 (Streamlit)

이 프로젝트는 `getBidPblancListInfoServc` API로 수집한 입찰공고 데이터를
Firebase(DB)에 적재해 두었다는 가정하에,
해당 데이터를 조회·필터링·열람하는 내부용 대시보드 예제입니다.

현재 코드는 **샘플 CSV(`sample_data.csv`)** 를 사용하도록 되어 있으므로,
Firebase 연동 전까지는 그대로 실행해서 화면 구조를 확인할 수 있습니다.

## 실행 방법

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Firebase와 연동하려면

1. `load_data()` 함수 내부를 수정하여
   Firebase Firestore 또는 Realtime Database에서 데이터를 읽어오도록 변경합니다.
2. 컬럼 스키마는 다음과 같이 맞춰 주면 됩니다.

- 공고기관명: `ntceInsttNm`
- 수요기관명: `dminsttNm`
- 입찰공고명: `bidNtceNm`
- 배정예산금액: `asignBdgtAmt`
- 추정가격: `presmptPrce`
- 재공고여부: `reNtceYn` (Y/N)
- 입찰공고일시: `bidNtceDt`
- 입찰개시일시: `bidBeginDt`
- 입찰마감일시: `bidClseDt`
- 공고기관담당자명: `ntceInsttOfclNm`
- 집행관명(담당자명 대체용): `exctvNm`
- 공고기관담당자전화번호: `ntceInsttOfclTelNo`
- 입찰참가자격등록마감일시: `bidQlfctRgstDt`
- 공고규격서 URL/파일명: `ntceSpecDocUrl1~10`, `ntceSpecFileNm1~10`
- 입찰공고상세URL: `bidNtceDtlUrl`
- 입찰공고URL: `bidNtceUrl`
- 통합공고번호: `untyNtceNo`
- 입찰공고번호: `bidNtceNo`

## 화면 구성 요약

- 좌측 사이드바: 조회 기준, 기간/공고번호, 예가, 키워드, 기관, 재공고 여부, 상태 필터
- 상단: 검색 결과 요약 (공고 수, 평균/최대 예가, 재공고 비율)
- 중앙: 입찰공고 목록 테이블
- 하단: 선택 공고 상세 정보 + 첨부파일 링크 + 상세 URL

