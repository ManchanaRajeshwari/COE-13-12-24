import streamlit as st
st.title("Even or Odd")
num=st.number_input("Enter number",min_value=1,step=1)
if st.button("Even/Odd"):
    if num%2==0:
        st.success("Even number")
    else:
        st.error("Odd number")