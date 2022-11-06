from bs4 import BeautifulSoup
import requests


def parse_text(subject_search, class_search, type_search):
    subject_sl = {
        'Биология': '11', 'География': '10', 'Информатика': '7', 'Математика': '6', 'Физика': '12', 'Химия': '13',
        'Астрономия': '20', 'ИЗО': '22', 'Искусство': '18', 'История': '8', 'Лингвистика': '24', 'Литература': '2',
        'ОБЖ': '16', 'Обществознание': '9', 'Предпринимательсво': '23', 'Право': '15', 'Психология': '28',
        'Робототехника': '27', 'Русский язык': '1', 'Технология': '17', 'Физкультура': '19', 'Черчение': '31',
        'Экология': '21', 'Экономика': '14',
        'Ин.языки': '3%5D=on&subject%5B32%5D=on&subject%5B25%5D=on&subject%5B30%5D=on&subject%5B29%5D=on&subject%5B35%5D=on&subject%5B26%5D=on&subject%5B4%5D=on&subject%5B5%5D=on&subject%5B34%5D=on&subject%5B0'
    }

    type_sl = {
        'Командные': '9', 'Личные': 'ind', 'Дистанционные': 'dist', 'Все': 'any'
    }

    URL = 'https://olimpiada.ru/activities?subject%5B' + subject_sl.get(
        subject_search) + '%5D=on&class=' + class_search + '&type=' + type_sl.get(
        type_search) + '&period_date=&period=year'
    result_search = ''
    result_text = list(set(parse(URL)))
    for elem in result_text:
        result_search += elem
    return result_search


def parse(url):
    URL = url
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/107.0.5304.88 Safari/537.36'
    }

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='fav_olimp olimpiada')
    comps = []
    result = []

    for item in items:
        comps.append({
            'title': item.find('span', class_='headline').get_text(strip=True),
            'class': item.find('span', class_='classes_dop').get_text(strip=True)
        })

        for comp in comps:
            result.append(f"Олимпиада: {comp['title']}, класс: {comp['class']}\n")
    return result




parse_text('Информатика', '11', 'Все')
