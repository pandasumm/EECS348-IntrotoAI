from __future__ import print_function
import math
import random

class Bayes_Classifier:

    def __init__(self):
        self.words = {}
        # self.class =
        self.num_positive = 0
        self.num_nagetive = 0

    def num_words(self):
        return len(self.words)

    # def num_positive(self):
    #     return


    def train(self,filename):
        # code to be completed by students to extract features from training file, and
        # to train naive bayes classifier.

        with open(filename, 'r') as f:
            lines = f.readlines()

        for line in lines:
            line = line.replace('\n', '')
            fields = line.split('|')
            wID = int(fields[0])
            # sentiment = 1 if fields[1] == '1' else 5
            sentiment = fields[1]
            text = fields[2].split()
            self.num_positive += len(text) if sentiment == '5' else 0
            self.num_nagetive += len(text) if sentiment == '1' else 0
            for word in text:
                word = word.lower()
                if word not in self.words:
                    self.words[word] = {sentiment:1}
                    temp = '1' if sentiment == '5' else '5'
                    self.words[word][temp] = 0
                else:
                    self.words[word][sentiment] += 1

    def classify(self,filename):
        # code to be completed by student to classifier reviews in file using naive bayes
        # classifier previously trains.  member function must return a list of predicted
        # classes with '5' = positive and '1' = negative
        positive = '5'
        negative = '1'
        predictions = []

        stop_words = ['.', ',', '?', '\'', '/', '-', '\"', '*', '#']

        with open(filename, 'r') as f:
            lines = f.readlines()
        for line in lines:
            line = line.replace('\n', '')
            fields = line.split('|')
            text = fields[2].split()
            p_positive = 0
            p_negative = 0
            for word in text:
                word = word.lower()
                if word in stop_words:
                    continue
                if word not in self.words:
                    p = math.log10(1.0/self.num_words())
                    # p_positive += p
                    # p_negative += p
                    # p_positive += math.log10(
                    #     1.0 / (self.num_words() + self.num_positive))
                    # p_negative += math.log10(
                    #     1.0 / (self.num_words() + self.num_nagetive))
                else:
                    # print (self.num_words()/self.num_positive)
                    p_positive += math.log10(1.0*(1+self.words[word][positive])/(self.num_words()+self.num_positive))
                    p_negative += math.log10(1.0*(1+self.words[word][negative])/(self.num_words()+self.num_nagetive))
            predictions.append('5' if p_positive >= p_negative else '1')
    
        return predictions
