
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

    # Create BeautifulSoup object; parse with 'html'
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve the parent divs for all articles
    results = soup.find_all('li', class_='slide')
    # Loop through results to retrieve article title and paragraph
    news_title = []
    news_p = []
    for result in results:
        div = result.find('div',class_='content_title')
        link = div.find('a')
        news_title.append(link.text.strip())
        paragraph = result.find('div',class_='article_teaser_body')
        news_p.append(paragraph.text.strip())

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
    featured_image_url = url_original + clean_href[1]
    #Mars facts scraping
    mars_facts_url = 'http://space-facts.com/mars/'
    facts_table = pd.read_html(mars_facts_url)
    #Mars weather scraping
    mars_twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_twitter_url)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    parent_ol = soup.find('ol',id='stream-items-id')
    weather_li = parent_ol.find_all('li')
    latest_weather = weather_li[0]
    latest_weather_p = latest_weather.find('p')
    mars_weather = latest_weather_p.text.strip()
    #Mars Hemisphere
    hemisphere_url = 'https://www.lpi.usra.edu/education/explore/mars/background/'
    base_url = "https://www.lpi.usra.edu/education/explore/mars/background/"
    browser.visit(hemisphere_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    parent_div = soup.find('div', id = 'main')
    contents = parent_div.find_all('p', class_="center")
    contents
    images = dict.fromkeys(['Description', 'img_url'])
    images_desc = []
    images_url = []
    for content in contents:
        img = content.find('img').get('src')
        desc = content.find('img').get('alt')
        img_url = base_url + img
        images_desc.append(desc)
        images_url.append(img_url)

    mars_data = {
        "News_Title": news_title,
        "Paragraph":news_p,
        "Image_url":featured_image_url,
        "Latest_Weather": mars_weather,
        "Mars_Facts": facts_table,
        "Mars_Image_Desc":images_desc,
        "Mars_Image_URL": images_url
    }


    # Close the browser after scraping
    browser.quit()
    return mars_data

if(__name__=='__main__'):
    print(scrape())
