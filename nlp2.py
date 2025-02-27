# -*- coding: utf-8 -*-
"""NLP2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_pL0JueyelaFfJjKI3TtCQ48NJS6J-Pk

Слова "балетмейстер" и "концерт"
"""

import gensim
file = "drive/MyDrive/cbow.txt"
word2vec = gensim.models.KeyedVectors.load_word2vec_format(file, binary=False)

pos = ["выступление_NOUN", "опера_NOUN", "танцор_NOUN"]
neg = []

dist = word2vec.most_similar(positive=pos, negative = neg)
for i in dist:
    print(i)