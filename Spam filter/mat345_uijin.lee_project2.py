import os

#label the mails
directory = "G:/mat345/"
training_ham_path = os.path.join(directory, "training_ham")
testing_ham_path = os.path.join(directory, "testing_ham")
training_spam_path = os.path.join(directory, "training_spam")
testing_spam_path = os.path.join(directory, "testing_spam")

#create folders
if not os.path.exists(training_ham_path):
    os.mkdir(training_ham_path)
if not os.path.exists(testing_ham_path):
    os.mkdir(testing_ham_path)
if not os.path.exists(training_spam_path):
    os.mkdir(training_spam_path)
if not os.path.exists(testing_spam_path):
    os.mkdir(testing_spam_path)

#split files into testing and training every 4th message
easy_ham_path = os.path.join(directory, "easy_ham")
hard_ham_path = os.path.join(directory, "hard_ham")
spam_path = os.path.join(directory, "spam")

easy_ham = os.listdir(easy_ham_path)
hard_ham = os.listdir(hard_ham_path)
spam = os.listdir(spam_path)

countEasyHam = 1
countHardHam = 1
countSpam = 1

for files in easy_ham:
    if countEasyHam % 4 == 0:
        os.replace(os.path.join(easy_ham_path, files), os.path.join(testing_ham_path, files))
    else:
        os.replace(os.path.join(easy_ham_path, files), os.path.join(training_ham_path, files))
    countEasyHam += 1
    
for files in hard_ham:
    if countHardHam % 4 == 0:
        os.replace(os.path.join(hard_ham_path, files), os.path.join(testing_ham_path, files))
    else:
        os.replace(os.path.join(hard_ham_path, files), os.path.join(training_ham_path, files))
    countHardHam += 1
    
for files in spam:
    if countSpam % 4 == 0:
        os.replace(os.path.join(spam_path, files), os.path.join(testing_spam_path, files))
    else:
        os.replace(os.path.join(spam_path, files), os.path.join(training_spam_path, files))
    countSpam += 1

training_ham = os.listdir(training_ham_path)
training_spam = os.listdir(training_spam_path)

#gather words in hamword and spamword dictionaries
subject = "Subject"
hamWord = {}
spamWord = {}
WordList = []
IgnoreList = ["on", "an", "the", "this", "to", "is", "for", "in", "of", "a", "with", "are",
 "and", "that", "can", "as", "by", "so", "at", "you", "from", "your"]

for txt in training_ham:
    with open(os.path.join(training_ham_path, txt), 'r', encoding= 'cp850') as filedata:
        lines = filedata.readlines()
        for line in lines:
            words = line.split(' ')
            if subject in line:
                for w in words:
                    if w.isalpha() == True:
                        lower = w.lower()
                        if not lower in IgnoreList:
                            if not lower in hamWord:
                                hamWord[lower] = 1
                            hamWord[lower] += 1 
                        if not lower in WordList and not lower in IgnoreList:
                            WordList.append(lower)
                         
for txt in training_spam:
    with open(os.path.join(training_spam_path, txt), 'r', encoding= 'cp850') as filedata:
        lines = filedata.readlines()
        for line in lines:
            words = line.split(' ')
            if subject in line:
                for w in words:
                    if w.isalpha() == True:
                        lower = w.lower()
                        if not lower in IgnoreList:
                            if not lower in spamWord:
                                spamWord[lower] = 1
                            spamWord[lower] += 1
                        if not lower in WordList and not lower in IgnoreList:
                            WordList.append(lower)

NumSpam = 0
NumHam = 0
NumWord = 0

for w in WordList:
    if w in spamWord:
        NumSpam += spamWord.get(w)
        NumWord += spamWord.get(w)
    if w in hamWord:
        NumHam += hamWord.get(w)
        NumWord += hamWord.get(w)

alpha = 1
beta = 2

p_wSpam = {}
p_wHam = {}

p_spamW = {}
p_hamW = {}

for w in WordList:
    if w in spamWord:
        spam = spamWord.get(w)
        p_wSpam[w] = float((alpha + spam)/(beta + NumSpam))
    if w in hamWord:
        ham = hamWord.get(w)
        p_wHam[w] = float((alpha + ham)/(beta + NumHam))

pSpam = NumSpam / NumWord
pHam = 1.0 - pSpam

for w in WordList:
    wSpam = 0.0
    wHam = 0.0
    if w in spamWord:
        wSpam = p_wSpam.get(w)
    if w in hamWord:
        wHam = p_wHam.get(w)
    p_spamW[w] = ((pSpam * wSpam)/(pSpam * wSpam + pHam * wHam))
    p_hamW[w] = ((pHam * wHam)/(pSpam * wSpam + pHam * wHam))

