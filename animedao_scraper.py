import requests
import csv
from bs4 import BeautifulSoup

base_url = "https://animedao.to/animelist/?genres%5B0%5D=Adventure&status%5B0%5D=&order%5B0%5D=&page="

# Define the number of pages to scrape
num_pages = 6

with open('anime_info.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Release Date', 'Badge Score'])

    for page in range(1, num_pages+1):
        url = base_url + str(page)
        response = requests.get(url)

        if response.ok:
            soup = BeautifulSoup(response.content, 'html.parser')
            anime_info = soup.find_all("div", class_="animeinfo")
            anime_titles = [div.find('span', class_='animename').text for div in soup.find_all('div', class_='animeinfo')]
            release_date_elements = soup.find_all('span', class_='badge year rounded-0')
            release_dates = [element.text.strip().split(' ')[-1] for element in release_date_elements]
            badge_score_elements = soup.find_all('span', class_='badge score rounded-0')
            badge_scores = [element.text.strip().split(' ')[-1] for element in badge_score_elements]

            for title, date, score in zip(anime_titles, release_dates, badge_scores):
                writer.writerow([title, date, score])





