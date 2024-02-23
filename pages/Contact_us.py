import streamlit as st
import send_email


with st.form(key="Email_form"):
    st.title("Contact Us")
    user_name = st.text_input("Enter your Email")
    user_msg = st.text_area("Describe your problem")
    message = f"""\
    Subject: from{user_name}
    
    {user_msg}
    from {user_name}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email.send_mai(message)
        st.info("Your message was sent successfully..")
