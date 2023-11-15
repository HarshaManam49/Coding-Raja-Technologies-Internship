import streamlit as st
import spacy,re
import numpy as np
import joblib

model=joblib.load('model.pkl')
nlp=spacy.load("en_core_web_lg")
comment_type=['Negative','Neutral','Positive']



def preprocess(text) :
  text=text.lower()
  text=re.sub(r'[^0-9a-z\s\n]','',text)
  doc=nlp(text)
  filtered_tokens=[]
  for token in doc :
    if token.is_stop or token.is_punct :
      continue
    else :
       filtered_tokens.append(token.lemma_)
  return '  '.join(filtered_tokens)
 
def cnvt2wordvectors(text):
  return nlp(text).vector


st.title('Sentiment Analysis on Social Media  Comments')
text= st.text_input('Enter comment')


if st.button("Predict") :
    text=preprocess(text)
    test=cnvt2wordvectors(text)
    test = np.expand_dims(test, axis = 0) 
    pred=model.predict(test)
    st.header(comment_type[pred[0]])

