
import pandas as pd
import matplotlib.pyplot as plt

class task3a:

    def __init__(self, filename= None):
        if filename is None:
            self.y = pd.read_json('./Data/sample_100k_lines.json', lines=True)
        else:
            self.y =  pd.read_json(filename, lines=True)


    def VeiwBrowser(self):                      #Method to get Browser when Doc ID is not given
        plt.hist(self.y['visitor_useragent'], color='red', rwidth = 0.9)
        max = "The Most Used Browser is :" + self.y[
            'visitor_useragent'].value_counts().idxmax()  # Displays max value in Data Frame
        plt.title('Documents Opened By Browsers:' + max)
        plt.xlabel('Browsers')
        plt.ylabel('Frequency')

        plt.show()

        return max;

    def VeiwBrowserDoc(self, docID):                        #Method to get Browser when Doc ID is given
        df = self.y.loc[self.y['subject_doc_id'] == docID]
        plt.hist(df['visitor_useragent'], color='red', rwidth = 0.9)
        max = "The Most Used Browser is :" + self.y['visitor_useragent'].value_counts().idxmax()
        plt.title('Document '+ docID[-4:] +' Opened By Browsers: ' +max)
        plt.xlabel('Browsers')
        plt.ylabel('Frequency')
        plt.show()

        return max;

class task3b:

    def __init__(self, filename= None):
        if filename is None:
            self.y = pd.read_json('./Data/sample_100k_lines.json', lines=True)
        else:
            self.y =  pd.read_json(filename, lines=True)


    def VeiwBrowserName(self):                       #Method to get Browser when Doc ID is not given
        x = self.y.visitor_useragent.str.split('/', n=100, expand=True)
        x = x.loc[:, [0]]
        x = x.rename(columns={0: 'Browser'})
        x = pd.concat([self.y, x], axis=1)
        plt.hist(x['Browser'], color='red', rwidth = 0.9)

        plt.xlabel('Browser')
        plt.ylabel('Frequency')

        max = "The Most Used Browser is :" + x['Browser'].value_counts().idxmax()
        plt.title('Documents Opened By Browser:' +max)
        plt.show()
        return max;

    def VeiwBrowserNameDoc(self, docID):                 #Method to get Browser when Doc ID is not given
        x = self.y.visitor_useragent.str.split('/', n=100, expand=True)
        x = x.loc[:, [0]]
        x = x.rename(columns={0: 'Browser'})
        x = pd.concat([self.y, x], axis=1)
        df = x.loc[x['subject_doc_id'] == docID]
        plt.hist(df['Browser'], color='red')
        max = "The Most Used Browser is :" + x['Browser'].value_counts().idxmax()
        plt.title('Document '+ docID[-4:] +' Opened By Browsers: ' +max)
        plt.xlabel('Browser')
        plt.ylabel('Frequency')
        plt.show()

        return max;