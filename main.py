import streamlit as st
import pandas as pd
import numpy as np
import time
import datetime

def main():
    st.subheader("Example ChatBot")

    menu = ['HOME', 'EDA', "ML", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'HOME':
        st.subheader('HOME')
    elif choice == 'EDA':
        st.subheader('EDA')
    elif choice == 'ML':
        st.subheader('ML')
    else:
        st.subheader('About')

if __name__ == "__main__":
    main()