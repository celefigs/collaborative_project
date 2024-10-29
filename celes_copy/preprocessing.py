import nltk
from nltk.corpus import stopwords
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer



REPLACE_NO_SPACE = re.compile(r"[.;:!#\'?,\"()\[\]&]|\d+")  # delete punctuation and numbers
REPLACE_WITH_SPACE = re.compile(r"(<br\s*/><br\s*/>)|(\-)|(\/)") 


stop_words = set(stopwords.words('english'))

def preprocess_review(reviews):

    # Remove special characters
    reviews = re.sub(REPLACE_NO_SPACE, "", reviews)  #aqui tambien podemos usar RegexpTokenizer()
    reviews = re.sub(REPLACE_WITH_SPACE, " ", reviews)

    tokens = word_tokenize(reviews)

    # Lowercase and lemmatize
    lemmatizer = WordNetLemmatizer()

    lemmas = [lemmatizer.lemmatize(token.lower(), pos='v') for token in tokens if token.lower() not in stop_words]
    lemmas = [lemmatizer.lemmatize(token.lower(), pos='n') for token in lemmas if token.lower() not in stop_words]


    return lemmas