import streamlit as st
from app.services import HomePageService


def show_home_page():
    st.title("Home")
    area_id = st.text_input("エリアID")
    measure_value = st.number_input("計測値", step=0.1, value=2.0)

    if st.button("Save"):
        HomePageService.save_measure(area_id=area_id, measure_value=measure_value)

    if st.button("Get Latest"):
        HomePageService.get_latest()
