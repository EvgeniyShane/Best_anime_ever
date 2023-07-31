import requests
from bs4 import BeautifulSoup
import json

link = "https://shikimori.me/animes?search=Gintama"
headers={'User-Agent': 'Mozilla/5.0'}
# page = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})

def get_titles(link):
    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        title_elements = soup.select("a > span.title")
        print(title_elements)
        title_list = []

        for title_element in title_elements:
            title = title_element.text.strip()
            title_list.append(title)

        return title_list

    else:
        print(f"Ошибка при получении страницы. Код ошибки: {response.status_code}")
        return []

titles = get_titles(link)
data = {"Titles": titles}
with open("result.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Результаты успешно сохранены в файл 'result.json'.")