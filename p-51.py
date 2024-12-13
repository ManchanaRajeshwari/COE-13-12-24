import streamlit as st
class Bank:
    acbal=10000
    def deposit(self):
        d_amount=st.number_input("Enter deposit amount",key="d_amount")
        if st.button("Checking deposite or not"):
           if (d_amount>100):
               st.write("Accepted deposit as you entered amount is >100")
               if(d_amount<=50000):
                   st.write("Accepted deposit as You entered amount is below 50k")
               elif(d_amount%100)==0:
                   st.write("Accepted deposit as You entered amount is multiples of 100")
               else:
                   st.write("amount is >50k or not the multiples of 100")
           else:
               st.write("amount is less than 100")
    def withdraw(self):
      if(self.acbal>500):
        w_amount=st.number_input("Enter withdraw amount",key="w_amount")
        if st.button("Checking withdrawl or not"):
           if(w_amount>100):
              st.write("Accepted withdrawl as you entered w_amount is >100")
              if(w_amount< self.acbal):
                st.write("Accepted withdrawl as you entered w_amount is <accbal")
              elif(w_amount%100)==0:
                st.write("Accepted withdrawl as you entered w_amount is multiples of 100")
              else:
                st.write("You entered amount is amount is >balance or not multiples of 100")
           else:
               st.write("Min  balance is 500 not able to execute")
           string=st.text_input("Do you want transaction say yes/no",key="stri")
           if st.button("Check Transaction weather necessary or not"):
            if(string=="yes"):
               for i in range(3):
                  transac_amount=st.number_input("Enter transaction amount",key="transac")
                  if (transac_amount == 20000):
                     st.write("You can proceed")
                  else:
                     st.write("Unable to do transaction as amount is less than 20K")
               else:
                   st.write("You exceeded transaction limit")
            else:
                st.write("Continue..")
    def display(self):
     # while(True):
        st.write("1.Deposit")
        st.write("2.Withdraw")
        st.write("3.Balance Enquiry")
        st.write("4.Exit")
        st.write("Choose your option")
        option=st.number_input("Enter your option",key="unique_1")
        if(option==1):
            obj.deposit()
        elif(option==2):
            obj.withdraw()
        else:
            exit(0)
    def validate(self):
           st.title("Welcome to ABC bank")
           pin_num = st.number_input("Enter pin number",key="unique_2")
           if (pin_num==1234):
             obj.display()
           else:
               st.write("You entered pin is wrong")
obj=Bank()
obj.validate()


