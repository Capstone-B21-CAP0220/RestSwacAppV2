import pickle5 as pickle
from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences


saved_model = keras.models.load_model('../my_model.h5')

with open('../tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

# print(saved_model.summary())
# print(tokenizer.word_index)



new_sentence = ['Satu minggu yang lalu saya mengunjungi rumah kakek saya, lokasinya lumaya jauh dari rumah saya, namun ketika telah sampai dirumahnya saya kakek saya tidak ada dan hanya ada paman saya, paman saya juga tinggal bersama kakek saya, ketika saya tanya ternyata kakek saya sedang ada keperluan diluar dan mungkin akan lama kata paman saya, akhirnya saya duduk di kursi dengan main hp sembari beristirahat, disaat saya sedang main hp paman saya melihat gerak gerik yang mencurigakan, saya mulai khawatir, akhirnya saya memutuskan untuk pulang dan setelah saya mau keluar tiba-tiba pintu rumah kakek saya ditutup dikunci dan saya mulai takut, paman langsung memeluk dan memeras payudara saya dan menarik paksa saya ke kamar hingga tangan saya memar namun saya mencoba teriak namun mulut saya dibekap dan ditampar hingga dipukul, karena dan saat itu diancam akan dibunuh maka saya hanya bisa pasrah untuk memenuhi hasrat dia untuk berhubungan intim hingga kemaluan saya berdarah dan saya hanya bisa menangis pada saat itu. Mohon tolong saya']
new_sequences = tokenizer.texts_to_sequences(new_sentence)
new_padded = pad_sequences(new_sequences, maxlen=100, padding='post', truncating='post')

res = saved_model.predict(new_padded)
class_name = ['Seksual', 'Trafiking', 'Migran', 'Fisik', 'Psikis', 'Ekonomi']
print("Hasil Clasifikasi kasus  : {}".format(class_name[np.argmax(res)]))
prediksi = res[0]
print(res[0])
print(prediksi)
print(np.argmax(prediksi[1:]))
print(class_name)