#-----------------BMI Caluculator
# import
import streamlit as st

# main title or description
st.title("BMI Calculator ")
st.write("Calculate your BMI to check if you're at a healthy weight.")

# input field banany k liy cols bannay
col1, col2 = st.columns(2)

# col1 weight k liy
with col1:
    weight = st.number_input("Enter your weight (kg)", 30.0, 300.0, 70.0, 0.1)
# col2 height k liy  
with col2:
    height = st.number_input("Enter your height (cm)", 100.0, 250.0, 170.0, 0.1)

# bmi calculation k liy button
if st.button("Calculate BMI"):
    height_m = height / 100
# calculation formula 
    bmi = weight / (height_m ** 2)
#result show krny k liy
    st.write("### Your BMI is:", round(bmi, 2))
#conditions   
    if bmi < 18.5:
        st.warning("You are Underweight")
    elif 18.5 <= bmi < 25:
        st.success("You are at a Healthy Weight")
    elif 25 <= bmi < 30:
        st.warning("You are Overweight")
    else:
        st.error("You are Obese")
# categories   
    st.write("### BMI Categories:")
    st.write("""
| Category | BMI Range |
|----------|-----------|
| Underweight | < 18.5 |
| Healthy Weight | 18.5 - 24.9 |
| Overweight | 25 - 29.9 |
| Obese | ≥ 30 |
""")
# expander bmi se related info k liy use hota h
with st.expander("What is BMI?"):
    st.write("""
    Body Mass Index (BMI) is a simple measure that uses your height and weight to work out if your weight is healthy.
    
    **BMI Limitations:**
    - BMI doesn't account for muscle mass
    - BMI doesn't account for where fat is stored in the body
    - BMI may not be accurate for elderly people or children
    """)
