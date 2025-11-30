# ==========================
# Web Calculator using Streamlit
# ==========================

import streamlit as st

# Define calculation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

# Streamlit app
def main():
    # App title
    st.title("Simple Calculator !!")

    st.write("This is a beginner-friendly calculator built with Python & Streamlit.")

    # Take number inputs from user
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    # Operator selection (dropdown)
    operation = st.selectbox(
        "Select operation",
        ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]
    )

    # Button to perform calculation
    if st.button("Calculate"):
        # Map selected text to actual operation
        if operation.startswith("Addition"):
            result = add(num1, num2)
            op_symbol = "+"
        elif operation.startswith("Subtraction"):
            result = subtract(num1, num2)
            op_symbol = "-"
        elif operation.startswith("Multiplication"):
            result = multiply(num1, num2)
            op_symbol = "*"
        else:
            result = divide(num1, num2)
            op_symbol = "/"

        # Display result
        st.success(f"Result: {num1} {op_symbol} {num2} = {result}")


if __name__ == "__main__":
    main()




# streamlit run cal_streamlit.py
