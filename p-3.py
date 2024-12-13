import streamlit as st
st.title("Gross Salary Calculator")
basic_salary=st.number_input("enter basic salary",min_value=0)
if st.button("Calculate gross salary"):
  hra=0
  da=0
  if(basic_salary<10000):
    hra=(67*basic_salary)/100
    da=(73*basic_salary)/100
  elif(10000<=basic_salary<=20000):
    hra = (69*basic_salary)/100
    da=(76*basic_salary)/100
  else:
    hra = (73*basic_salary)/100
    da=(89*basic_salary)/100
  gs=hra+da+basic_salary
  st.info(f"Basic salary: {basic_salary:,.2f}")
  st.info(f"HRA:{hra:,.2f}")
  st.info(f"DA:{da:,.2f}")
  st.success(f"The gross_salary is:{gs:,.2f}")