# Spam classifier using a Recurrent Neural Network (SimpleRNN).
#
# Pipeline: text -> integer sequences -> padding -> Embedding -> SimpleRNN -> sigmoid.
# An RNN reads a sentence word by word and keeps a hidden state (memory) of what it has seen,
# which makes it suitable for sequence data such as text.
# (The original folder was named 'LSTM', but this script uses SimpleRNN; an LSTM is a more
# powerful variant that handles long-range dependencies better - see
# 02_keras_regression_and_classification_labs/06_stock_price_prediction_linear_and_lstm.ipynb.)
#
# Run: python rnn_text_spam_classifier.py     Requires: tensorflow

import numpy as np 
import tensorflow as tf
from  tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense , Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Tiny toy dataset: 2 spam messages and 2 normal messages
texts=['win money now',
       'claim your prize',
       'meeting tomorrow',
       'project discusssion']

# 1 = spam, 0 = not spam
labels=[1,1,0,0]
# Tokenizer maps every word to an integer id
tokenizer= Tokenizer()
# Build the vocabulary from the training texts
tokenizer.fit_on_texts(texts)
