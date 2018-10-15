#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utility functions for scraping from IMDb.com w/ Beautiful Soup.

For Metis Weeks 2-3, Project Luther.

@author: Steven Bierer
Created on Sun Oct  7 12:19:54 2018
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime

#pd.options.display.float_format = '${:,.2f}'.format

def imdb_yearsoup(year, page):
    """ Return a B.Soup object for an IMDb search-by-title page. """
    
    # Given integer year and page number, contruct a url and call B.Soup #
    URL_LEAD = "https://www.imdb.com/search/title?title_type=feature&"
    URL_MID = "&certificates=US%3AG,US%3APG,US%3APG-13,US%3AR&sort=boxoffice_gross_us,desc&"
    str_date = f"release_date={year}-01-01,{year}-12-31"
    str_page = f"page={page}"
    
    url_ = URL_LEAD + str_date + URL_MID + str_page
    soup = BeautifulSoup(requests.get(url_).text, "html5lib")
    
    return soup


def imdb_titles(year):
    """Return dictionary of film titles and IMBb codes for a given year."""
    
    # Dictionary is in form {code: title}, so code can be used as a table key.    
    print(f'\nExtracting titles from {year}:')
 
    title_codes = {}
    MAXPAGE = 40  # a failsafe
    for pp in range(1,MAXPAGE+1):  # loop through pages until no titles are found
        soup = imdb_yearsoup(year,pp)
        film_headers = soup.find_all(class_='lister-item-header')
        
        if len(film_headers)==0:
            break
        print('.',end='')
        
        for i in range(len(film_headers)):
            code = film_headers[i].find('a')['href'].split('/')[2]
            title = film_headers[i].find('a').contents
            title_codes[code] = title

    print('\n')
    return title_codes


def imdb_titlesoup(film_code):
    """ Return B.Soup object for a single-title listing."""
    
    url_ = "https://www.imdb.com/title/" + film_code
    soup = BeautifulSoup(requests.get(url_).text, "html5lib")
    
    time.sleep(0.02)  # pause to minimize bot-identification
    return soup


def imdb_dataframe(year):
    """ Return dataframe with extracted data across titles."""
    
    title_dict = imdb_titles(year)  # dictionary of {code:title}
    print(f'Extracting info from {len(title_dict)} titles: ')
    
    info_dict = {}; cnt = 0
    for i in title_dict:
        # Info will be obtained from three divisions of webpage #
        soup_i = imdb_titlesoup(i)
        film_infoA = soup_i.find('div',id='titleStoryLine')
        film_infoB = soup_i.find('div',id='titleDetails')
        film_infoC = soup_i.find('div',class_='ratingValue')
        
        # Get values for each type of desired information #
        try:
            ibit = film_infoA.find(text=re.compile('Genres')).parent.parent
            genre_list = tuple(
                    item.text.strip() for item in ibit.findChildren('a')
                    )
        except:
            genre_list = None

        try:
            ibit = film_infoA.find(text=re.compile(
                    'Motion Picture Rating')).parent.parent
            rating = ibit.findChild('span').text
            rating = re.search('Rated (G|PG-13|PG-17|PG|R|NC-17)',rating)
            if rating:
                rating = rating.group(1)
            else:
                rating = 'UNRATED'
        except:
            rating = 'UNRATED'
        
        try:
            ibit = film_infoB.find(text=re.compile('Country')).parent.parent
            country = ibit.findChildren('a')[0].text.upper().strip()
        except:
            country = 'JUPITER'
        
        try:
            ibit = film_infoB.find(text=re.compile('Language')).parent.parent
            language = ibit.findChildren('a')[0].text.upper().strip()
        except:
            language = 'LATIN'

        try:
            ibit = film_infoB.find(text=re.compile('Release Date')).parent
            rdate_list = ibit.nextSibling.strip().split(' ')[:3]
            rdate = ' '.join(rdate_list)  # input format is e.g. 8 October 2008
            rdate = datetime.strptime(rdate, '%d %B %Y')
        except:
            rdate = None

        try:
            ibit = film_infoB.find(text=re.compile('Budget')).parent.parent
            budget = re.search('\$[\w,]*',ibit.text.strip())         # remove '$'
            budget = float(budget.group(0)[1:].replace(',',''))/1e6  # to $mil
        except:
            budget = None
        
        try:
            ibit = film_infoB.find(text=re.compile('Opening Weekend USA')).parent.parent
            opening = re.search('\$[\w,]*',ibit.text.strip())
            opening = float(opening.group(0)[1:].replace(',',''))/1e6
        except:
            opening = None
    
        try:
            ibit = film_infoB.find(text=re.compile('Gross USA')).parent.parent
            gross = re.search('\$[\w,]*',ibit.text.strip())
            gross = float(gross.group(0)[1:].replace(',',''))/1e6
        except:
            gross = None
        
        try:
            ibit = film_infoC.findNext()
            rating_strings = ibit.attrs['title'].split(' ')
            user_rating = float(rating_strings[0])
            count_rating = int(rating_strings[3].replace(',',''))
        except:
            user_rating = None
            count_rating = 0

        # Put information into dictionary form #
        info_dict[i] =  {'Genre' : genre_list,          # tuple of strings
                         'MPAA' : rating,               # string
                         'Country' : country,           # string
                         'Language' : language,         # string
                         'Rating_User' : user_rating,   # float (0.0-10.0)
                         'Rating_Count' : count_rating, # integer
                         'Release_Date' : rdate,        # datetime object
                         'Budget' : budget,             # float ($ millions)
                         'Sales_Opening' : opening,     # float ($ millions)
                         'Sales_Gross' : gross          # float ($ millions)
                         }
        cnt += 1
        if not cnt%50:
            print(f'{cnt} ',end='')
    
    # Create a final dataframe #
    df_title = pd.DataFrame.from_dict(      # unique imdb code gives index
            title_dict,orient='index',columns=['Title'])
    df_info = pd.DataFrame.from_dict(
            info_dict,orient='index')       # add movie title to the info
    df_total = pd.concat([df_title,df_info],axis=1,sort=True)
    df_total.index.name = 'Code'
        
    print('')
    return df_total
    # end imdb_dataframe()


# --------------------------------------------------------------------------

if __name__ == "__main__":
    # For debugging purposes #
    df_imdb2008 = imdb_dataframe(2003)


