sentence = [
    "granny starting to fear spiders in the graden might be real",
    "the weather today is bright and sunny"
]

sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

print(model.predict)