import streamlit as st

def main():
    st.title("Simple Streamlit App")
    
    # Create a form
    with st.form("user_form"):
        name = st.text_input("Enter your name:")
        age = st.number_input("Enter your age:", min_value=0, step=1)
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            st.success(f"Hello, {name}! You are {age} years old.")

if __name__ == "__main__":
    main()
