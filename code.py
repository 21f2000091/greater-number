import streamlit as st 
num=st.number_input("Enter first number")
num2=st.number_input("Enter second number")
num3=st.number_input("Enter third number")
m=max(num1,num2,num3)
st.write(m)
