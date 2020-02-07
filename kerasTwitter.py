# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:43:36 2020

@author: Ali
"""
import pandas as pd
import numpy as np
import re
import string
import gensim
import scipy
import matplotlib.pyplot as plt
import pickle
import time


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfVectorizer
# Keras
print(scipy.__version__)

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout, Embedding, Flatten, Conv1D, MaxPooling1D, LSTM
from keras import utils
from keras.callbacks import ReduceLROnPlateau, EarlyStopping



decode_map = {0: "NEGATIVE", 2: "NEUTRAL", 4: "POSITIVE"}
def decode_sentiment(label):
    return decode_map[int(label)]

def remove_pattern(input_txt, userpattern,RTpattern):
    r = re.findall(userpattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
    RT = re.findall(RTpattern, input_txt)
    for i in RT:
        input_txt = re.sub(i, '', input_txt)        
        
    return input_txt

def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text

def decode_sentimental(score, include_neutral=True):
    if include_neutral:        
        label = NEUTRAL
        if score <= SENTIMENT_THRESHOLDS[0]:
            label = NEGATIVE
        elif score >= SENTIMENT_THRESHOLDS[1]:
            label = POSITIVE

        return label
    else:
        return NEGATIVE if score < 0.5 else POSITIVE
    
def predict(text, include_neutral=True):
    start_at = time.time()
    # Tokenize text
    x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=SEQUENCE_LENGTH)
    # Predict
    score = model.predict([x_test])[0]
    # Decode sentiment
    label = decode_sentimental(score, include_neutral=include_neutral)

    return {"label": label, "score": float(score),
       "elapsed_time": time.time()-start_at} 

sent140filepath='C:/Users/Ali/Desktop/Twitter Project/sentiment140.csv'

sent140_columns=['target','ids','date','flag','user','text']
DATASET_ENCODING = "ISO-8859-1"
userpattern="@[\w]*"
RTpattern="RT"
TRAIN_SIZE = 0.8

# KERAS
SEQUENCE_LENGTH = 300
EPOCHS = 8
BATCH_SIZE = 1024

# SENTIMENT
POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
NEUTRAL = "NEUTRAL"
SENTIMENT_THRESHOLDS = (0.4, 0.7)

# WORD2VEC 
W2V_SIZE = 300
W2V_WINDOW = 7
W2V_EPOCH = 32
W2V_MIN_COUNT = 10

#Model Names
WORD2VEC_MODEL = "140sent_w2v_model.w2v"
keras_MODEL = "LSTM_sentiment_model.h5"
TOKENIZER_MODEL = "tokenizer.pkl"
ENCODER_MODEL = "encoder.pkl"


df140=pd.read_csv(sent140filepath,encoding =DATASET_ENCODING,names=sent140_columns)
df140['sentiment']= df140.target.apply(lambda x: decode_sentiment(x))


df140_train, df140_test = train_test_split(df140, test_size=1-TRAIN_SIZE, random_state=42)

df140_train['tidy_text'] = np.vectorize(remove_pattern)(df140_train['text'], userpattern,RTpattern)

#Remove Punctuation
df140_train['tidy_text'] = df140_train['tidy_text'].apply(lambda x: remove_punct(x))


documents = [_text.split() for _text in df140_train.tidy_text]



w2v_model = gensim.models.word2vec.Word2Vec(size=W2V_SIZE, 
                                            window=W2V_WINDOW, 
                                            min_count=W2V_MIN_COUNT, 
                                            workers=8)
w2v_model.build_vocab(documents)

words = w2v_model.wv.vocab.keys()
vocab_size = len(words)

w2v_model.train(documents, total_examples=len(documents), epochs=W2V_EPOCH)


w1=['love']
print(w2v_model.wv.most_similar(positive=w1))

#save w2v model
w2v_model.save(WORD2VEC_MODEL)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(df140_train.tidy_text)

vocab_size = len(tokenizer.word_index) + 1
print("Total words", vocab_size)

x_train = pad_sequences(tokenizer.texts_to_sequences(df140_train.tidy_text), maxlen=SEQUENCE_LENGTH)
x_test = pad_sequences(tokenizer.texts_to_sequences(df140_test.text), maxlen=SEQUENCE_LENGTH)


labels = df140_train.target.unique().tolist()
labels.append(NEUTRAL)

encoder = LabelEncoder()
encoder.fit(df140_train.target.tolist())

y_train = encoder.transform(df140_train.target.tolist())
y_test = encoder.transform(df140_test.target.tolist())

y_train = y_train.reshape(-1,1)
y_test = y_test.reshape(-1,1)

print("y_train",y_train.shape)
print("y_test",y_test.shape)

# Embedding Layer
embedding_matrix = np.zeros((vocab_size, W2V_SIZE))
for word, i in tokenizer.word_index.items():
  if word in w2v_model.wv:
    embedding_matrix[i] = w2v_model.wv[word]
print(embedding_matrix.shape)

embedding_layer = Embedding(vocab_size, W2V_SIZE, weights=[embedding_matrix], input_length=SEQUENCE_LENGTH, trainable=False)

#Keras LSTM Model
model = Sequential()
model.add(embedding_layer)
model.add(Dropout(0.5))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))

#Compile model

model.compile(loss='binary_crossentropy',
              optimizer="adam",
              metrics=['accuracy'])

callbacks = [ ReduceLROnPlateau(monitor='val_loss', patience=5, cooldown=0),
              EarlyStopping(monitor='val_acc', min_delta=1e-4, patience=5)]

history = model.fit(x_train, y_train,
                    batch_size=BATCH_SIZE,
                    epochs=EPOCHS,
                    validation_split=0.1,
                    verbose=1,
                    callbacks=callbacks)

#Evaluate
score = model.evaluate(x_test, y_test, batch_size=BATCH_SIZE)
print()
print("ACCURACY:",score[1])
print("LOSS:",score[0])

#Model Evaluation Viz.

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
 
epochs = range(len(acc))
 
plt.plot(epochs, acc, 'b', label='Training acc')
plt.plot(epochs, val_acc, 'r', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()
 
plt.figure()
 
plt.plot(epochs, loss, 'b', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
 
plt.show()



predict("I love the music")

#Save Models
model.save(keras_MODEL)
w2v_model.save(WORD2VEC_MODEL)
pickle.dump(tokenizer, open(TOKENIZER_MODEL, "wb"), protocol=0)
pickle.dump(encoder, open(ENCODER_MODEL, "wb"), protocol=0)



print(labels)



print(df140.head())
