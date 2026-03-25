import streamlit as st

st.title("mon premiére app streamlit🚀 ")
st.write("bonjour depuis tunisie freelance")

nom = st.text_input("quel est ton prenom?")

if nom:
    st.success(f"Bienvenue {nom} ! 🎉")
