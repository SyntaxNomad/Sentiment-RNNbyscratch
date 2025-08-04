import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder




label_encoder = LabelEncoder()

data = pd.read_csv("IMDB Dataset.csv")
data['sentiment']=label_encoder.fit_transform(data['sentiment'])

import string

char_to_num = {}
num = 1





# Add all lowercase letters
for char in string.ascii_lowercase:
    char_to_num[char] = num
    num += 1

# Add all uppercase letters  
for char in string.ascii_uppercase:
    char_to_num[char] = num
    num += 1

# Add all digits
for char in string.digits:
    char_to_num[char] = num
    num += 1

# Add common punctuation
punctuation = ' !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
for char in punctuation:
    char_to_num[char] = num
    num += 1






for i in range(len(data)):
    current_review = data['review'].iloc[i]
    temp=[]
    for char in current_review:
        if char in char_to_num:
          temp.append(char_to_num[char])
        else:
            continue
    
        print(temp)

