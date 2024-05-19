import streamlit as st
from app.views import show_home_page, show_sub_page

PAGES = {"モデル作成": show_home_page, "モデル一覧": show_sub_page}


def main():
    st.write("Hoge")
    selected_page = st.sidebar.radio("Select Mode", list(PAGES.keys()))

    page = PAGES[selected_page]
    page()


if __name__ == "__main__":
    main()
