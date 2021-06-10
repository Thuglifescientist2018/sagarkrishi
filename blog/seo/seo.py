
from blog import seo
import nltk

seo_list = []
seo_tags = []


def metatagseo(content):
    content = content
    def is_noun(pos): return pos[:2] == 'NN'

    # do the nlp stuff
    tokenized = nltk.word_tokenize(content)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    for n in nouns:
        if len(n) >= 7:
            if not "/" in n:
                if n not in seo_list:
                    seo_list.append(n.lower())
    seo_tags = ', '.join(seo_list)

    return seo_tags


def description(content):
    desc = content[:250]
    return desc
