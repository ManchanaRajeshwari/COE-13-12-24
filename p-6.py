import streamlit as st
salary=st.number_input("Enter your salary",min_value=1)
bill_1=st.number_input("Enter bill_1 amount")
bill_2=st.number_input("Enter bill_2 amount")
bill_3=st.number_input("ENter bill_3 amount")
total_bill=bill_1+bill_2+bill_3
st.info(f"The total bill is:{total_bill}")
percentage=(total_bill*100)/salary
st.success(f"The total percentage:{percentage}")
