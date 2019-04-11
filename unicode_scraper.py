import csv
import requests
import time

from bs4 import BeautifulSoup as bs

BASE_URL = 'https://www.fileformat.info/info/unicode/category/{target}/list.htm'

LETTERS = ['Lu', 'Ll', 'Lo']

NUMBERS = ['Nd', 'Nl', 'No']

PUNCS = ['Pc', 'Pe', 'Pe']

FILE_CATEGORY = {
    'data/unicode_letters.csv': LETTERS,
    'data/unicode_numbers.csv': NUMBERS,
    'data/unicode_punctuations.csv': PUNCS,
}


def main():
    for filename, categories in FILE_CATEGORY.items():
        with open(filename, 'w') as f:
            fieldnames = ['category', 'unicode', 'name', 'browser']
            dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
            dict_writer.writeheader()
            for category in categories:
                url = BASE_URL.format(target=category)
                res = requests.get(url).content
                soup = bs(res, 'html.parser')
                rows = []
                table = soup.select('table > tbody')[0]
                for idx, row in enumerate(table.select('tr')):
                    cols = [each.text for each in row.select('td')[0:3]]
                    csv_row = {
                        'category': category,
                        'unicode': cols[0],
                        'name': cols[1],
                        'browser': cols[2]
                    }
                    rows.append(csv_row)
                dict_writer.writerows(rows)
                time.sleep(1)


if __name__ == '__main__':
    main()
