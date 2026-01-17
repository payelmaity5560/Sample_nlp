import streamlit as st
import nltk
import spacy
import string  
import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.stem import PorterStemmer,LancasterStemmer
from sklearn.feature_extraction.text import CountVectorizer

#Download NLTK Data
nltk.download("punkt")
nltk.download("stopwords")

#load spacy model
nlp = spacy.load("en_core_web_sm")

#streamlit page config
st.set_page_config(
    page_title="NLP preprocessing"
    layout="wide"
)

#app title
st.title("nlp processing app")
st.write("tokenization , text cleaning , steaming, lemmantization, and bag of words")

#user input
text =st.text_area("enter text for NLP processing ",height=150,
                   placeholder="example : yadav is the HOD of HIT and loves NLP")

#sidebar option
option =st.sidebar.radio(
    "select NLP tochnique",
    [
        "tokenization",
        " text cleaning" ,
         " steaming",
          " lemmantization",
           " bag of words"
    ]
)
#process button
if st.button("process text"):
    if text.strip()=="":
        st.warning("please enter same text,")


#Tokenization
    elif option== "tokenization":
        st.subheader("tokenization Output")
        col1,col2,col3 = st.columns(3)

        # sentence Tokenization
        with col1:
            st.markdown("### Sentence Tokenization")
            sentences = sent_tokenize(text)
            st.write(sentences)
        #  Word Tokenization 
        with col2:
            st.markdown("### Word Tokenization")
            words = word_tokenize(text)
            st.write(words) 

        #char tokenations
        with col3:
            st.markdown("### character Tokenization")
            characters = list(text)
            st.write(characters)
    elif option =="text cleaning":
        st.subheader("text cleaning output")

        #convert text to lower
        text_lower = text.lower()

        #remove punctuation & numbers
        cleaned_text = "".join(ch for ch in text_lower if ch not in string.punctuation and not ch.isdigit())

        #remove stopwords using spacy
        doc= nlp(cleaned_text)
        final_words =[ token.text for token in doc if not token.is_stop and token.text.strip() !=""]

        st.markdown("#### orignal text")
        st.write(text)


        st.markdown("### cleaned text")
        st.write(" ".join(final_words))

    #steaming
    elif option =="stemming":
        st.subheader("stemming output")

        words = word_tokenize(text)
        
        porter= PorterStemmer()
        lancaster = LancasterStemmer()


        #apply steaming
        porter_sem = [porter.stem(word) for words in words]
        Lancaster_stem = [ Lancaster_stem(word) for word in words]