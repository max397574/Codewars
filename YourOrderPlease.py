#https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
def order(sentence:str)->str:
    words=sentence.split(' ')
    sentenceord=''
    wordsord=sorted(words, key=lambda w:sorted(w))
    sentenceord=" ".join(wordsord)
    return sentenceord
