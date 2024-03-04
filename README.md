# Trip-Plan-RecSys
CBF, CF 기반의 여행지 추천 시스템과
Genetic Algorithm 기반으로 만든 여행 스케줄 추천시스템입니다(업데이트 예정)

## 사용 데이터
AIHUB의 국내 여행로그 데이터(수도권, 서부권, 동부권, 제주도 및 도서지역) 4개 데이터 통합
수도권: https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71581
서부권: https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71582
동부권: https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71585
제주도 및 도서지역: https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71584
다운로드를 받은 후 각 csv를 밑의 데이터 구조에 맞게 넣으면 된다.

## 설치 방법
'''
$ git clone https://github.com/bhmoon98/Trip-Plan-RecSys.git
$ mkdir data csv
$ pip install -r requirements.txt
'''

## 데이터 구조
```
csv/
├── area/
│ ├── tn_visit_area_info_A.csv
│ ├── tn_visit_area_info_B.csv
│ ├── tn_visit_area_info_C.csv
│ └── tn_visit_area_info_D.csv
├── code/
│ ├── tc_codea_A.csv
│ └── tc_codeb_B.csv
├── consume/
│ ├── tn_activity_consume_his_A.csv
│ ├── tn_activity_consume_his_B.csv
│ ├── tn_activity_consume_his_C.csv
│ ├── tn_activity_consume_his_D.csv
│ ├── tn_adv_consume_his_A.csv
│ ├── tn_adv_consume_his_B.csv
│ ├── tn_adv_consume_his_C.csv
│ ├── tn_adv_consume_his_D.csv
│ ├── tn_lodge_consume_his_A.csv
│ ├── tn_lodge_consume_his_B.csv
│ ├── tn_lodge_consume_his_C.csv
│ ├── tn_lodge_consume_his_D.csv
│ ├── tn_mvmn_consume_his_A.csv
│ ├── tn_mvmn_consume_his_B.csv
│ ├── tn_mvmn_consume_his_C.csv
│ └── tn_mvmn_consume_his_D.csv
├── move/
│ ├── tn_move_his_A.csv
│ ├── tn_move_his_B.csv
│ ├── tn_move_his_C.csv
│ └── tn_move_his_D.csv
├── sgg/
│ └── tc_sgg.csv
└── travel/
├── tn_travel_A.csv
├── tn_travel_B.csv
├── tn_travel_C.csv
└── tn_travel_D.csv
└── traveller/
├── tn_traveller_master_A.csv
├── tn_traveller_master_B.csv
├── tn_traveller_master_C.csv
└── tn_traveller_master_D.csv
```

preprocess 폴더의 aggregrate.ipynb 파일을 실행시키면 데이터가 통합되고 전처리됩니다.
최종 데이터 구조는 다음과 같습니다.

'''
data/
├── activity_exp.csv
├── adv_exp.csv
├── area.csv
├── lodge_exp.csv
├── move_his.csv
├── mvmn_exp.csv
├── travel.csv
└── traveller.csv
'''

## 파일 설명
/preprocess/aggregate.ipynb: 데이터 통합 및 재배치
/preprocess/categorical_data.ipynb: 범주형 데이터 설명 및 열람
/preprocess/preprocess.py: 각 필터링에 필요한 데이터만 전처리
CBF.ipynb: 컨텐츠 기반 필터링 모델 학습(CatBoost), cbf_model.cbm 생성됨.
CBF_Inference.ipynb: cbf_model.cbm을 사용하여 초기 사용자 여행지 추천
CF.ipynb: user-item matrix를 사용하여 유사한 사용자 추천 및 유사한 아이템 추천
CF_Embedding.ipynb: Neural MF와 Embedding Vector를 사용한 협업 필터링

## 업데이트 예정
만족도, 재방문 의향, 추천 의향 중 사용자의 의향을 가장 잘 드러내는 계수 비율(Grid Search, Random Search 사용)
-> 이 결과로 사용자의 rating을 만족도로 설정함
사용자가 여행에 사용한 비용에 관한 데이터 분석(exp 레이블 csv)
Genetic Algorithm을 사용한 여행 스케줄 추천 시스템
추천시스템 Demo(개발 완료)





