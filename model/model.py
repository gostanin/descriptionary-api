import sys
import warnings

from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import numpy


warnings.filterwarnings("ignore")


def _load_model():
    return Word2Vec.load("model/word2vec.model")


def model_predict(description, top=1):
    if not top:
        top = 1
    description = simple_preprocess(description, deacc=True)
    model = _load_model()
    description = filter((lambda x: x in model.wv.vocab), description)
    return [word for word, similarity in model.most_similar(positive=description, topn=int(top))]
