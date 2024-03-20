import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
import matplotlib.pyplot as plt
import seaborn as sns
import time

sns.set_theme(style='whitegrid', font_scale=1.5)
sns.set_palette('Set2', n_colors=10)
# plt.rc('font', family='AppleGothic')
plt.rc('font', family='Malgun Gothic')

plt.rc('axes', unicode_minus=False)
from matplotlib.cm import get_cmap

# Get the 'tab10' colormap
tab10 = get_cmap('tab10')

SIDOS={11:'서울특별시',26:'부산광역시',27:'대구광역시',28:'인천광역시',29:'광주광역시',30:'대전광역시',31:'울산광역시',36:'세종특별자치시', 41:'경기도', 42:'강원도', 43:'충청북도',44:'충청남도',45:'전라북도', 46:'전라남도', 47:'경상북도', 48:'경상남도', 49:'제주특별자치도',50:'etc'}

@st.cache_data
def get_datas():
    data = pd.read_csv("health_2017~2021.csv", index_col=0)
    return data

data = get_datas()
def txt_gen(txt):
    for t in list(txt):
        yield t
        time.sleep(0.2)
def home():
    APP_SUB_TITLE = '건강 데이터 분석'
    # st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)
    st.subheader("데이터 정보")
    st.info("건강검진정보 (2017년~2021년)")
    st.divider()
    txt = "현재 데이터는 2017년부터 2021년도까지의 건강검진 정보를 나타냅니다."


    st.write_stream(txt_gen(txt))
    if st.button("next",use_container_width=True):
        st.session_state['page']='시기별'
        st.rerun()

def period():
    st.title("시기별 분석")

    tmp = data.copy()
    st.sidebar.header('성별')
    option01 = st.sidebar.multiselect('남성=1, 여성=2', (tmp.SEX.unique()), default=(tmp.SEX.unique()))
    tmp = tmp[tmp['SEX'].isin(option01)]
    st.subheader("시기별 분석 데이터 샘플")
    st.dataframe(tmp.head())
    st.info("2020년 데이터는 없어서 제외했습니다")

    st.subheader('코로나19 전후 건강상태 변화')
    st.write('건강한 사람 비율(HEALTHY), 음주 비율(DRK_YN), 흡연비율(SMK_STAT_TYPE_CD),\n 시력(SIGHT_LEFT, SIGHT_RIGHT), 혈청크레아틴(CREATININE) 등에 주목')
    tmp = tmp.groupby('HCHK_YEAR').mean()
    col = st.selectbox('분석 컬럼 선택',tmp.columns[2:])
    whole_values = tmp[tmp.index!=2020].groupby('HCHK_YEAR')[[col]].mean()
    st.download_button('Download',whole_values.to_csv(encoding='euc-kr'), '시기건강.csv')
    colors = [tab10.colors[i % 10] for i in range(len(whole_values))]

    fig, ax = plt.subplots()
    ax.set_title(col)
    ax.bar(whole_values.index.astype(str), whole_values[col], color=colors)
    overall_average = whole_values[col].mean()
    ax.axhline(y=overall_average, color='gray', linestyle='--', linewidth=2)
    st.pyplot(fig)

    if st.button("next",use_container_width=True):
        st.session_state['page']='연령별'
        st.rerun()

def age():

    tmp = data.copy()
    st.sidebar.header('성별')
    option01 = st.sidebar.multiselect('남성=1, 여성=2', (tmp.SEX.unique()), default=(tmp.SEX.unique()))
    tmp = tmp[tmp['SEX'].isin(option01)]

    st.title("연령별 분석")
    st.subheader('5세 단위별 성인 건강상태')
    st.write('20대 = 5, 6 / 30대 = 7,8 / 40대 = 9, 10 / 50대 = 11, 12 / 60대 = 13, 14 / 70대 = 15, 16 / 80대 이상 = 17, 18')
    st.write('')
    tmp = tmp.groupby('AGE_GROUP').mean()
    col = st.selectbox('분석 컬럼 선택',tmp.columns[2:])
    whole_values = tmp.groupby('AGE_GROUP')[[col]].mean()
    st.download_button('Download',whole_values.to_csv(encoding='euc-kr'), '연령건강.csv')
    colors = [tab10.colors[i % 10] for i in range(len(whole_values))]

    fig, ax = plt.subplots()
    ax.set_title(col)
    ax.bar(whole_values.index.astype(str), whole_values[col], color=colors)
    overall_average = whole_values[col].mean()
    ax.axhline(y=overall_average, color='gray', linestyle='--', linewidth=2)
    st.pyplot(fig)
    # st.bar_chart(whole_values, use_container_width=True)

    if st.button("next",use_container_width=True):
        st.session_state['page']='시도별'
        st.rerun()

def sido():
    tmp = data.groupby('SIDO').mean()
    tmp.index = [SIDOS[idx] for idx in tmp.index]
    tmp.reset_index(inplace=True)
    # tmp.AGE_GROUP=tmp.AGE_GROUP.astype('int')
    tiles = ['OpenStreetMap', 'CartoDB positron', 'CartoDB dark_matter']
    with st.sidebar:
        st.divider()
        t = st.sidebar.radio('Map', tiles)
        col = st.selectbox('분석 컬럼 선택',tmp.columns[2:])

    map = folium.Map(location=[36.194012, 127.5019596], zoom_start=7, scrollWheelZoom=True, tiles=t)
    choropleth = folium.Choropleth(
        geo_data='SIDO_MAP_2022_cp949.json',
        data=tmp,
        columns=('index', col),
        key_on='feature.properties.CTP_KOR_NM',
        line_opacity=0.8,
        highlight=True
    )
    choropleth.geojson.add_to(map)

    st_map = st_folium(map, width=600, height=700)