import pandas as pd
from graphviz import Digraph

class task5:

    def __init__(self, filename= None):
        if filename is None:
            self.y = pd.read_json('./Data/sample_100k_lines.json', lines=True)
        else:
            self.y = pd.read_json(filename, lines=True)


    def getDocVeiwedBy(self, docId):
        x = self.y.loc[(self.y['subject_doc_id'] == docId) & ( self.y['env_type'] == 'reader')]
        x = x['visitor_uuid'].dropna().unique()
        return x

    def getUserReadDoc(self, userID):
        w = self.y.loc[(self.y['visitor_uuid'] == userID)& ( self.y['env_type'] == 'reader')]
        w = w['subject_doc_id'].dropna()
        return w

    def AlsoLikes(self, docID, userID=None):

        a = self.getDocVeiwedBy(docID)        #Getting Users who Viewed Docs
        b = {}
        for x in a:
            b[x] = self.getUserReadDoc(x).tolist()      # Getting Documents viewed by user and stored in a list
        m = {}

        if userID in b:                       # Removing UserID if specified
            b.pop(userID, None)
            a = a[(a != userID)]

        n = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in b.items()]))

        for x in a:
            m[x] = (n[x].value_counts().sort_values(ascending=False)).to_dict()    #Sorts as pandas based on vlaue of Doc id for each user

        s = {}
        for x in m:                                                   #Loop to count instances of Document IDs as whole
            for i in m[x]:
                if i in s:
                    s[i] = s[i] + m[x][i]
                else:
                    s[i] = m[x][i]

        a = []
        b = []

        for x in s:
            b.append(s[x])

        b.sort(reverse= True)

        for x in b:
            for key, value in s.items():            #Sorting Doc ID based on value
                if x == value:
                    a.append(key)

        a = pd.DataFrame(a, columns=['Users Also Read(5d)'])
        a = a['Users Also Read(5d)'].unique()
        a = pd.DataFrame(a, columns=['Users Also Read(5d)'])
        a.drop(a[a['Users Also Read(5d)'] == docID].index, inplace=True)
        a['count']= a['Users Also Read(5d)'].map(s)
        return a.head(10)

class task6:

    def __init__(self, filename= None):
        self.filename = filename

    def DotPlot(self, docID, userID= None):
        t5 = task5(self.filename)
        a = t5.getDocVeiwedBy(docID)  # Getting Users who Viewed Docs
        b = {}
        for x in a:
            b[x] = t5.getUserReadDoc(x).unique().tolist()  # Getting Documents viewed by user and stored in a list
        n = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in b.items()]))
        m = {}
        for x in n:                                   #Drops any duplicate values within dataframe and stores in dictionary
            n[x] = n[x].drop_duplicates()
            m[x] = n[x].dropna().unique().tolist()

        z = {}

        likes = t5.AlsoLikes(docID, userID)     #Gets top 10 Also Reads from task5()
        like = likes['Users Also Read(5d)'].tolist()
        like.append(docID)

        for x in m:                                   #From m finds DocIDs that are there in AlsoLikes() and stores in Dictionary
            a = []
            for liked in like:
                for value in m[x]:
                    if (value == liked):
                        a.append(value)
            z[x] = a

        # Starting the Dot graph making process
        f = Digraph(comment='Dot Graph')
        value = docID[-4:]
        f.attr('node', shape='circle')
        f.node(str(value), str(value), style='filled', fillcolor='green')

        if not (userID is None) and not (userID == ''):
           f.attr('node', shape='square')  # Creates Node for userid
           f.node(userID[-4:], userID[-4:], style='filled', fillcolor='green')

        if userID in z:                                       #Remove UserID if it exists in Sorting Dictionary
            for x in z[userID]:
                 if x == docID:
                    f.edge(userID[-4:], value, nodesep='100.0')
            z.pop(userID, None)

        for index in z:                                        #Creating nodes for other users
            val = []
            f.attr('node', shape='square')
            f.node(index[-4:], index[-4:])
            for value in z[index]:
                value = value[-4:]
                if not(value in val):                           #Prevents Extra connections if node with last name exists
                    val.append(value)
                    f.attr('node', shape='circle')
                    f.node(value, value)
                    f.edge(index[-4:], value, nodesep='200.0')
        f.render('./Output/Dot Graph for task 6',view=True)
        return;
