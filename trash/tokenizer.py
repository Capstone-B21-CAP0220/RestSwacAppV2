import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
    'I love my dog',
    'I love my cat'
]

tokenizer = Tokenizer(num_words=100)
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print("Word Index")

print(word_index)

sequences = tokenizer.texts_to_sequences(sentences)
print("Sequences")
print(sequences)

sentences_test = [
    'I love my live',
    'cat live outside',
    'what the fuck are you doing'
]

print("Kelemahan Sequences tanpa oov")

sequences_with_test_data = tokenizer.texts_to_sequences(sentences_test)
print(sequences_with_test_data)
print('Seperti yang kita lihat kata live tidak ada dalam kamus sehingga jumlah sequences berkurang, bisa ditangani dengan oov token')

tokenizer2 = Tokenizer(num_words=100, oov_token="<OOV>")
tokenizer2.fit_on_texts(sentences)
word_index = tokenizer2.word_index

sequences = tokenizer2.texts_to_sequences(sentences)

sequences_with_test_data = tokenizer2.texts_to_sequences(sentences_test)

print('Tokenizer nya with oov')
print(word_index)
print(sequences)
print(sequences_with_test_data)


print('To handle diverent length use pad sequence')
padded = pad_sequences(sequences_with_test_data)
print(padded)

# 0 = padding
# 1 = oov