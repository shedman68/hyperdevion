import spacy 

nlp = spacy.load('en_core_web_sm')

# Example garden-path sentences
gardenpathSentences = [
    "The old man the boat.",
    "The complex houses married and single soldiers and their families."
]

# adding to list
gardenpathSentences.append("Mary gave the child a Band-Aid.")
gardenpathSentences.append("That Jill is never here hurts.")
gardenpathSentences.append("The cotton clothing is made of grows in Mississippi.")


for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print(f"Original Sentence: {sentence}")
    print("Tokens:")
    for token in doc:
        print(f"{token.text} ({token.pos_})")

    print("Named Entities:")
    for ent in doc.ents:
        print(f"{ent.text} ({ent.label_})")
    print("-" * 40)

# Print explanations for entity labels
print("Explanation of Entity Labels:")
for label in set([ent.label_ for ent in doc.ents]):
    print(f"{label}: {spacy.explain(label)}")

## Entity: “Mary”
#Explanation: The label for this entity is PERSON. It represents people, including fictional characters.
#Sense: Given that “Mary” is a common name associated with individuals, the label makes sense in terms of the word.
#Entity: “Mississippi”
#Explanation: The label for this entity is GPE (Geopolitical Entity). It refers to countries, cities, states, or other political divisions.
#Sense: “Mississippi” is a state in the United States, so the label aligns well with the word.