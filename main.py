import requests
from bs4 import BeautifulSoup

url = "https://uk.indeed.com/jobs?q=junior+developer&l=United+Kingdom"

response = requests.get(url)

data = response.text 

soup = BeautifulSoup(data, "html.parser")

tags = soup.find_all("a")

