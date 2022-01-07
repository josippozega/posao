import streamlit as st
import requests


def main():
    menu = ["Početna", "O Aplikaciji"]
    choice = st.sidebar.selectbox("Menu", menu)

    st.title("App za traženje posla, dev bj Josip Požega")

    if choice =="Početna":
        st.subheader("Početna")


    else:
        st.subheader("O Aplikaciji")




if __name__ == '__main__':
   main()
