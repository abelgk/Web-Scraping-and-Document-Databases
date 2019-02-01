# Mission to Mars
Web app built with combination of flask, python, splinter, beautifulsoup, pymongo and bootstrap to scrape multiple websites to find data in relation to Mars Mission and render on a HTML page.

### Sites Scraped
- **NASA Mars News Site** - to collect the latest news title and paragraph

- **JPL Mars Space Images - Featured Image** - Used splinter to navigate the site and find the image url for the current Featured Mars Image

- **Mars Weather** - Visited the Mars Weather twitter account and scraped the latest Mars weather tweet from the page and saved the tweet text for the weather report.

- **Mars Facts** - Visited the Mars Facts webpage and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. Used Pandas to convert the data to a HTML table string.

- **Mars Hemispheres** - Visited the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres, found the image url to the full resolution image, saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys img_url and title, appended the dictionary with the image url string and the hemisphere title to a list.

### MongoDB and Flask Application
- Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
- converted the Jupyter notebook into a Python script that executes all of the scraping code from above and return one Python dictionary containing all of the scraped data.
- created a route to import the python script and call the required function.
- Stored the return value in MongoDB as a Python dictionary.
- Created a root route / to query our Mongo database and pass the mars data into an HTML template to display the data.
- Created a template HTML file called index.html that takes the mars data dictionary and display all of the data in the appropriate HTML elements.

### Libraries needed
- pandas
- splinter
- pymongo
- Flask
- requests
- beautifulsoup
