import streamlit as st
from model import autocorrect

st.set_page_config(page_title="NLP Autocorrect", page_icon="📚")

st.title("📚 NLP Auto Suggestion App ")

user_input = st.text_input("Enter a word:")

st.button("suggest")

if user_input:
    results = autocorrect(user_input)

    st.subheader("Suggestions:")

    for word, similarity, probability in results:
        st.write(
            f"Word: {word} | Similarity: {round(similarity*100,2)}% | Probability: {round(probability*100,4)}"
        )
