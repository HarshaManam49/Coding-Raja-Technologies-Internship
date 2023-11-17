# Coding-Raja-Technologies-Internship
## 1)Classification of Indian Food Classification using Pretrained models
#### Description
>Classifies Indian Food Image to 20 categories of indian food
#### Workflow
>1)Loaded images from folders using tf.data.Dataset pipeline.  
>2)Rescaled images into desired format.  
>3)Builted data augmentation sequential model for better generalization of classification model.  
>3)Dowloaded the pretrained Resent50 model with imagenet weights.  
>4)Added data augmentation and  classifier neural network layer on top of resnet50 model.  
>5)Fine tuned  model on our dataset.  
>6)Evaluated on test data.  
>7)Model is saved in .keras extension which can be loaded and can be trained further.

##### Tech Stack<br> 
>Tensorflow  
>Keras       
>Matplotlib  
>Numpy

Data set link <https://www.kaggle.com/datasets/l33tc0d3r/indian-food-classification>

## 2)Sentiment Analysis of Social Media Comments
#### Description
>Classifies  social media comment into negitive, neutral or positive categories.  
#### Workflow 
>1)Prepocessed data by removing stopwords, punctuations and coverted into it base word using lemmatization.    
>2)Using spacy word vectors conveted text data into Word Embeddings.    
>3)Various Ml and Deep neural networks are trained.  
>4)Performed various evaluation metrics like precession,recall,f1 score,accuracy  to select best model.       
>5)Best model is saved and deployed using steamlit.  
##### Tech Stack<br>
>Spacy library  
>Tensorflow  
>Keras     
>Streamlit  
>Pandas  
>Matplotlib  
 
To use webapp, download zip and run below commands  
>1)'pip install -r requirements.txt' to install required libraries  
>2)'streamlit run app.py' to host application in local host

Data set link <https://www.kaggle.com/datasets/abhi8923shriv/sentiment-analysis-dataset> <br>
