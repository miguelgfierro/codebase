from pytrends.request import TrendReq
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


GOOGLE_END_POINT = "http://www.google.com/search"


class GoogleTrend(object):
    """Gets the Google trends of a set of terms
    
    Args:
        keywords (list): List of terms to search.
    """

    def __init__(self, keywords):
        self.keywords = keywords
        self.pytrend = TrendReq()
        self.pytrend.build_payload(kw_list=self.keywords, timeframe="today 5-y")

    def interest_over_last_5years(self):
        """Returns the interest in the last 5 years in a monthly basis: 260 results"""
        df = self.pytrend.interest_over_time()
        return df

    def interest_over_last_year(self):
        """Returns the interest in the last year in a monthly basis: 52 results"""
        self.pytrend.build_payload(kw_list=self.keywords, timeframe="today 12-m")
        df = self.pytrend.interest_over_time()
        return df

    def interest_by_city(self):
        """Returns interest in 50 cities"""
        df = self.pytrend.interest_by_region(resolution="CITY")
        return df

    def interest_by_country(self):
        """Returns interest in 52 countries"""
        df = self.pytrend.interest_by_region(resolution="COUNTRY")
        return df

    def number_google_results(self):
        """Return the approximate number of results in Google"""
        results = {}
        for key in self.keywords:
            r = requests.get(
                GOOGLE_END_POINT, params={"q": '"' + key + '"', "tbs": "li:1"}
            )
            soup = BeautifulSoup(r.text)
            number_text = soup.find("div", {"id": "resultStats"}).text
            number = re.sub("\D", "", number_text)
            results[key] = number
        df = pd.DataFrame([results])
        return df

