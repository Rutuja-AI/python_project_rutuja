import streamlit as st

email=st.text_input('Enter email:')
pass1=st.number_input('Enter password:')

btn=st.button('Login')

if btn:
    if email=='amangupta@gmail.com' and pass1==12345:

        st.balloons()
    else:
        st.error('Login Error')