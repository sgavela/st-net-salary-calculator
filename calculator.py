import streamlit as st

def calculate_net_salary(gross_salary):
    brackets = [
        (0, 12450, 0.19),
        (12450, 20199, 0.24),
        (20200, 35199, 0.30),
        (35200, 59999, 0.37),
        (60000, 299999, 0.45),
        (300000, float('inf'), 0.47)
    ]
    
    tax_paid = 0
    remaining_salary = gross_salary

    for lower, upper, rate in brackets:
        if remaining_salary > 0:
            taxable_amount = min(remaining_salary, upper - lower)
            tax_paid += taxable_amount * rate
            remaining_salary -= taxable_amount
        else:
            break

    net_salary = gross_salary - tax_paid
    return net_salary

st.title("Net Salary Calculator (Spain)")

gross_salary = st.number_input("Enter your gross salary (€):", min_value=0.0, step=100.0)

if st.button("Calculate Net Salary"):
    net_salary = calculate_net_salary(gross_salary)
    st.write(f"Your estimated net salary is: **{net_salary:.2f} €**")
