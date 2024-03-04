import pandas as pd

def area_preprocess(df_area):
    df_area = df_area[(df_area['VISIT_AREA_TYPE_CD'] == 1) | (df_area['VISIT_AREA_TYPE_CD'] == 2) |
                  (df_area['VISIT_AREA_TYPE_CD'] == 3) | (df_area['VISIT_AREA_TYPE_CD'] == 4) |
                  (df_area['VISIT_AREA_TYPE_CD'] == 5) | (df_area['VISIT_AREA_TYPE_CD'] == 6) |
                  (df_area['VISIT_AREA_TYPE_CD'] == 7) | (df_area['VISIT_AREA_TYPE_CD'] == 8) ]
    df_area.dropna(subset = ['LOTNO_ADDR'], inplace = True)
    df_area = df_area.reset_index(drop = True)
    
    sido = []
    gungu = []
    
    for i in range(len(df_area['LOTNO_ADDR'])):
        sido.append(df_area['LOTNO_ADDR'][i].split(' ')[0])
        gungu.append(df_area['LOTNO_ADDR'][i].split(' ')[1])
    df_area['SIDO'] = sido
    df_area['GUNGU'] = gungu
    
    area_feature = ['TRAVEL_ID', 'VISIT_AREA_NM', 'VISIT_ORDER', 'SIDO', 'GUNGU', 'VISIT_AREA_TYPE_CD', 'X_COORD', 'Y_COORD',
                   'VISIT_START_YMD', 'DGSTFN', 'REVISIT_INTENTION', 'RCMDTN_INTENTION', 'RESIDENCE_TIME_MIN', 'REVISIT_YN'
    ]
    df_area = df_area[area_feature]
    
    return df_area

def travel_preprocess(df):
    travel_list = []
    for i in range (len(df)):
        check = df['TRAVEL_MISSION_CHECK'][i]
        priority = int(check.split(';')[0])
        travel_list.append(priority)
    
    # 가장 먼저 있는 미션은 미션 우선순위 1순위로 저장
    df['TRAVEL_MISSION_PRIORITY'] = travel_list
    
    # 날짜 열을 datetime 형식으로 변환
    df['TRAVEL_START_YMD'] = pd.to_datetime(df['TRAVEL_START_YMD'])
    df['TRAVEL_END_YMD'] = pd.to_datetime(df['TRAVEL_END_YMD'])

    # 여행 일수 계산 (여행 종료일 - 여행 시작일) + 1
    df['TRAVEL_DAYS'] = (df['TRAVEL_END_YMD'] - df['TRAVEL_START_YMD']).dt.days + 1
    df_travel = df[['TRAVEL_ID', 'TRAVELER_ID', 'TRAVEL_MISSION_PRIORITY', 'TRAVEL_DAYS']]
    
    return df_travel

def traveller_preprocess(df_traveller):
    traveller_feature = [
        'TRAVELER_ID', 'GENDER', 'AGE_GRP', 'INCOME',
        'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4', 'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
        'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM'
    ]
    df_traveller = df_traveller[traveller_feature]
    
    return df_traveller

def preprocess_values(df):
    df = df.dropna(subset = ['TRAVEL_STYL_1', 'TRAVEL_MOTIVE_1', 'DGSTFN'])
    df.reset_index(drop = True, inplace = True)

    df['RESIDENCE_TIME_MIN'] = df['RESIDENCE_TIME_MIN'].replace(0,60)
    df['REVISIT_YN'] = df['REVISIT_YN'].replace('N', 0)
    df['REVISIT_YN'] = df['REVISIT_YN'].replace('Y', 1)
    df['GENDER'] = df['GENDER'].replace('남', 0)
    df['GENDER'] = df['GENDER'].replace('여', 1)
    
    # 'SIDO'가 '광복동' 또는 '동부리'인 행 삭제
    df = df[~df['SIDO'].isin(['광복동', '동부리'])]

    # 이름 통일을 위한 매핑 딕셔너리
    name_mapping = {
        '강원도': '강원',
        '경기도': '경기',
        '경상남도': '경남',
        '경상북도': '경북',
        '광주광역시': '광주',
        '대구광역시': '대구',
        '대전광역시': '대전',
        '부산광역시': '부산',
        '서울특별시': '서울',
        '세종특별자치시': '세종',
        '울산광역시': '울산',
        '인천광역시': '인천',
        '전라남도': '전남',
        '전라북도': '전북',
        '충청남도': '충남',
        '충청북도': '충북',
        '제주특별자치도': '제주'
    }

    # 이름 통일 적용
    df['SIDO'] = df['SIDO'].map(name_mapping).fillna(df['SIDO'])
    
    return df

