import spacy
from spacy import displacy

nlp=spacy.load("en_core_web_lg")

# doc=nlp("search ahmad")
# print(type(doc))

# print(doc)

# for token in doc:
#     print(token.text,token.lemma_,token.pos_,token.dep_,token.head)

# for ent in doc.ents:
#     print(ent.text,ent.label_)

# for sent in doc.sents:
    # print(sent.text)

# extracting name from above

# for ent in doc.ents:
#     if(ent.label_=='PERSON'):
#         print(ent.text)

# doc1 = nlp("I love pizza")
# doc2 = nlp("I like pizza")
# print(doc1.similarity(doc2))    # 0.0-1.0

app_keys={
    "google":["browser","web","web browser","google","chrome"],
    "notepad":["note","notes","writing tool"],
    "calc":["calculation","calculations","addition","subtraction","multiplication","division"],
}
def identify_keywords(input:str):
    
    doc=nlp(input)
    userDemand=0
    for i in input:
        if i.lower()=="open" or i.lower()=="search":
            userDemand+=1
    srch=""
    chk=0
    for token in doc:
        for k in app_keys:
            if token.lemma_ in app_keys[k]:
                if token.lemma_=='google':
                    if userDemand==2:
                        c=0
                        for t in doc:
                            if t.text=='search':
                                pass 
                    else:
                        pass #open google
                elif token.lemma_=="calc":
                    pass # open calculator
                elif token.lemma_=="notepad":
                    pass #open notepad
            
            
    return 1

identify_keywords("open web")