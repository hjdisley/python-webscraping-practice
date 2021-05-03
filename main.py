import requests
from bs4 import BeautifulSoup

url = "https://uk.indeed.com/jobs?q=junior+developer&l=United+Kingdom"

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, "html.parser")

tags = soup.find_all("a")

# for tag in tags:
#     print(tag.get('href'))

titles = soup.find_all("a", {"class": "jobtitle"})

for title in titles:
    print(title.text)

locations = soup.find_all("span", {"class": "location"})

for location in locations:
    print(location.text)

companies = soup.find_all("span", {"class": "company"})

for company in companies:
    print(company.text)

summaries = soup.find_all("div", {"class": "summary"})

for summary in summaries:
    print(summary.text)
