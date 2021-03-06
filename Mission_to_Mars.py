
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd

# Path to chromedrive
#!which chromedriver
# Mac users
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


def mars_news(browser):
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    # news=""
    html = browser.html
    news_soup = soup(html, 'html.parser')

  # Add try/except for error handling
  try:

    slide_elem = news_soup.select_one('ul.item_list li.slide')

    # Assign the title and summery text to veriable
    slide_elem.find("div", class_='content_title')

    # Use the parent element to find the first #'a'tag snd save it as
    # news_title
    news_title = slide_elem.find("div", class_='content_title').get_text()
    news_title

    # Use the parent element to find the paragraph #text
    new_p = slide_elem.find('div', class_="article_teaser_body").get_text()
    new_p

  except AttributeError:
    return None, None

    return news_title, new_p

def featured_image(browser):

    # JPL Special Featured Images Featuere Image
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

  # Add try/except for error handling
  try:

    # Find the relative image url
    img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    img_url_rel

  except AttributeError:
    return None
    # Use the base URL to create an absolute URL
    img_url = f'https// data-clsss-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url


def mars_facts():

  try:
    # Use 'read_html' to scrape the facts table into a dataframe
    df = pd.read_html('http://space-facts.com/mars/')[0]


  except BaseException:
    return Non
    # Mars Facts
    df.columns = ['description', 'value']
    df.set_index('description', inplace=True)
    df

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()


    browser.quit()
