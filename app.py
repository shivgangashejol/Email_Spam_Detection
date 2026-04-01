import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
import sklearn

ps=PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    lst = []
    for i in text:
        if i.isalnum():
            lst.append(i)
    text = list(lst)
    lst.clear()
    for i in text:
        if i not in stopwords.words("english") and i not in string.punctuation:
            lst.append(i)
    text = lst[:]
    lst.clear()
    for i in text:
        lst.append(ps.stem(i))

    return " ".join(lst)



tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Prediction")

input_sms = st.text_area("Enter your email")

if st.button("Predict"):
    transformed_text = transform_text(input_sms)

    vector_input = tfidf.transform([transformed_text])

    result = model.predict(vector_input)

    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
