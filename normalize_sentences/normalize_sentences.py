import re


def normalize_sentences(sentence):
    patt = "([^.].[.?!] )(?! )"
    return re.sub(patt, r"\1 ", sentence)


def end_sentence_repl(matchobj):
    return matchobj.group(0)[0] + "  "

