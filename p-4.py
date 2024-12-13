import streamlit as st
project=st.number_input("Enter project score",min_value=0)
internal=st.number_input("Enter internal_score",min_value=0)
external=st.number_input("Enter external score",min_value=0)
if st.button("Evaluate the marks"):
   if(project >=50 and internal >=50 and external >=50):
      total=0
      total=(70*project)/100+(10*internal)/100+(20*external)/100
      if(total>=90):
         st.write("A grade")
      elif(total>80):
         st.write("B grade")
      else:
         st.write("C grade")
   else:
      if(project<50):
         st.write("Failed in project score:",project)
      if(internal< 50):
         st.write("Failed in internal score:",internal)
      if(external < 50):
         st.write("Failed in external score:",external)

