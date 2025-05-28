import streamlit as st

st.title("Hello, World!")
st.sidebar.header("dashboard")
name = st.text_input("Masukkan nama Anda:")
if name:
    st.write(f"Halo, {name}!")


