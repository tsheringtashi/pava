import streamlit as st
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd

img = Image.open("D:/LAND RATE/additional_land/BoB-Logo.png")
st.set_page_config(page_title= "LAND RATE BoBL",
                   page_icon=":bar_chart:",
                   layout="wide",
                   )
df_bumthang = pd.read_csv("D:/LAND RATE/additional_land/bumthang.csv")
df_bumthang = df_bumthang.iloc[:,1:]

df_dagana = pd.read_csv("D:/LAND RATE/additional_land/dagana.csv", index_col=False)
df_dagana = df_dagana.iloc[:,1:]

df_debsi = pd.read_csv("D:/LAND RATE/additional_land/debsi.csv")
df_debsi = df_debsi.iloc[:,1:]
# df_debsi["BOB_2021_RATE"]=df_debsi["BOB_2021_RATE"].astype(int)

df_haa = pd.read_csv("D:/LAND RATE/additional_land/haa.csv")
df_haa = df_haa.iloc[:,1:]

df_gasa = pd.read_csv("D:/LAND RATE/additional_land/gasa.csv")
df_gasa = df_gasa.iloc[:,1:]

df_karbreytar = pd.read_csv("D:/LAND RATE/additional_land/karbreytar.csv")
df_karbreytar = df_karbreytar.iloc[:,1:]

df_lhuentse = pd.read_csv("D:/LAND RATE/additional_land/lhuentse.csv")
df_lhuentse = df_lhuentse.iloc[:,1:]

df_outskirt_thim = pd.read_csv("D:/LAND RATE/additional_land/outskirt_thim.csv")
df_outskirt_thim = df_outskirt_thim.iloc[:,1:]
# df_outskirt_thim["BOB_2021_RATE"]=df_outskirt_thim["BOB_2021_RATE"].astype(int)

df_paro = pd.read_csv("D:/LAND RATE/additional_land/Paro.csv")
df_paro = df_paro.iloc[:,1:]
df_paro["BOB_2021_RATE"]= df_paro["BOB_2021_RATE"].astype(int)

df_pling_town = pd.read_csv("D:/LAND RATE/additional_land/pling_town.csv")
df_pling_town = df_pling_town.iloc[:,1:]

df_pling_karbreytar = pd.read_csv("D:/LAND RATE/additional_land/karbreytar.csv")
df_pling_karbreytar = df_pling_karbreytar.iloc[:,1:]


df_pasakha = pd.read_csv("D:/LAND RATE/additional_land/pasakha.csv")
df_pasakha = df_pasakha.iloc[:,1:]

df_pling_outskirt = pd.read_csv("D:/LAND RATE/additional_land/pling_outskirt.csv")
df_pling_outskirt = df_pling_outskirt.iloc[:,1:]

df_punakha = pd.read_csv("D:/LAND RATE/additional_land/punakha.csv")
df_punakha = df_punakha.iloc[:,1:]

df_samtse = pd.read_csv("D:/LAND RATE/additional_land/samtse.csv")
df_samtse = df_samtse.iloc[:,1:]

df_sarpang = pd.read_csv("D:/LAND RATE/additional_land/sarpang.csv")
df_sarpang = df_sarpang.iloc[:,1:]

df_sjongkhar = pd.read_csv("D:/LAND RATE/additional_land/sjongkhar.csv")
df_sjongkhar = df_sjongkhar.iloc[:,1:]

df_tashigang = pd.read_csv("D:/LAND RATE/additional_land/tashigang.csv")
df_tashigang = df_tashigang.iloc[:,1:]

df_thim_thomde = pd.read_csv("D:/LAND RATE/additional_land/thim_thomde.csv")
df_thim_thomde = df_thim_thomde.iloc[:,1:]
# df_thim_thomde["BOB_2021_RATE"]=df_thim_thomde["BOB_2021_RATE"].astype(int)

df_trongsa = pd.read_csv("D:/LAND RATE/additional_land/trongsa.csv")
df_trongsa = df_trongsa.iloc[:,1:]

