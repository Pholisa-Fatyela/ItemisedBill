import csv

def readingCSV():
    with open('ItemisedBill.csv', 'rU') as newFile:
        reader = csv.reader(newFile)
        newbill = [row for row in reader]
        return newbill
