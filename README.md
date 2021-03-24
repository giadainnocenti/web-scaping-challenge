# web-scraping-challenge
This challenge was divided in two steps: Scraping and creation of an HTML page using MongoDB and Flask Application. /
The ultimate goal is the development of a web application that scrapes various websites to retrieve data related to the Mission to mars and displays the information in a single HTML page.

# 1. Scraping
The scraping script was optimized using [Jupyter notebook](./Mission_to_Mars/mission_to_mars.ipynb). The notebook was then exported as a [python script](./Mission_to_Mars/scrape_mars.py) and adapted to be run as a function. /
The developed scripts uses [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [splinter](https://splinter.readthedocs.io/en/latest/) and [pandas](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html).
The following websites were scraped:
 * [NASA](https://mars.nasa.gov/news/)
    The latest news information was scraped.
 * [JPL Mars Space Images](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html)
    The featured Image was scraped.
 * [Mars Facts](https://space-facts.com/mars/)
    The table containing Mars information was scraped.
 * [Mars Hemispheres](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
    High resolution images of each of Mars' hemisphere were scraped.
# 2. MongoDB and Flask Application
