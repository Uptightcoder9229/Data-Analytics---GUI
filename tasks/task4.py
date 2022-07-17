import pandas as pd


class task4d:

    def __init__(self, filename= None):
        if filename is None:
            self.y = pd.read_json('./Data/sample_100k_lines.json', lines=True, dtype= str)
        else:

            self.y =  pd.read_json(str(filename), lines=True)


    def avid_readers(self): #Method to Scan for most read readers
        df = self.y.loc[( self.y['env_type'] == 'reader') & (self.y['event_type'] == 'pagereadtime')]
        df = df.groupby('visitor_uuid')['event_readtime'].sum()
        df = df.sort_values(ascending=False)  #sorts values, Index is visitor id
        x = df.to_frame().reset_index()
        x = x.rename(columns={'visitor_uuid': '(4) Readers who have spent most time reading','event_readtime': 'Total Time Spent Reading' } )
        return x.head(10);

