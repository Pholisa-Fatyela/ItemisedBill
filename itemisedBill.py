import csv

def readingCSV():
    with open('ItemisedBill.csv', 'rU') as newFile:
        reader = csv.reader(newFile)
        newbill = [row for row in reader]
        return newbill

def creatingDictionaryList(data):
    dictionaryList = []
    keys = ['Date', 'Provider', 'Number', 'Duration']
    for lists in data:
        dictionaryList.append(dict(zip(keys, lists)))
    return dictionaryList
