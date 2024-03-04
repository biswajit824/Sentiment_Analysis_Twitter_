import streamlit as st
import pickle
import time

st.title("Twitter Sentiment Analysis")

#load model
model = pickle.load(open('twitter_sentiment.pkl', 'rb'))

tweet = st.text_input("Enter your tweet")

sumbit = st.button("Predict")

if sumbit:
    start = time.time()
    prediction = model.predict([tweet])
    print(prediction[0])
    st.write("Prediction Sentiment is:-  ", prediction[0])
    end = time.time()
    st.write("Prediction time taken:-  ", round(end-start, 2), "seconds")