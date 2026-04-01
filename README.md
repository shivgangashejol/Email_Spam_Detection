# Email_Spam_Detection
A machine learning project that classifies emails as Spam or Not Spam (Ham) using Natural Language Processing (NLP) and provides an interactive web interface using Streamlit.

## Overview
Email spam detection is an important application of machine learning in communication systems. This project builds a classification model trained on a public dataset and deploys it using a simple and interactive Streamlit web application.

## Features
- Text preprocessing (cleaning, tokenization, stopword removal)
- Feature extraction using TF-IDF
- Machine learning model for classification
- Interactive web interface using Streamlit
- Real-time prediction of email messages

## Streamlit App
The project includes a web application where users can input email text and check whether it is spam or not.

Run the Streamlit App
streamlit run app.py

Then open your browser at:
http://localhost:8501

## Dataset
Dataset sourced from GitHub
Contains labeled email messages:
- Spam
- Ham (Not Spam)

dataset link:
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

## Technologies Used
- Python
- NumPy
- Pandas
- Scikit-learn
- NLTK
- Streamlit

## Model Performance
- Accuracy - 97.67%
- Precision- 100%

## Future Improvements
- Use deep learning models such as LSTM or BERT
- Deploy the Streamlit app online
- Add file upload for bulk email classification
- Improve user interface

## Author
Shivganga Shejol
Email:shivgangashejol@gmail.com
LinkedIn: linkedin.com/in/shivgangashejol
