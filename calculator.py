import streamlit as st

st.title("🧮 Simple Calculator")

# Ask for numbers
num1 = st.number_input("Enter first number", step=1.0)
num2 = st.number_input("Enter second number", step=1.0)

# Ask for operation
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

# Button to calculate
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"

    # 👉 Output appears right below the question
    st.success(f"Result: {result}")

