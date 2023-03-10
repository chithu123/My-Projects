# Program for Twitter Scraping using MongoDB and streamlit

# Necessary modules are imported
import snscrape.modules.twitter as sntwitter
import streamlit as st
import pandas as pd
import pymongo
from pymongo import MongoClient
from PIL import Image
from datetime import date
import json

# MongoDB client connection is done
client = pymongo.MongoClient("mongodb+srv://chitrababu:1a2b3c4d@cluster0.hxpkf0q.mongodb.net/?retryWrites=true&w=majority")
tweetdb = client.chitra
tweetdb_main = tweetdb.twitterscr.py


# Here starts the main function
def main():
  tweets = 0   
  st.markdown("""
  <style>
   body {   
   background-color: #00f900 !important;
   }
   </style>
    """, 
   unsafe_allow_html=True) 
    
  st.markdown(
  f"""
  <h1 style='color: #F63366; font-size: 48px;'>Twitter Scraping</h1>
  """,
  unsafe_allow_html=True)
    
  #st.title("Twitter Scraping")
  # Menus used in Twitter Scrape web app -- 5 menus are used
  
  menu = ["Home","About","Search","Display","Download"]
  choice = st.sidebar.selectbox("Menu",menu)
  # Menu 1 is Home page 
  if choice=="Home":
  
    st.markdown(
    f"""
    <h3 style='color: #F63366; font-size: 18px;'>Home</h3>
    """,
    unsafe_allow_html=True)
    
    with st.expander("Home"):
        st.write('''This app is a web-based Twitter scraping tool built with the Python library Streamlit. 
                    It allows users to search for tweets containing a specific hashtag or keyword within a given time frame. 
                    The tweets are then extracted from Twitter using the Snscrape package and saved to a MongoDB database.
                    The app provides an easy-to-use interface that allows users to specify their search parameters and view the 
                    results in real-time. The tweets can also be downloaded in CSV or JSON format for further analysis.''')                   
                    
        image = Image.open(r"C:\guvi\datascience-project\elonmusk.png") 
        st.image(image, width=680, caption='Chitra-Twitter Scraping')
        
       

  # Menu 2 is about the Twitter Scrape libraries, databases and apps
  
  elif choice=="About":
    st.markdown(
        f"""    
        <h3 style='color: #F63366; font-size: 18px;'>About</h3>    
        """,
        unsafe_allow_html=True) 
       
    # Info about Twitter Scrapper
    with st.expander("Twitter Scrapper"):
      st.write('''Twitter Scrapper (or Twitter Scraper) is a type of web scraping tool used to extract data from Twitter, 
                    a popular social media platform. A Twitter scraper uses automated bots to collect large amounts of
                    data from Twitter, such as tweets, user profiles, hashtags, and trends.
                    Twitter scrapers can be used for a wide range of applications, such as sentiment analysis, 
                    brand monitoring, market research, and social media analytics. By extracting data from Twitter, 
                    businesses and organizations can gain insights into consumer behavior, market trends, and public opinion.''')
      image = Image.open(r"C:\guvi\datascience-project\twitterscrapper.png") 
      st.image(image, caption='')

    # Info about Snscraper
    with st.expander("Snscraper"):
      st.write('''Both Snscrape and Snscraper are valid Python packages used for web scraping social media platforms, including Twitter, 
                    Instagram, and Reddit. However, the correct name of the package is Snscrape (without the extra "r").
                    In some cases, people may use the incorrect name Snscraper by mistake, or they may be referring to a 
                    different package with a similar name. However, if you want to use the package, you should install 
                    and import it using the correct name Snscrape..''')
      image = Image.open(r"C:\guvi\datascience-project\scrapper.png") 
      st.image(image, caption='')


    # Info about MongoDB database
    with st.expander("MongoDB"):
      st.write('''MongoDB is a popular open-source, document-oriented NoSQL database that is used to store and manage 
                    unstructured and semi-structured data. MongoDB uses a document data model, which means that data is stored
                    in flexible, JSON-like documents, making it easy to handle and scale data..''')
      image = Image.open(r"C:\guvi\datascience-project\mongodb.png") 
      st.image(image, caption='')

    # Info about Streamlit framework
    with st.expander("Streamlit"):
      st.write('''Streamlit is a popular open-source Python library used for building interactive web applications and data visualizations. 
                    It allows you to create custom web applications with just a few lines of Python code. Streamlit provides a simple 
                    and intuitive way to create web applications by providing ready-to-use UI components and easy-to-use APIs..''')
      image = Image.open(r"C:\guvi\datascience-project\streamlit.png") 
      st.image(image, caption='')
      
     

  # Menu 3 is a search option
  elif choice=="Search":
    st.markdown(
        f"""    
        <h3 style='color: #F63366; font-size: 18px;'>Search</h3>    
        """,
        unsafe_allow_html=True) 
    # Every time after the last tweet the database will be cleared for updating new scraping data
    tweetdb_main.delete_many({})

    # Form for collecting user input for twitter scrape
    with st.form(key='form1'):
      # Hashtag input
      st.subheader("Tweet searching Form")
      st.write("Enter the hashtag or keyword to perform the Twitter Scraping")
      query = st.text_input('Hashtag or keyword')

      # No of tweets for scraping
      st.write("Enter the limit for the Data Scraping: Maximum limit is 1000 tweets")
      limit = st.number_input('Insert a number',min_value=0,max_value=1000,step=10)

      # From date to end date for scraping
      st.write("Enter the Starting date to scrap the tweet data")
      start = st.date_input('Start date')
      end = st.date_input('End date')
      
      # Submit button to scrap
      submit_button = st.form_submit_button(label="Tweet Scrap")
    
    if submit_button:
      st.success(f"Tweet hashtag {query} received for scraping".format(query))

      # TwitterSearchScraper will scrape the data and insert into MongoDB database
      for tweet in sntwitter.TwitterSearchScraper(f'from:{query} since:{start} until:{end}').get_items():
        # To verify the limit if condition is set
        if tweets == limit:
          break
        # Stores the tweet data into MongoDB until the limit  is reached
        else:      
          new = {"date":tweet.date,"user":tweet.user.username, "url":tweet.url, "followersCount":tweet.user.followersCount, "friendsCount":tweet.user.friendsCount, "favouritesCount":tweet.user.favouritesCount,"mediaCount":tweet.user.mediaCount}
          tweetdb_main.insert_one(new)
          tweets += 1
      
    # Display the total tweets scraped
    df = pd.DataFrame(list(tweetdb_main.find()))
    cnt = len(df)
    st.success(f"Total number of tweets scraped for the input query is := {cnt}".format(cnt))
    

  # Menu 4 is for diaplying the data uploaded in MmongoDB
  elif choice=="Display":
    st.markdown(
        f"""    
        <h3 style='color: #F63366; font-size: 18px;'>Display</h3>    
        """,
        unsafe_allow_html=True) 
    # Save the documents in a dataframe
    df = pd.DataFrame(list(tweetdb_main.find()))
    #Dispaly the document 
    st.dataframe(df)
       

  # Menu 5 is for Downloading the scraped data as CSV or JSON
  else:
    col1, col2 = st.columns(2)

    # Download the scraped data as CSV
    with col1:
      st.write("Download the tweet data as CSV File")
      # save the documents in a dataframe
      df = pd.DataFrame(list(tweetdb_main.find()))
      # Convert dataframe to csv
      df.to_csv('twittercsv.csv')
      def convert_df(data):
        # Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')
      csv = convert_df(df)
      st.download_button(
                        label="Download data as CSV",
                        data=csv,
                        file_name='twitercsv.csv',
                        mime='text/csv',
                        )
      st.success("Successfully Downloaded data as CSV")

    # Download the scraped data as JSON
    with col2:
      st.write("Download the tweet data as JSON File")
      # Convert dataframe to json string instead as json file 
      twtjs = df.to_json(default_handler=str).encode()
      # Create Python object from JSON string data
      obj = json.loads(twtjs)
      js = json.dumps(obj, indent=4)
      st.download_button(
                        label="Download data as JSON",
                        data=js,
                        file_name='twtjs.js',
                        mime='text/js',
                        )
      st.success("Successfully Downloaded data as JSON")

# Call the main function
main()