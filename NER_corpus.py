#Training data

with open("E://7th sem CSE/internship/CRF_4_NER-master/train.txt", "r") as f:
    sents = [line.strip() for line in f.readlines()]


train_num = int((len(sents)//3))
with open("E://7th sem CSE/internship/CRF_4_NER-master/train.data", "w") as g:
    for i in range(train_num):
        words = sents[3*i].split('\t')
        postags = sents[3*i+1].split('\t')
        tags = sents[3*i+2].split('\t')
        for word, postag, tag in zip(words, postags, tags):
            g.write(word+' '+postag+' '+tag+'\n')
        g.write('\n')

print('OK train!')





#Testing Data

with open("E://7th sem CSE/internship/CRF_4_NER-master/test.txt", "r") as f:
    sents = [line.strip() for line in f.readlines()]


test_num = int((len(sents)//3))
with open("E://7th sem CSE/internship/CRF_4_NER-master/test.data", "w") as g:
    for i in range(test_num):
        words = sents[3*i].split('\t')
        postags = sents[3*i+1].split('\t')
        tags = sents[3*i+2].split('\t')
        for word, postag, tag in zip(words, postags, tags):
            g.write(word+' '+postag+' '+tag+'\n')
        g.write('\n')

print('OK test!')

