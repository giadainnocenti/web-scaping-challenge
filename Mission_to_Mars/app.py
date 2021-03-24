from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
conn = "mongodb://localhost:27017/mission_to_mars"
client = PyMongo(app, uri=conn)

@app.route("/")
def index():
    mars = client.db.mars.find_one()
    return render_template( "index.html", mars=mars)

# This section does the scraping and updates the values in the db and posts to index.html
@app.route("/scrape")
def scraper():
    mars = client.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data,upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)