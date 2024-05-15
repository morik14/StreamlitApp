import streamlit as st
from presentation import show_home, show_sub

PAGES = {"モデル作成": show_home, "モデル一覧": show_sub}


def main():
    st.write("Hoge")
    selected_page = st.sidebar.radio("Select Mode", list(PAGES.keys()))

    page = PAGES[selected_page]
    page()


if __name__ == "__main__":
    main()
