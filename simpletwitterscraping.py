pip install snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd
import json

query = 'from:elonmusk since:2023-02-15 until:2023-03-07'
limit = 1000

tweets = sntwitter.TwitterSearchScraper(query).get_items()

df = pd.DataFrame(columns=['Date','URL' ,'Tweet'])

for index, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if index > limit:
        break
    df2 = {'Date': tweet.date, 'URL': tweet.url, 'Tweet': tweet.rawContent}
    df = pd.concat([df, pd.DataFrame.from_records([df2])])

print(df)

df.to_csv('elonmusk.csv')


output:
  
         Date  \
0  2023-03-06 22:36:57+00:00   
0  2023-03-06 22:08:42+00:00   
0  2023-03-06 20:38:06+00:00   
0  2023-03-06 20:25:15+00:00   
0  2023-03-06 20:14:06+00:00   
..                       ...   
0  2023-02-15 01:31:44+00:00   
0  2023-02-15 01:18:25+00:00   
0  2023-02-15 00:43:45+00:00   
0  2023-02-15 00:37:24+00:00   
0  2023-02-15 00:31:59+00:00   

                                                  URL  \
0   https://twitter.com/elonmusk/status/1632872927...   
0   https://twitter.com/elonmusk/status/1632865818...   
0   https://twitter.com/elonmusk/status/1632843016...   
0   https://twitter.com/elonmusk/status/1632839781...   
0   https://twitter.com/elonmusk/status/1632836977...   
..                                                ...   
0   https://twitter.com/elonmusk/status/1625669153...   
0   https://twitter.com/elonmusk/status/1625665801...   
0   https://twitter.com/elonmusk/status/1625657077...   
0   https://twitter.com/elonmusk/status/1625655479...   
0   https://twitter.com/elonmusk/status/1625654117...   

                                                Tweet  
0   @ryanhallyall It is a major priority to enable...  
0   Accounts engaging in repeated, egregious weapo...  
0                  @cb_doge @TrungTPhan I was robbed!  
0   @micsolana If what they want are pretty pics &...  
0   @BillyM2k @micsolana Yup, they can dish it out...  
..                                                ...  
0                      Twitter pinned lists are great  
0             @cb_doge @alifarhat79 High mileage club  
0       @hikingskiing A lot has happened in ten years  
0   @YoungBudgeteer @Jarrad_Hicks @abidc @anotherc...  
0   @alifarhat79 Damn, that’s impressive bus driving!  

[542 rows x 3 columns]
