import streamlit as st
import requests

base_url="https://remotive.io/api/remote-jobs"

def get_data(url):
    resp = requests.get(url)
    return resp.json()


def main():
    menu = ["Početna", "O Aplikaciji"]
    choice = st.sidebar.selectbox("Menu", menu)

    st.title("App za traženje posla")
    st.subheader("dev by Josip Požega")

    if choice =="Početna":
        st.subheader("Početna")
        
        with st.form(key='searchform'):
            nav1, nav2, nav3 = st.columns([3,2,1])
            
            with nav1:
                search_term = st.selectbox("Koji posao želiš?")
            with nav2:
                location = st.text_input("Na kojoj lokaciji?")
            with nav3: 
                st.text=("Traži")
                submit_search = st.form_submit_button(label='Traži ')
         
        st.success=("Tražili ste {} u {}".format(search_term,location))


    else:
        st.subheader("O Aplikaciji")




if __name__ == '__main__':
   main()
