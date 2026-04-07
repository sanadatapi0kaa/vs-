# 単語を数値にするpython
import re
import json
import random
import numpy as np
import attention

token_dim = 8

def DataTalkList():
    from datasets import load_dataset
    ds = load_dataset("roskoN/dailydialog")["train"]

    with open("../data/dataset.txt", "w", encoding="utf-8") as file:
        for i, u in enumerate(ds):
            file.write("<BOS> ")
            text = u["utterances"][0]
            text = re.sub(r'([.,!?])', r' \1 ', text)
            text = " ".join(text.split())
            file.write(text)
            for utt in u["utterances"][1:]:
                text = utt
                text = re.sub(r'([.,!?])', r' \1 ', text)
                text = " ".join(text.split())
                file.write(" <SEP> " + text)
            file.write(" <EOS>\n")
    print("DataTalkList successed!")

def MakeDataListAndId():
    datasetd = open("../data/dataset.txt", "r", encoding="utf-8")
    wordfile = open("../data/word.json", "w", encoding="utf-8")

    nostructure = {".", ",", "/", "(", ")", "[", "]", "!", "?"}
    dataset = datasetd.read()
    before = set(dataset.split())
    middle = set()
    after = {}
    special = ["<PAD>", "<BOS>", "<EOS>", "<SEP>"]
    for u in before:
        if any(chr.isdigit() for chr in u):
            continue
        elif u in special:
            continue
        elif any(ord(chr) < 32 or ord(chr) == 127 for chr in u):
            continue
#        elif len(u) == 1 and u not in nostructure:
#            continue
        else:
            middle.add(u.lower())
    middle = special + list(middle) + ["<UNK>"]

    for i, u in enumerate(middle):
        after[u] = i

    wordfile.write(str(after))

    datasetd.close() 
    wordfile.close()
    print("MakeDataListAndId successed!")

def StringToId(string): #in: string out: list
    word = json.loads(open("../data/word.json", "r", encoding="utf-8").read())
    words = string.lower().split()
    id = []
    for i, u in enumerate(words):
        if u not in word:
            print("no word find [" + u + "] in list")
        else:
            id.append(word[str(u)])
    return id

def IdToString(id): #in: list out: list
    word = json.loads(open("../data/word.json", "r", encoding="utf-8").read())
    ids = list(id)
    string = []
    for i, u in enumerate(ids):
        if int(u) > len(word):
            print("no id find [" + u + "]")
        else:
            for j in word:
                if word[j] == int(u):
                    string.append(j)
    return string

def MakeRandomToken():
    word = json.loads(open("../data/word.json", "r", encoding="utf-8").read())
    vocabfile = open("../data/vocab.json", "w", encoding="utf-8")
    v = len(word)
    e = [[0 for _ in range(token_dim)] for _ in range(v)]
    for i in range(v):
        for j in range(token_dim):
            e[i][j] = random.random()
    vocabfile.write(str(e))
    print("MakeRandomToken successed!")

def IdToWordToken(id): #in: list out: list
#    if type(id) != "<class 'list'>":
#        print("input error: arg is not list in IdToWordToken() function.")
#        return
    vocab = json.loads(open("../data/vocab.json", "r", encoding="utf-8").read())
    token = [[0 for _ in range(token_dim)] for _ in id]
    for i, u in enumerate(id):
        token[i] = vocab[int(u)]
    return token

def AddPositionToken(ids): #in: list out: list
    if (token_dim != len(ids[0])):
        print("error: different token_dim")
        return
    for i in range(len(ids)):
        for j in range(token_dim):
            div = 10000 ** ((2 * (j // 2)) / token_dim)
            if j % 2 == 0:
                ids[i][j] += np.sin(i / div)
            elif j % 2 == 1:
                ids[i][j] += np.cos(i / div)
    return ids

# DataTalkList()
# MakeDataListAndId()
# MakeRandomToken()
# print(IdToWordToken(StringToId("I love you .")))
# AddPositionToken([[0.6938675080191237, 0.45416365558827054, 0.9745788530133734, 0.2315200312397251, 0.1489799716647281, 0.23516237339837076, 0.0258848829499726, 0.18303573632176162], [0.25854806311499, 0.6240277823631565, 0.6192052285972156, 0.8584914187802557, 0.56109097796619, 0.07447859082720776, 0.14469262091523039, 0.8616202121003058], [0.8156228153398246, 0.5483865064454017, 0.30420314399421233, 0.6717924717744124, 0.21767131941569995, 0.8159912202336824, 0.7705920622351916, 0.6378888571380887], [0.9532998084730818, 0.8824828793742482, 0.33701707687838867, 0.09109514495230708, 0.6172649437962542, 0.6581508140745935, 0.9610937223584437, 0.8508608187567092]])

def Trydo():
    a = StringToId("I love you .")
    a = IdToWordToken(a)
    a = AddPositionToken(a)
    a = attention.MakeScores(a)
    print(a)

Trydo()