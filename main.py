import requests
from bs4 import BeautifulSoup

# Переменные которые мы будем использовать
url = 'https://rostov.hh.ru/search/vacancy?clusters=true&area=76&enable_snippets=true&salary=&st=searchVacancy&text=python&page=1'
# 1 Установить requests
# 2 Установить Beautifulsoup4
# 3 Установить lxml
# Передаем заголовки, для того что бы браузер не подумал что мы бот
headers = {
    "Accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


# Получаем HTML страницу в виде текста
def get_html(url, headers=headers):
    print(repr(url))
    url = url.rstrip()
    r = requests.get(url)
    src = r.text
    print(src)
    # Сохраняем полученную страницу в файл т.к. многие сайты не любят когда их парсят. Так мы не прлучим бан
    # Нужно все максимально подробно указывать и наче не работает
    with open('index.html', mode='w', encoding='utf-8') as f:
        f.write(src)
    return src


def get_all_title(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('div', class_='list-wrap product-list')
    print(title)


def main():
    total = get_html(url)


# print(total)


if __name__ == '__main__':
    # try:
    main()
#
# except:
#     print('Опа')