def preprocess_values_embed(df):
    df = df.dropna(subset = ['TRAVEL_STYL_1', 'TRAVEL_MOTIVE_1', 'DGSTFN'])
    df.reset_index(drop = True, inplace = True)

    df['RESIDENCE_TIME_MIN'] = df['RESIDENCE_TIME_MIN'].replace(0,60)
    df['REVISIT_YN'] = df['REVISIT_YN'].replace('N', 0)
    df['REVISIT_YN'] = df['REVISIT_YN'].replace('Y', 1)
    df['GENDER'] = df['GENDER'].replace('남', 0)
    df['GENDER'] = df['GENDER'].replace('여', 1)
    
    # 'SIDO'가 '광복동' 또는 '동부리'인 행 삭제
    df = df[~df['SIDO'].isin(['광복동', '동부리'])]

    # 이름 통일을 위한 매핑 딕셔너리
    name_mapping = {
        '강원도': '강원',
        '경기도': '경기',
        '경상남도': '경남',
        '경상북도': '경북',
        '광주광역시': '광주',
        '대구광역시': '대구',
        '대전광역시': '대전',
        '부산광역시': '부산',
        '서울특별시': '서울',
        '세종특별자치시': '세종',
        '울산광역시': '울산',
        '인천광역시': '인천',
        '전라남도': '전남',
        '전라북도': '전북',
        '충청남도': '충남',
        '충청북도': '충북',
        '제주특별자치도': '제주'
    }

    # 이름 통일 적용
    df['SIDO'] = df['SIDO'].map(name_mapping).fillna(df['SIDO'])

    #EMBEDDING 위해 0부터 시작하려고 1 감소
    df['TRAVEL_STYL_1'] = df['TRAVEL_STYL_1'] - 1
    df['TRAVEL_STYL_2'] = df['TRAVEL_STYL_2'] - 1
    df['TRAVEL_STYL_3'] = df['TRAVEL_STYL_3'] - 1
    df['TRAVEL_STYL_4'] = df['TRAVEL_STYL_4'] - 1
    df['TRAVEL_STYL_5'] = df['TRAVEL_STYL_5'] - 1
    df['TRAVEL_STYL_6'] = df['TRAVEL_STYL_6'] - 1
    df['TRAVEL_STYL_7'] = df['TRAVEL_STYL_7'] - 1
    df['TRAVEL_STYL_8'] = df['TRAVEL_STYL_8'] - 1
    df['TRAVEL_MOTIVE_1'] = df['TRAVEL_MOTIVE_1'] - 1
    
    return df

def cbf_preprocess(df_traveller, df_travel, df_area):

    df_traveller = traveller_preprocess(df_traveller)
    df_travel = travel_preprocess(df_travel)
    df_area = area_preprocess(df_area)

    df = pd.merge(df_travel, df_traveller, left_on='TRAVELER_ID', right_on='TRAVELER_ID', how='inner')
    df = pd.merge(df_area, df, left_on='TRAVEL_ID', right_on='TRAVEL_ID', how='right')

    df = preprocess_values(df)

    remain_feature = [
        'GENDER', 'AGE_GRP', 'TRAVEL_COMPANIONS_NUM',
        'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4', 'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
        'TRAVEL_MOTIVE_1', 'TRAVEL_MISSION_PRIORITY', 'VISIT_AREA_NM', 'DGSTFN'
    ]

    df = df[remain_feature]
    df = df.dropna(subset=remain_feature)

    categorical_features = [ 
        'GENDER', 'TRAVEL_MOTIVE_1',
        'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4', 'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
        'TRAVEL_MISSION_PRIORITY', 'VISIT_AREA_NM'
    ]

    for feature in categorical_features:
        df[feature] = df[feature].astype(str)

    return df, categorical_features

def cf_preprocess(df_traveller, df_travel, df_area):

    df_traveller = traveller_preprocess(df_traveller)
    df_travel = travel_preprocess(df_travel)
    df_area = area_preprocess(df_area)

    df = pd.merge(df_travel, df_traveller, left_on='TRAVELER_ID', right_on='TRAVELER_ID', how='inner')
    df = pd.merge(df_area, df, left_on='TRAVEL_ID', right_on='TRAVEL_ID', how='right')

    df = preprocess_values(df)

    features = [
        'TRAVELER_ID', 'GENDER', 'AGE_GRP', 'INCOME', 'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3',
        'TRAVEL_STYL_4', 'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
        'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM',
        'VISIT_AREA_NM', 'VISIT_AREA_TYPE_CD', 'SIDO', 'GUNGU', 'RESIDENCE_TIME_MIN', 'REVISIT_YN',
        'DGSTFN'
    ]

    df = df[features]
    df = df.dropna(subset=features)

    return df

def cf_preprocess_embed(df_traveller, df_travel, df_area):

    df_traveller = traveller_preprocess(df_traveller)
    df_travel = travel_preprocess(df_travel)
    df_area = area_preprocess(df_area)

    df = pd.merge(df_travel, df_traveller, left_on='TRAVELER_ID', right_on='TRAVELER_ID', how='inner')
    df = pd.merge(df_area, df, left_on='TRAVEL_ID', right_on='TRAVEL_ID', how='right')

    df = preprocess_values_embed(df)

    features = [
        'TRAVELER_ID', 'GENDER', 'AGE_GRP', 'INCOME', 'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3',
        'TRAVEL_STYL_4', 'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
        'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM',
        'VISIT_AREA_NM', 'VISIT_AREA_TYPE_CD', 'SIDO', 'GUNGU', 'RESIDENCE_TIME_MIN', 'REVISIT_YN',
        'DGSTFN'
    ]

    df = df[features]
    df = df.dropna(subset=features)

    return df