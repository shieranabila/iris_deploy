import streamlit as st

st.title("Hello, World!")
st.sidebar.header("dashboard")
st.text("selamat datang!!")
name = st.text_input("Masukkan nama Anda:")
if name:
    st.write(f"Halo, {name}!")


