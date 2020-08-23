import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html')

soup = BeautifulSoup(webpage.content, 'html.parser')
print(soup)
rating_tags = soup.find_all(attrs={"class": "Rating"})
print(rating_tags)
ratings = []

for rating in rating_tags[1:]:
  ratings.append(float(rating.get_text()))
plt.hist(ratings)
plt.show()
plt.clf()
company_names = soup.find_all(attrs={'class': 'Company'})
print(company_names)
company = []
for name in company_names[1:]:
  company.append(name.get_text())

df = pd.DataFrame.from_dict({'Company': company, 'Rating': ratings})
average_group_ratings = df.groupby('Company').Rating.mean()
ten_best_rated = average_group_ratings.nlargest(10)
print(ten_best_rated)

cocoa_data = soup.select('.CocoaPercent')
cocoa_percents = []

for cp in cocoa_data[1:]:
  cocoa_percents.append(int(float(cp.string[:-1])))
print(cocoa_percents)

df['CocoaPercentage'] = cocoa_percents
print(df.head())

plt.scatter(df.CocoaPercentage, df.Rating)
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
plt.show()
