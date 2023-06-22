import streamlit as st


st.header("Welcome to NAWE Intelligent Platform")
st.subheader("Please input all the information. We will create an account for you after our verification")

contact_form="""
<form action = "https://formsubmit.co/sumon@nawe.ae" method = "POST" >
    <input type = "text" name = "name" placeholder="Full Name" required >
    <input type = "text" name = "Organization Name" placeholder="Organization name" required >
    <input type = "email" name = "Company email" placeholder="Please provide your valid organization email" required >
    <button type = "submit" > Send </button >
    </form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

#use local CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)
local_css("style/style.css")

