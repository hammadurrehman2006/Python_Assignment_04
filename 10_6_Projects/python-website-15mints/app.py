#----------------PYTHON WEBSITE
import streamlit as st
from datetime import datetime

# title
st.title("Welcome to My Simple Website! 👋")

# sidebar
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "About", "Contact"])

if page == "Home":
    st.header("Home Page")
    st.write("This is a simple website created with Streamlit!")
    
# content
    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello, {name}! 👋")
    
# simple button
    if st.button("Click me!"):
        st.write("Button clicked! 🎉")

elif page == "About":
    st.header("About Us")
    st.write("This is a demo website created using Python and Streamlit.")
    
# 2 columns
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Our Features")
        st.write("✨ Easy to use")
        st.write("🚀 Fast development")
        st.write("📱 Mobile-friendly")
    
    with col2:
        st.subheader("Technologies")
        st.write("🐍 Python")
        st.write("📊 Streamlit")
        st.write("🎨 HTML/CSS")

else:
    st.header("Contact Us")
    
# simple contact form
    contact_form = st.form("contact_form")
    email = contact_form.text_input("Your Email")
    message = contact_form.text_area("Your Message")
    submit = contact_form.form_submit_button("Send Message")
    
    if submit:
        st.success("Thank you for your message! We'll get back to you soon.")
