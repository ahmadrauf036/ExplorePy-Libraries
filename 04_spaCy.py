import spacy
from spacy import displacy

nlp=spacy.load("en_core_web_sm")

doc=nlp("Ahmad is a good boy. i love ahmad.")

print(doc)

for token in doc:
    print(token.text)
