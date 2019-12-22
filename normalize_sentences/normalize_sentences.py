import re


def normalize_sentences(sentence):
    patt = "[\.\?\!]( {1})(?! )"
    return re.sub(patt, end_sentence_repl, sentence)


def end_sentence_repl(matchobj):
    return matchobj.group(0)[0] + "  "

