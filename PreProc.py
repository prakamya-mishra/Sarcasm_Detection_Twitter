import re
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import csv
import os


def main():
    pwd = os.getcwd();
    norm_in = pwd + "/norm_input"
    norm_out = pwd + "/norm_out"
    sarc_in = pwd + "/sarc_input"
    sarc_out = pwd + "/sarc_out"
    stop = set(stopwords.words('english'))

    for f in os.listdir(norm_in):
        inputDest = os.path.join(norm_in,f)
        outputDest = os.path.join(norm_out,f)
        inputFile = open(inputDest,"r")
        outputFile = open(outputDest,"w")
        reader=csv.reader(inputFile)
        writer=csv.writer(outputFile)
        for row in reader:
            row[2]=preprocess(row[2],stop)
            print(row)
            writer.writerow(row)
        inputFile.close()
        outputFile.close()
    for f in os.listdir(sarc_in):
        inputDest = os.path.join(sarc_in,f)
        outputDest = os.path.join(sarc_out,f)
        inputFile = open(inputDest,"r")
        outputFile = open(outputDest,"w")
        reader=csv.reader(inputFile)
        writer=csv.writer(outputFile)
        for row in reader:
            row[2]=preprocess(row[2],stop)
            print(row)
            writer.writerow(row)
        inputFile.close()
        outputFile.close()


def preprocess(tweet,stopwords):
    tweet = tweet.replace("#sarcasm","")
    tweet = tweet.replace("#sarcastic","")
    tweet = re.sub(r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)", "", tweet)
    tweet = re.sub(r'^https?:\/\/.*[\r\n]*', '', tweet, flags=re.MULTILINE)
    table = str.maketrans("?/:^&*()!@$%:;',<.>-+*\{\}[]\"#"," "*30)
    tweet= tweet.translate(table)
    stemmer = SnowballStemmer("english",ignore_stopwords=True)
    tokens = tweet.split()
    tokens = [ w for w in tokens if w not in stopwords]
    tokens = [item for item in tokens if item.isalpha()]
    tokens = [ stemmer.stem(w) for w in tokens ]
    return " ".join(tokens)



if __name__=="__main__":
    main()

