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

# Convert each text into a list of word ids
seq= tokenizer.texts_to_sequences(texts)

# Pad with zeros so all sequences have the same length
X= pad_sequences(seq)
y= np.array(labels)

# +1 because id 0 is reserved for padding
vocab_size= len(tokenizer.word_index)+1

print('training data shape --', X.shape)



# Model: Embedding -> SimpleRNN -> Dense(sigmoid)
model= Sequential([
    # Embedding: learn an 8-dimensional vector for every word
    Embedding(vocab_size, 8, input_length=X.shape[1]),
    # SimpleRNN: reads the sequence word by word and keeps a 16-unit hidden state
    SimpleRNN(16),
    # One sigmoid neuron: probability that the message is spam
    Dense(1, activation='sigmoid')
])

# Binary cross-entropy for a 2-class problem; Adam optimiser
model.compile( 
    optimizer='adam',
    loss= 'binary_crossentropy',
    metrics=['accuracy']

)

# Train for 40 epochs
model.fit(X, y, epochs= 40, verbose=1)

# Try an unseen message: reuse the same tokenizer and pad to the training length
test_text= ['win money now using lottery ']

test_seq= tokenizer.texts_to_sequences(test_text)
test_pad= pad_sequences(test_seq, maxlen= X.shape[1])
