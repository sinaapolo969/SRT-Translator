# you should first run this commands:
#       1- pip install pandas
#       2- pip install googletrans==3.1.0a0

import pandas as pd
import re
from googletrans import Translator


df = pd.read_excel('C:/Users/kara/SRT.xlsx')
df.fillna(0, inplace = True)
translator = Translator()

print('PLEASE WAIT.....')
for i in range(len(df[1])):
    if type(df[1][i]) != int:
        if re.search("[a-z]", df[1][i]):
            x = translator.translate(df[1][i], dest = 'fa')
            df[1][i] = x.text

new_file_path = 'enter your directory' + 'subtittle.srt'
with open(new_file_path, 'w') as f:
    for i in df[1]:
        if i == 0:
            f.write('\n')
        else:
            f.write(str(i))
            f.write('\n')
print('DONE!!!')

