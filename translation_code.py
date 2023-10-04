import spacy
from googletrans import Translator
import nltk 
import numpy as np
import pandas as pd


#nltk.download('punkt')



nlp = spacy.load("en_core_web_sm")
translator = Translator()


def translate_sentence(sentence):
    doc = nlp(sentence)
    translated_sentence = ""
    
    for token in doc:
        # Check if the token is a noun (using spaCy's part-of-speech tagging)
        if token.pos_ == "NOUN":
            # If it's a noun, add it as-is to the translated sentence
            translated_sentence += token.text + " "
        else:
            # If it's not a noun, try to translate it to Hindi
            try:
                translated_token = translator.translate(token.text, src="en", dest="hi")
                translated_sentence += translated_token.text + " "
            except Exception as e:
                print(f"Translation error for '{token.text}': {str(e)}")
                translated_sentence += token.text + " "  # Keep the original token

    return translated_sentence

# english_sentence = input("Enter an English sentence: ")
# translated_result = translate_sentence(english_sentence)
# print("Translated Sentence:", translated_result)




