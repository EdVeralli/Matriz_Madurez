#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 12:37:15 2023

@author: eduardo
"""

import stanza

nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma')
doc = nlp('Barack Obama nacio en Hawaii un dia lunes.')
#print(*[f'word: {word.text+" "}\tlemma: {word.lemma}' for sent in doc.sentences for word in sent.words], sep='\n')



for sent in doc.sentences:
    for word in sent.words:
        print( word.text , word.lemma)
