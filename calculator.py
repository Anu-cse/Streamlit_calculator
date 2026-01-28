import streamlit as st 
st.title("Calculator App")
num1=st.number_input("Enter first number:", value=16)
num2=st.number_input("Enter second number:",value=16)
operations=st.selectbox("choose operation",["add","sub","multiply","divide"])
if operations == "add":
    result = num1+num2
elif operations == "sub":
    result = num1-num2
elif operations == "multiply":
    result = num1*num2
elif operations == "divide":
    result = num1/num2
else:
    result = "zero division error"
print("RESULT:",result)
 