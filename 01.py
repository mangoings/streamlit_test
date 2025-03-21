import os
import pandas as pd
import streamlit as st

os.chdir(os.path.dirname(os.path.abspath(__file__))) # streamlit 파일 디렉토리 경로 일치시키기
df = pd.read_csv('./output/2025_daegu_apt_total.csv')
# print(df.head())

gu_list = df['구'].sort_values().unique() # 중복제거, 오름차순 정렬

with st.sidebar:
    gu_selected = st.selectbox(label='1. 구를 선택주세요!',
                               options=gu_list,
                               index=None,
                               placeholder='== 선택 ==')
    if gu_selected:
        df1 = df.query(f'구 == "{gu_selected}"').reset_index(drop=True)

        dong_list = df1['동'].sort_values().unique()
        dong_selected = st.selectbox(label='2. 동을 선택주세요!',
                                   options=dong_list,
                                   index=None,
                                   placeholder='== 선택 ==')
        if dong_selected:
            df1 = df1.query(f'동 == "{dong_selected}"').reset_index(drop=True)



st.title('2025년 대구 아파트 매매 내역')
if gu_selected:
    st.write(df1)