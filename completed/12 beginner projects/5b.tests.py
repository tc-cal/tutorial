
from word_list import words

directory = words # can + words at the end
criteria = [w for w in directory] # do something to w for each w in directory
cri = "".join(l for l in criteria)
print(cri)

