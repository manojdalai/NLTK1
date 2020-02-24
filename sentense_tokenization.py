#import nltk
#nltk.download()
import nltk.data
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
para = "Hello World. It's good to see you. Thanks for buying this book can't isn't."
print(sent_tokenize(para))


tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
print(tokenizer.tokenize(para))
print(word_tokenize(para))

#tokenizer = PunktWordTokenizer()
#tokenizer.tokenize(para)





