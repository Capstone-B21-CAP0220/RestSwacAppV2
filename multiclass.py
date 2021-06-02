import pandas as pd
# df = pd.read_csv('https://github.com/Capstone-B21-CAP0220/RestSwacAppV2/blob/main/DatasetSAPPA%20-%20Sheet1.csv')
df=pd.read_csv('https://github.com/srivatsan88/YouTubeLI/blob/master/dataset/consumer_compliants.zip?raw=true', compression='zip', sep=',', quotechar='"')
print(len(df))