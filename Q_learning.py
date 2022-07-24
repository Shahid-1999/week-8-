import streamlit as st

num=st.number_input('Enter a number')

if num%2==0:
    st.write('Number is even')
else:
    st.write('Number is odd')