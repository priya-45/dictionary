# import requests
import requests
URL = "https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
sample = requests.get(URL)
from bs4 import BeautifulSoup
soup = BeautifulSoup(sample.text,"html.parser") # iss object ke throw hum kahi bhi khel sakte hai
Title = soup.title

print(Title)#ye apke web page ka title print karega