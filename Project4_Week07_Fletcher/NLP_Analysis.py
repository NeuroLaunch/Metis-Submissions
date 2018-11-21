#!/usr/bin/env python3
"""Utility functions to tokenize and model text.

For Metis Weeks 7-8, Project Fletcher.

@author: Steven Bierer
Created on Wed Nov 14, 2018
"""

import pandas as pd
from scipy.sparse import lil_matrix
from nltk.corpus import wordnet
from gensim import corpora

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

def tokenize(text, nlp, stopwords, accept_tags=['NOUN','VERB','ORG']):
    """ Tokenize items in list 'text', suitable for news articles. """
    doc_tokens = []
    
    WNPOS = {'NOUN':wordnet.NOUN, 'VERB':wordnet.VERB,
             'ADJ':wordnet.ADJ, 'ADV':wordnet.ADV}
    
    # First get generic words and keep ones with desired parts of speech #
    tokens = nlp(text.lower())  # nlp() = standard SpaCy processing tool
    for token in tokens:
        if token.orth_.isspace() or token.like_url:
            continue
        if (token.pos_ in accept_tags) and (token.text not in stopwords):
            lemma = wordnet.morphy(token.text, WNPOS[token.pos_])
            if lemma:
                doc_tokens.append(lemma)

    # Then get named entities, folding monetary + pct values into categories #
    tokens = nlp(text)
    for entity in tokens.ents:
#        print(entity, len(entity),entity.label_)
        if entity.label_ in accept_tags:
            doc_tokens.append(entity.text.upper())
        elif entity.label_=='PERCENT':
            doc_tokens.append('PERCENT')
        elif entity.label_=='MONEY':
            doc_tokens.append('MONEY')
    
    return doc_tokens
# end tokenize()

def make_dictionary(documents, nlp, stopwords, accept_tags):
    """ From list of documents, vectorize tokens for LDA analysis. """
    text_data = []
    cnt = 0
    
    for doc in documents:
        tokens = tokenize(doc, nlp, stopwords, accept_tags)
        text_data.append(tokens)
        
        cnt += 1
        if not cnt%500:
            print(f'{cnt}, ')
    print()
    
    dictionary = corpora.Dictionary(text_data)
        
    return dictionary, text_data
# end make_dictionary()

def make_tftable(tokens, docs):
    """ Create a sorted dataframe of token frequencies across documents. """
    df_tokens = pd.DataFrame(list(tokens.values()), columns=['token'])
    tf = [dict(i) for i in docs]        # accumulate tokens
    
    tf = pd.DataFrame(tf).sum(axis=0)   # term frequencies
    tf = pd.DataFrame(tf, columns=['count'])
    tf.index.names = ['tokenid']
    tf = pd.concat([tf, df_tokens], axis=1)[['token','count']]
    
    tf.sort_values(['count'], ascending=False, inplace=True)
    
    return tf
# end make_tftable()

def make_ldatable(lda_docs, ntopics, sparse=False):
    """ Create dataframe from LDA topic/prob list, w/ sparse matrix option. """

    A = lil_matrix((len(lda_docs), ntopics))
    for i, row in enumerate(lda_docs):
        for tup in row:
            A[i, tup[0]] = tup[1]
    
    if not sparse:
        A = pd.DataFrame(A.toarray())
    
    return A
# end make_ldatable()

def classification_score(ytrue, ypred):
    accuracy = accuracy_score(ytrue, ypred)
    precision = precision_score(ytrue, ypred)
    recall = recall_score(ytrue, ypred)
    f1 = f1_score(ytrue, ypred)
        
    print(f"-- Metric ------ Value ----")
    print(f" Accuracy:  {accuracy:10.3f}")
    print(f" Precision: {precision:10.3f}")
    print(f" Recall:    {recall:10.3f}")
    print(f" F1 Score:  {f1:10.3f}")
    print('\n')
# end classification_score()

