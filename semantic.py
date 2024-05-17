import spacy
nlp = spacy.load('en_core_web_sm')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

1. 0.5929929675536907: This value represents the similarity score between the words “cat” and “monkey.” It indicates how similar their meanings are based on their word vectors or embeddings. A higher score suggests greater similarity.
2. 0.40415016164997786: Here, we have the similarity score between “banana” and “monkey.” Again, this value reflects the semantic similarity between these two words.
3. 0.22358825939615987: Lastly, this score represents the similarity between “banana” and “cat.”

# There are higher values between cat and monkey than there are between monkey and banana. This would indicate that SpaCy understands closer similarities in the classification of animals than the food the animal eats

# An example I would suggest is : 
word4 = nlp("moon")
word5 = nlp("star")
word6 = nlp("white")
print(word5.similarity(word4))
print(word6.similarity(word5))
print(word6.similarity(word4))

# It seems the simpler language model 'en_core_web_sm' uses no word vectors loaded so the doc. similarity method is just using the tagger, parser and ner methods. 

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
        
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(f"{sentence} - {similarity:.4f}") # converting the float value to a string before concatenating it