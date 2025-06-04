# maslahat.py

import streamlit as st

def maslahat_ber(yosh):
    if yosh < 7:
        return "Siz hali juda yoshsiz. Ko‘proq o‘yin o‘ynang va ertaklar o‘qing!"
    elif yosh < 14:
        return "Matematika va ingliz tilini chuqur o‘rganing!"
    elif yosh < 20:
        return "IT va dasturlashni o‘rganing, hoziroq boshlang!"
    elif yosh < 30:
        return "Karyera, biznes, yoki universitet haqida o‘ylang."
    else:
        return "Yoshlarga maslahat bering va tajriba ulashing 🙂"

st.title("🧠 AI Maslahat Ilovasi")
yosh = st.number_input("Yoshingizni kiriting:", min_value=1, max_value=100, step=1)

if st.button("Maslahat olish"):
    natija = maslahat_ber(yosh)
    st.success(natija)
