import argparse
import os
from datetime import datetime

import nest_asyncio
import pandas as pd
import twint
from tqdm import tqdm

nest_asyncio.apply()

MAIN_SAVE_DIR = './home/scrapped_data/'

HASHTAG = "#TrybunałKonstytucyjny"
HASHTAG_SINCE = "2020-10-19 00:00:00"
HASH_FILE_NAME = 'hash_trybunal.csv'

USERS_SUB_FOLDER = 'users'
USER_SINCE = "2020-10-12 00:00:00"

# read arg
parser = argparse.ArgumentParser()
parser.add_argument(
    '--search-depth',
    required=False,
    help='Depth of retweeted users search',
    type=int,
    default=3
)
search_depth = parser.parse_args().search_depth

# create new save dir
today = datetime.today()
new_dir = '_'.join(
    [str(today.day), str(today.hour+2), str(today.minute), str(today.second)]
)
os.mkdir(MAIN_SAVE_DIR+new_dir)
hash_save_dir = MAIN_SAVE_DIR+new_dir+'/'

# download all tweets with hashtag
c = twint.Config()
c.Since = HASHTAG_SINCE
c.Output = (hash_save_dir+HASH_FILE_NAME)
c.Store_csv = True
c.Search = HASHTAG
c.Tabs = True
twint.run.Search(c)

# read found users profiles
os.mkdir(hash_save_dir+USERS_SUB_FOLDER)
users_save_dir = hash_save_dir+USERS_SUB_FOLDER+'/'

def read_user_profile(user, since, save_dir):
    c = twint.Config()
    c.Username = user
    c.Retweets = True
    c.Store_csv = True
    c.Output = (save_dir+user+".csv")
    c.Since = since
    c.Tabs = True
    twint.run.Profile(c)

def get_retweeted_users(user, save_dir):
    retweeted_users = []
    try:
        user_data = pd.read_csv(save_dir+user+".csv", sep='\t')
        user_data = user_data[user_data['retweet'] == True]
        if len(user_data) > 0:
            user_data['rt_user_name'] = user_data.apply(
                lambda x: x['tweet'].split(' ')[1][1:-1],
                axis=1
            )
            retweeted_users = user_data['rt_user_name'].unique()
    except Exception as e:
        print(e)
    print('Found retweeted users: '+str(len(retweeted_users)))
    return retweeted_users

scanned_users = set([])
next_queue = pd.read_csv(hash_save_dir+HASH_FILE_NAME, sep='\t')['username'].unique()
for i in range(search_depth):
    queue = next_queue
    next_queue = []
    for user in tqdm(queue, desc="QUEUE "+str(i)):
        if user not in scanned_users:
            read_user_profile(user, USER_SINCE, users_save_dir)
            scanned_users.add(user)
            if search_depth > 1:
                next_queue.extend(get_retweeted_users(user, users_save_dir))
