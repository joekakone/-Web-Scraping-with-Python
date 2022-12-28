#!/usr/bin/env python
# coding: utf-8

# # Web Scraping with Python
# 
# 1. **BeautifulSoup** [[Notebook]](01_beautifulsoup.ipynb)
# 2. Scrapy [[Notebook]](02_scrapy.ipynb)
# 3. Selenium [[Notebook]](03_selenium.ipynb)
# 4. Pandas [[Notebook]](04_pandas.ipynb)
# 
# prepared by [Joseph Konka](https://www.linkedin.com/in/joseph-koami-konka/)

# ## Collect Job offers online with BeautifulSoup
# [Emploi.tg](https://www.emploi.tg/) is a job offers website. The task consist 
# 1. Get the list of available job offers
# 2. Extract job offers details
# 3. Export data to .json file

# ## Packages

# In[1]:


import json

import requests
from bs4 import BeautifulSoup
import pandas as pd


# ## Paths & Config

# In[2]:


BASE_URL = "https://www.emploi.tg/recherche-jobs-togo?page={}"
OUTPUT_FILE = "outputs/emploi_tg.json"


# ## Structure

# In[3]:


MOTHER_BALISE = "div"
MOTHER_CLASS = "search-results jobsearch-results"

ITEM_BALISE = "div"
ITEM_CLASS = "job-description-wrapper"
ITEM_TITLE_BALISE = "h5"
ITEM_RECRUTER_BALISE = "p"
ITEM_RECRUTER_CLASS = "job-recruiter"
SPLITER = "|"
ITEM_OVERVIEW_BALISE = "div"
ITEM_OVERVIEW_CLASS = "search-description"
ITEM_LINK_BALISE = "a"

WEBSITE_BALISE = "td"
WEBSITE_CLASS = "website-url"

FIELD_BALISE = "div"
FIELD_CLASS = "field-item even"

POSITION_MOTHER_BALISE = "div"
POSITION_MOTHER_CLASS = "ad-ss-title"
POSITION_BALISE = "strong"

CONTENT_BALISE = "div"
CONTENT_CLASS = "jobs-ad-details"


# ## Functions & Classes

# In[4]:


class BaseScraper(object):
    def __init__(self, params=None):
        self.params = params

    @staticmethod
    def get_source(url):
        # retreive source code 
        code = requests.get(url)

        return BeautifulSoup(code.text, "html.parser")

    def extract_item_details(self):
        raise NotImplementedError

    def get_items(self):
        raise NotImplementedError

    @staticmethod
    def save(data, path):
        # Save data
        print(f"Saving data at {path}")
        writer = pd.ExcelWriter(path)
        data.to_excel(writer, index=False, sheet_name="Offers")


# In[5]:


class EmploiTogoScraper(BaseScraper):
    def __init__(self, params=None):
        super().__init__(params=params)

    def get_item_details(self, url):
        print("->", url)
        soup = self.get_source(url)
        field = soup.find(FIELD_BALISE, {"class": FIELD_CLASS}).text
        content = soup.find(CONTENT_BALISE, {"class": CONTENT_CLASS}).text.strip()

        details = {
            "field": field,
            "content": content
        }
        return details

    def get_items(self, soup):
        soup_items = soup.find_all(ITEM_BALISE, {"class": ITEM_CLASS})
        items = []
        for soup_item in soup_items:
            title = soup_item.find(ITEM_TITLE_BALISE).text
            recruter = soup_item.find(ITEM_RECRUTER_BALISE, {"class": ITEM_RECRUTER_CLASS})
            date, recruter = recruter.text.split(SPLITER)
            date, recruter = date.strip().replace(".", "/"), recruter.strip()
            url = soup_item.get("data-href")
            overview = soup_item.find(ITEM_OVERVIEW_BALISE, {"class": ITEM_OVERVIEW_CLASS}).text
            details = self.get_item_details(url)
            items.append(
                {
                    "title": title,
                    "url": url,
                    "recruter": recruter,
                    "date": date,
                    "overview": overview,
                    "content": details["content"]
                }
            )
        return items


# ## Start collecting data

# In[6]:


scraper = EmploiTogoScraper()


# In[7]:


jobs = []
i = 0
while True:
    soup = scraper.get_source(BASE_URL.format(i))
    try:
        # Pagination
        items = scraper.get_items(soup)
        assert len(items) > 0
        jobs.extend(items)
        i += 1
    except:
        break


# ## Save data to .json

# In[8]:


with open(OUTPUT_FILE, 'w') as f:
    json.dump(jobs, f, ensure_ascii=True, indent=4)


# ## Load job offers from json file

# In[9]:


dt = pd.read_json(OUTPUT_FILE)
dt.head()


# ## Let get in touch
# [![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/joekakone)](https://github.com/joekakone) [![Facebook Badge](https://img.shields.io/badge/-Facebook-blue?style=flat-square&logo=Facebook&logoColor=white&link=https://www.facebook.com/joekakonepage)](https://www.facebook.com/joekakonepage) [![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/joseph-koami-konka/)](https://www.linkedin.com/in/joseph-koami-konka/) [![Twitter Badge](https://img.shields.io/badge/-Twitter-blue?style=flat-square&logo=Twitter&logoColor=white&link=https://www.twitter.com/joekakone)](https://www.twitter.com/joekakone) [![Gmail Badge](https://img.shields.io/badge/-Gmail-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:joseph.kakone@gmail.com)](mailto:joseph.kakone@gmail.com)
