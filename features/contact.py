import streamlit as st

def run():
    st.title("📞 Contact Us")
    st.write("Feel free to reach out through the contact form below.")

    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button("Send"):
        if name and email and message:
            st.success(f"Thank you {name}, we received your message!")
        else:
            st.error("Please fill out all fields.")
