"""Case Detail Scraper

Scrape Case details from casenote.kr"""

import requests
from bs4 import BeautifulSoup


def case_scraper(request):
	"""Search request in casenote.kr and return outcome"""


	req = requests.get("https://casenote.kr/search/?q="+request)
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	issue = soup.find('div', {'class': 'issue'}).get_text()
	summary = soup.find('div', {'class': 'summary'}).get_text()

	return [issue, summary]





# //*[@id="mainbar"]/div[2]/div[2]
# print(case_scraper('98다22543'))