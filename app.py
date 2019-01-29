from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_mars"
mongo = PyMongo(app)
# connect to mongo db and collection

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # find data from mongoDB
    details = mongo.db.mars_data.find_one()

    # render templated data on brower
    return render_template("index.html", mars_info=details)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # Run the scrape function
    scraped_mars_data = scrape_mars.scrape()
    # Update the Mongo database using update and upsert=True
    mongo.db.mars_data.update({}, scraped_mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)