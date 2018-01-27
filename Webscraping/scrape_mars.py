


# ### Mission to Mars - Webscraping and 


import time
from splinter import Browser
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd


def init_browser():

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    # create mars_data dict that we can insert into mongo
    mars_data = {}

    ## Mars News

    # visit mars news page
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(3)

    # create html object and run parser on it
    html = browser.html
    soup = bs(html, 'html.parser')


    # save latest headline and text to variables
    news_title = soup.find('div', class_="content_title").text
    news_p = soup.find('div', class_="article_teaser_body").text
    time.sleep(2)

    ## Mars Images
    
    # visit mars images page
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)
    time.sleep(3)

    # find featured full image button and click it
    browser.click_link_by_partial_text("FULL IMAGE")
    time.sleep(2)

    # create html object and run parser on it
    html = browser.html
    soup = bs(html, 'html.parser')

    # Save link for featured image as a variable
    link_end = soup.find('img', class_='fancybox-image')
    featured_image_url = "https://www.jpl.nasa.gov"+(link_end["src"])


    ## Mars Weather

    # visit Mars Weather Twitter page
    url3 = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url3)
    time.sleep(3)

    # create html object and run parser on it
    html = browser.html
    weather_soup = bs(html, 'html.parser')

    # Save latest weather tweet as variable
    mars_weather = weather_soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    time.sleep(2)

    ## Mars Facts

    # visit Mars Facts page
    url4 = "http://space-facts.com/mars/"
    browser.visit(url4)
    time.sleep(3)

    # create list of table data
    tables = pd.read_html(url4)
    tables
    time.sleep(2)

    # convert list to dataframe
    mars_df = tables[0]
    mars_df

    # convert dataframe to html
    mars_table = mars_df.to_html()
    mars_table

    # remove \n's by replacing with ''
    mars_table.replace('\n', '')

    # add variables to mars_data dictionary with keys
    mars_data["src"] = featured_image_url
    mars_data["headline"] = news_title
    mars_data["text"] = news_p
    mars_data["weather"] = mars_weather
    mars_data["facts"] = mars_table

    return mars_data




# ## Step 2 - MongoDB and Flask Application
# 
# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
# 
# * Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
# 
# * Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.
# 
#   * Store the return value in Mongo as a Python dictionary.
# 
# * Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.
# 
# * Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.
# 
# ![final_app_part1.png](Images/final_app_part1.png)
# ![final_app_part2.png](Images/final_app_part2.png)
# 
# * Finally, deploy your Flask app to Heroku.