sortedP_spamW = dict(sorted(p_spamW.items(), key = lambda item: item[1], reverse=True))
sortedP_hamW = dict(sorted(p_hamW.items(), key = lambda item: item[1], reverse=True))

print("list of 5 words with highest p(spam|wk)")
print(list(sortedP_spamW.keys())[0])
print(list(sortedP_spamW.keys())[1])
print(list(sortedP_spamW.keys())[2])
print(list(sortedP_spamW.keys())[3])
print(list(sortedP_spamW.keys())[4])
print("\n")
print("list of 5 words with highest p(ham|wk)")
print(list(sortedP_hamW.keys())[0])
print(list(sortedP_hamW.keys())[1])
print(list(sortedP_hamW.keys())[2])
print(list(sortedP_hamW.keys())[3])
print(list(sortedP_hamW.keys())[4])

#testing
testing_ham = os.listdir(testing_ham_path)
testing_spam = os.listdir(testing_spam_path)
T_hamWord = {}
T_spamWord = {}
T_WordList = []


for txt in testing_ham:
    with open(os.path.join(testing_ham_path, txt), 'r', encoding= 'cp850') as filedata:
        lines = filedata.readlines()
        for line in lines:
            words = line.split(' ')
            if subject in line:
                for w in words:
                    if w.isalpha() == True:
                        lower = w.lower()
                        if not lower in IgnoreList:
                            if not lower in T_hamWord:
                                T_hamWord[lower] = 1
                            T_hamWord[lower] += 1 
                        if not lower in T_WordList and not lower in IgnoreList:
                            T_WordList.append(lower)
                         
for txt in testing_spam:
    with open(os.path.join(testing_spam_path, txt), 'r', encoding= 'cp850') as filedata:
        lines = filedata.readlines()
        for line in lines:
            words = line.split(' ')
            if subject in line:
                for w in words:
                    if w.isalpha() == True:
                        lower = w.lower()
                        if not lower in IgnoreList:
                            if not lower in T_spamWord:
                                T_spamWord[lower] = 1
                            T_spamWord[lower] += 1
                        if not lower in T_WordList and not lower in IgnoreList:
                            T_WordList.append(lower)

T_NumSpam = 0
T_NumHam = 0
T_NumWord = 0

for w in T_WordList:
    if w in T_spamWord:
        T_NumSpam += T_spamWord.get(w)
        T_NumWord += T_spamWord.get(w)
    if w in T_hamWord:
        T_NumHam += T_hamWord.get(w)
        T_NumWord += T_hamWord.get(w)

T_p_wHam = {}
T_p_wSpam = {}

for w in WordList:
    TwSpam = 0.0
    TwHam = 0.0

    if w in spamWord:
        TwSpam = p_wSpam.get(w)
    if w in hamWord:
        TwHam = p_wHam.get(w)
    if w in T_WordList:
        T_p_wSpam[w] = (pSpam * TwSpam)/(pSpam * TwSpam + pHam * TwHam)
    else:
        T_p_wSpam[w] = (pSpam * (1-TwSpam))/(pSpam * (1-TwSpam) + pHam * (1-TwHam))

predictSpam = 0
predictHam = 0
RealSpam = 0
RealHam = 0

spamPredictedSpam = 0
hamPredictedHam = 0
spamPredictedHam = 0
hamPredictedSpam = 0

for w in T_p_wSpam:
    if w in T_hamWord:
        RealHam += 1
        #print(w, "is in ham and ")
        if T_p_wSpam.get(w) >= 0.5:
            predictSpam += 1
            hamPredictedSpam += 1
            #print("'",w,"'" ,"could be spam")
        else:
            predictHam += 1
            hamPredictedHam += 1
            #print("'",w,"'" ,"could not be spam")
    if w in T_spamWord:
        RealSpam += 1
        #print(w, "is in spam and")
        if T_p_wSpam.get(w) >= 0.5:
            predictSpam += 1
            spamPredictedSpam += 1
            #print("'",w,"'" ,"could be spam")
        else:
            predictHam += 1
            spamPredictedHam += 1
            #print("'",w,"'" ,"could not be spam")


accuracy = (spamPredictedSpam + hamPredictedHam) / (spamPredictedSpam + hamPredictedHam + spamPredictedHam + hamPredictedSpam)
precision = (spamPredictedSpam)/(predictSpam)
recall = (spamPredictedSpam)/(RealSpam)

print("accuracy is ", accuracy)
print("precision is ", precision)
print("recall is ", recall)
