# 単語を数値にするpython

def DataTalkList():
    import re
    from datasets import load_dataset

    ds = load_dataset("roskoN/dailydialog")["train"]
    nostructure = {".", ",", "/", "(", ")", "[", "]", "!", "?"}

    with open("../data/dataset.txt", "w", encoding="utf-8") as file:
        for i, u in enumerate(ds):
            file.write("<BOS> ")
            text = u["utterances"][0]
            text = re.sub(r'=([.,!?])-', r' \1 ', text)
            text = " ".join(text.split())
            file.write(text)
            for utt in u["utterances"][1:]:
                text = utt
                text = re.sub(r'=([.,!?])-', r' \1 ', text)
                text = " ".join(text.split())
                file.write(" <SEP> " + text)
            file.write(" <EOS>\n")

def MakeDataListAndId():
    datasetd = open("../data/dataset.txt", "r", encoding="utf-8")
    vocab = open("../data/vocab.json", "w", encoding="utf-8")

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
        elif len(u) == 1 and u not in nostructure:
            continue
        else:
            middle.add(u.lower())
    middle = special + list(middle)

    for i, u in enumerate(middle):
        after[u] = i

    vocab.write(str(after))

    datasetd.close() 
    vocab.close()

def StringToId(string):
    import json

    vocab = json.loads(open("../data/vocab.json", "r", encoding="utf-8").read())
    token = string.split()
    id = []
    for i, u in enumerate(token):
        id.append(vocab[str(u)])
    print(id)

def IdToString(id):
    import json

    vocab = json.loads(open("../data/vocab.json", "r", encoding="utf-8").read())
    token = id.split()
    string = []
    for i, u in enumerate(token):
        string.append(vocab[int(u)])
    print(string)
