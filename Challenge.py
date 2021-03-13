
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# Mac users
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')


slide_elem.find("div", class_='content_title')


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### JPL Space Images Featured Image


# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'

browser.visit(url)


# Find and click the full image button
# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup\n",
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# find the relative image url\n",
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Use the base url to create an absolute url\n",
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space{img_url_rel}'
img_url


# ### ### Mars Facts


df = pd.read_html(
    'https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]

df.head()


df.columns = ['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


df.to_html()


# ### Mars Weather


# Visit the weather website\n",
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)

# Parse the data\n",
html = browser.html
weather_soup = soup(html, 'html.parser')


# Scrape the Daily Weather Report table\n",
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres


# 1. Use browser to visit the URL \n",
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# 2. Create a list to hold the images and titles.\n",
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.\n",
links = browser.find_by_css('a.product-item img')

for i in range(len(links)):
    hemisphere = {}

    # Find elements going to click link.
    browser.find_by_css('a.product-item img')[i].click()

    # Find sample image link
    sample_element = browser.links.find_by_text('Sample').first

    # Get hemisphere Title
    hemisphere['img_url'] = sample_element['href']

    # Get hemisphere Title
    hemisphere['title'] = browser.find_by_css('h2.title').text

    # Add Objects to hemisphere_image_urls list
    hemisphere_image_urls.append(hemisphere)

    # Go Back
    browser.back()


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


browser.quit()
