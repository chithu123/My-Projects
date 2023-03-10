Twitter Scraping with MongoDB and Streamlit

This is a web-based Twitter scraping tool built with Python, using the Streamlit framework for the user interface, the Snscrape package for accessing Twitter data, and the MongoDB database to store the extracted tweets. The app allows users to search for tweets containing a specific hashtag or keyword within a given time frame, and view, download, and analyze the results in real-time.

Acknowledgements

•	GUVI
•	Mentor Mr. BalaChander
•	Streamlitdocs

Installation

To use this app, you need to have Python 3.x installed on your system, as well as the following Python packages:
•	streamlit
•	snscrape
•	pandas
•	pymongo
•	PIL

You can install them using pip, like this:
pip install streamlit snscrape pandas pymongo pillow
or 
requirement.txt file.

you also need to have access to a MongoDB database, and provide the connection string and database name in the program.


Usage

To run the app, open a terminal, navigate to the directory where the program is located, and enter the following command:
streamlit run twitter_scrape.py

This will start the app in your web browser, and you can interact with it using the menus and buttons.

Features

The app has five menus that allow you to perform different tasks:
1.	Home: This is the landing page, where you can read a brief description of the app and see an image.
2.	About: This page provides information about the tools and technologies used in the app, such as Twitter Scrapper, Snscrape, MongoDB, and Streamlit.
3.	Search: This page allows you to search for tweets containing a specific keyword or hashtag, within a specified time frame. You can also choose how many tweets to display on the screen, and the fields to include in the output.
4.	Display: This page shows the tweets that match the search criteria, in a table format. You can sort the tweets by different columns, and click on a tweet to see more details.
5.	Download: This page allows you to download the tweets that match the search criteria, in CSV or JSON format.

Demo Video Link: https://youtu.be/O28nXsIFZzs


Screenshots
Here are some screenshots of the app in action: 
 
![image](https://user-images.githubusercontent.com/99309914/224333894-2ccdae6b-7c93-485d-9aa6-e81f19bb52c1.png) 
![image](https://user-images.githubusercontent.com/99309914/224333947-249df003-c268-4ed3-9f51-19151319788e.png)
![image](https://user-images.githubusercontent.com/99309914/224334038-11b113b3-7ddb-4ad5-8e1d-ff41c79b003c.png)
![image](https://user-images.githubusercontent.com/99309914/224334091-ce845172-efff-40ba-a478-42ba348bb074.png)


 
 

