from polyglot.text import Text
import pandas as pd
import os
from tqdm import tqdm
tqdm.pandas()

files_dir = './home/data/'
files = os.listdir(files_dir)

def get_polarity(row):
    try:
        polarity = Text(row['tweet']).polarity
    except ValueError:
        polarity = 0

    return polarity

for file_name in files:
    if file_name.endswith('.csv'):
        print(file_name)
        file_dir = ''.join([files_dir, file_name])
        data = pd.read_csv(file_dir, sep='\t')
        data['polarity'] = data.progress_apply(get_polarity, axis=1)
        data.to_csv(file_dir, sep='\t')