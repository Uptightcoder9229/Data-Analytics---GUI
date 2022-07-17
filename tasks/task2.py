
import pandas as pd
import matplotlib.pyplot as plt


class task2b:

    def __init__(self, filename=None):
        if filename is None:
            self.y = pd.read_json('./Data/sample_100k_lines.json', lines=True)
        else:
            self.y = pd.read_json(filename, lines=True)

        #Csv with data of continents and country
        self.z = pd.read_csv('./Data/country_continent.csv', header=None, index_col=0, squeeze=True, na_filter=False)


    def VeiwContient(self, docID):      #Method to see if continent DocID was veiwed at
        self.y['visitor_continent'] = (self.y['visitor_country'].map(self.z)).astype(str)  #Maps Continent data frame to dataset
        df = self.y.loc[self.y['subject_doc_id'] == docID]
        plt.hist(df['visitor_continent'], rwidth = 0.9,color='red')
        plt.title('Document Opened By Continent')
        plt.xlabel('Continent')
        plt.ylabel('Frequency')
        plt.show()
        return df;

class task2a:

    #Constructor to store
    def __init__(self, filename= None):
        if filename is None:
            self.y = pd.read_json('./Data/sample_100k_lines.json', lines=True)
        else:
            self.y =  pd.read_json(filename, lines=True)


    def VeiwCountry(self, arg1):   #Method to see countries DocID was veiwed at

        df = self.y.loc[self.y['subject_doc_id'] == arg1]
        plt.hist(df['visitor_country'], color='red', rwidth= 0.9)
        plt.title('Document Opened By Country')
        plt.xlabel('Country')
        plt.ylabel('Frequency')
        plt.show()
        return df;


