#NLTK-NLP The tutorial is an introduction to NLTK word tokenization
#WordTokenization with NLTK
import nltk
nltk.download('punkt_tab')
from nltk import word_tokenize
mys="Dua lipa was born in Kosovo"
print(word_tokenize(mys))
