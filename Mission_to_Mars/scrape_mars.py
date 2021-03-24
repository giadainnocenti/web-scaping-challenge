import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser


url_nasa = 'https://mars.nasa.gov/news/'
url_jpl = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
url_mars_facts = 'https://space-facts.com/mars/'
url_hemisphere = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

def visit_check_url(url, browser_to_use = 'chrome', text_check = 'Mars'):
    #set up the browser to use
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser(browser_to_use, **executable_path, headless=False)
    #visit the given url
    browser.visit(url)
    #it returns a positive message if there is text in the url and a negative one if it is empty
    if browser.is_text_present(text_check):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found...")
    return(browser)
 
def get_NASA(url_nasa=url_nasa):
    #check if you can find the website
    browser = visit_check_url(url_nasa)
    #creating a BEautifulSoup object
    soup = bs(browser.html, 'html.parser')
    #reading the latest News Title
    news_title = soup.find_all('div', class_='content_title')[0].text
    #reading the latest news body
    paragraph = soup.find_all('div', class_="article_teaser_body")[0].text   
    browser.quit()
    return news_title, patagraph

def get_JPL(url_jpl=url_jpl):
    #check if you can find the website
    browser = visit_check_url(url_jpl)
    #clicking on the button FULL IMAGE to see the full image featured this month  class="btn btn-outline-light"
    browser.links.find_by_partial_text('FULL IMAGE').click()
    #scraping the page with BS
    soup = bs(browser.html, 'html.parser')
    #saving the image url, sometimes it does not find mars3.jpg I am not sure why
    featured_image_url = url_jpl.replace("index.html", soup.find(class_="fancybox-image")["src"]) 
    browser.quit()
    return (featured_image_url)

def get_facts(url_mars_facts=url_mars_facts):
    #check if you can find the website
    browser = visit_check_url(url_mars_facts)
    browser.quit()
    # reading the table from the url using pandas
    table = pd.read_html(url_mars_facts)
    #selecting the table containing Mars information
    df_facts = table[0]
    #renaming the columns
    df_facts.columns = ['Description', 'Value']
    #saving the table as an HTML and stripping \n character not known by html.
    html_facts = df_facts.to_html(classes="table table-dark")
    html_facts = html_facts.replace('\n','')
    return(df_facts, html_facts)

def get_hemispheres(url_hemisphere=url_hemisphere):
    browser = visit_check_url(url_hemisphere)
    html = browser.html
    #check if you can find the website
    soup = bs(html, 'html.parser')
    #finding all the items and possible images
    items = soup.find_all(class_='item')
    #getting information on the images such as title and urls to find the full image
    hemispheres = []
    for item in items:
        item_dic = {}
        #finding the titles of the images
        title = item.find('h3').text
        item_dic['Title'] = title
        #clicking in every image to retrieve the full size picture
        browser.links.find_by_partial_text(title).click()
        html = browser.html
        soup = bs(html, 'html.parser')
        #finding the urls of the picture
        url_1 = soup.find('div', class_='downloads')
        url = url_1.find('a')['href']
        item_dic['img_url'] = url
        browser.back()
        hemispheres.append(item_dic)
        browser.quit()
        return(hemispheres)

def scrape():
    info ={}
    news_title, paragraph = get_NASA()
    info["news_title"]= news_title
    info["news_paragraph"]=news_p

    featured_image_url = get_JPL()
    info["Featured_image_url"] = featured_image_url

    df_facts, html_facts = get_facts()
    info['mars_facts'] = html_facts

    hemispheres_images_urls = get_hemispheres()
    info["full_image_hemisphere_urls"]=hemispheres_images_urls

    return info

    

    
    
    

