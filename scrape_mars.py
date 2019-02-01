
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome',**executable_path, headless=False)
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    mars_data = {}
    # Create BeautifulSoup object; parse with 'html'
    soup = BeautifulSoup(html, 'html.parser')
    # # Loop through results to retrieve article title and paragraph
    latest_news = {}
    items = soup.find_all('li',class_='slide')
    item = items[0]
    div = item.find('div',class_='content_title')
    link = div.find('a')
    title = link.text.strip()
    article = item.find('div', class_='article_teaser_body')
    date = item.find('div', class_ ="list_date").get_text()
    mars_data['title'] = title
    mars_data['article'] = article.text.strip()
    mars_data['date'] = date

    # JPL Mars Space Images - Featured Image
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    image_html = browser.html
    soup = BeautifulSoup(image_html,'html.parser')
    ul = soup.find('div',class_='carousel_container')
    images = ul.find_all('div',class_='carousel_items')
    image = images[0]
    image_a = image.find('article',class_='carousel_item')
    image_href = image_a.get('style')
    clean_href = image_href.split("'")
    url_original = 'https://www.jpl.nasa.gov'
    mars_data['featured_image_url'] = url_original + clean_href[1]
    #Mars facts scraping
    mars_facts_url = 'http://space-facts.com/mars/'
    facts_table = pd.read_html(mars_facts_url)
    #convert table to DF, give column header and print
    mars_facts_df = facts_table[0]
    mars_facts_df.columns = ['Facts', 'Values']
    mars_facts_df
    # Save html code to folder Assets
    data = mars_facts_df.to_html()
    # Dictionary entry from MARS FACTS
    mars_data['mars_facts'] = data

    #Mars weather scraping
    mars_twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_twitter_url)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    parent_ol = soup.find_all('div', class_='js-tweet-text-container')
    weather_li = parent_ol[1].find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    mars_weather = weather_li.text.strip()
    mars_data['mars_weather'] = mars_weather
    # print(mars_weather)
    #Mars Hemisphere
    hemisphere_url = 'https://www.lpi.usra.edu/education/explore/mars/background/'
    base_url = "https://www.lpi.usra.edu/education/explore/mars/background/"
    browser.visit(hemisphere_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    parent_div = soup.find('div', id = 'main')
    contents = parent_div.find_all('p', class_="center")
    hemisphere_url = []
    for content in contents:
        img = content.find('img').get('src')
        desc = content.find('img').get('alt')
        img_url = base_url + img
        hemisphere_url.append({"Description" : desc, "img_url" : img_url})
    mars_data['hemisphere'] = hemisphere_url
    # Close the browser after scraping
    browser.quit()
    return mars_data
    # print(mars_data)
if(__name__=='__main__'):
    print(scrape())
