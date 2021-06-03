import pandas as pd
df2 = pd.read_csv('https://github.com/Capstone-B21-CAP0220/RestSwacAppV2/blob/main/DatasetSAPPA%20-%20Sheet1.zip?raw=true', compression='zip', sep=',', quotechar='"')
print(len(df2))
