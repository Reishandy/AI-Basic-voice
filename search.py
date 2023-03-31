import requests
from bs4 import BeautifulSoup


def search(text):
    # Setting up
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
    }
    url = 'https://www.google.com/search?lr=lang_en&q=' + text.replace(" ", "+")
    soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')
    result = ''

    if ' ' not in text:
        try:
            result += ' ' + soup.find('div', class_='kno-rdesc').text
        except:
            pass

    # Try to get result
    try:
        result += ' ' + soup.find('span', class_='hgKElc').text
    except:
        pass
    try:
        result += ' ' + soup.find('span', class_='Z0LcW t2b5Cf').text
    except:
        pass

    if result == '':
        try:
            web_desc = soup.find('div', class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf').text
            if '—' in web_desc:
                web_desc = web_desc.split('—')[1]
            if '...' in web_desc:
                web_desc = web_desc.split('.')[0]
            result += ' ' + web_desc
        except:
            pass

    if result == '':
        return 'Unfortunately I cannot find the result'
    return result


if __name__ == '__main__':
    print('module test...')
    # Example
    # print(search('how many stars are there in milky way'))
    # print(search('when is valentine'))
    # print(search('why does earth have water'))
    # print(search('how many days are in march'))
    # print(search('when will ramadan end'))
    print(search('youtube'))
