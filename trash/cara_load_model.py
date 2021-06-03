import pickle5 as pickle
from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences




saved_model = keras.models.load_model('./my_model.h5')

with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

# print(saved_model.summary())
# print(tokenizer.word_index)



new_sentence = ['']
new_sequences = tokenizer.texts_to_sequences(new_sentence)
new_padded = pad_sequences(new_sequences, maxlen=100, padding='post', truncating='post')

res = saved_model.predict(new_padded)
class_name = ['Seksual', 'Trafiking', 'Migran', 'Fisik', 'Psikis', 'Ekonomi']
print("Hasil Clasifikasi kasus  : {}".format(class_name[np.argmax(res)]))
print(res)
print(np.argmax(res))
print(class_name)