df_tyangtse = pd.read_csv("D:/LAND RATE/additional_land/tyangtse.csv")
df_tyangtse = df_tyangtse.iloc[:,1:]

df_wangdue = pd.read_csv("D:/LAND RATE/additional_land/wangdue.csv")
df_wangdue = df_wangdue.iloc[:,1:]

df_zhemgang = pd.read_csv("D:/LAND RATE/additional_land/zhemgang.csv")
df_zhemgang = df_zhemgang.iloc[:,1:]






a1, a2, a3,a4, a5 , a6= st.columns(6)
st.sidebar.image(img, width=100)
a5.button("MENU")
a6.button("LOG OUT")

rad = st.sidebar.radio("REGION SELECTION:", ["BUMTHANG","PARO","PHUNTSHOLING", "THIMPHU", "OTHERS"])

if rad == "THIMPHU":
    option = st.selectbox("SELECT THE LOCATION", ("THIMPHU THROMDE", "DEBSI","OUTSKIRT THIMPHU"))
    if option == "THIMPHU THROMDE":
        st.table(data = df_thim_thomde)

    if option == "DEBSI":
        st.table(data = df_debsi)

    if option == "OUTSKIRT THIMPHU":
        st.table(data = df_outskirt_thim)


if rad == "PHUNTSHOLING":
    option = st.selectbox("SELECT THE LOCATION", ("PLING TOWN", "KABREYTAR","PASAKHA", "PLING OUTSKIRT"))
    if option == "PLING TOWN":
        st.table(data = df_pling_town)

    if option == "KABREYTAR":
        st.table(data = df_karbreytar)

    if option == "PASAKHA":
        st.table(data = df_pasakha)

    if option == "PLING OUTSKIRT":
        st.table(data = df_pling_outskirt)


if rad == "OTHERS":
    option = st.selectbox("SELECT THE LOCATION",
                          ("DAGANA", "GASA", "HAA", "LHUENTSE", "PUNAKHA", "SAMTSE","SAMDRUPJONGKHAR", "SARPANG","TASHIGANG","TASHIYANGTSE","TRONGSA", "WANGDUE", "ZHEMGANG"))
    # st.write("you have selected:", option)
    if option == "DAGANA":
       # st.markdown("The details of land in Dagana:")
       st.table(df_dagana)

    if option == "HAA":
       # st.markdown("The details of land in Dagana:")
       st.table(df_haa)

    if option == "GASA":
        # st.markdown("The details of the land rate in Gasa:")
        st.table(df_gasa)
    if option == "LHUENTSE":
        # st.markdown("The details of the land rate in Lhuentse:")
        st.table(df_lhuentse)
    if option == "PUNAKHA":
        # st.markdown("The details of the land rate in Punakha:")
        st.table(df_punakha)
    if option == "SAMTSE":
        # st.markdown("The details of the land rate in Samtse:")
        st.table(df_samtse)
    if option == "SARPANG":
       # st.markdown("The details of land in Sarpang:")
       st.table(df_sarpang)
    if option == "TASHIGANG":
        # st.markdown("The details of the land rate in Tashigang:")
        st.table(df_tashigang)
    if option == "TRONGSA":
        # st.markdown("The details of the land rate in Trongsa:")
        st.table(df_trongsa)
    if option == "WANGDUE":
        # st.markdown("The details of the land rate in Wangdue:")
        st.table(df_wangdue)
    if option == "ZHEMGANG":
        # st.markdown("The details of the land rate in Zhemgang:")
        st.table(df_zhemgang)

    if option == "SAMDRUPJONGKHAR":
        # st.markdown("The details of the land rate in Samdrupjongkhar:")
        st.table(df_sjongkhar)
    if option == "TASHIYANGTSE":
        # st.markdown("The details of the land rate in Tashiyangtse:")
        st.table(df_tyangtse)


if rad == "BUMTHANG":
    st.table(data = df_bumthang)

if rad == "PARO":
    st.table(df_paro)
