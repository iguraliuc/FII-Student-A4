import requests
import json
import re
from lxml.html import fromstring


BASE_URL = r"https://profs.info.uaic.ro/~orar/"
ORAR_URL = r"https://profs.info.uaic.ro/~orar/orar_profesori.html"


def generate_orare():

    request = requests.get(ORAR_URL)
    data = request.text
    site_title = re.findall(r'<li><a href="([^"]+)">\s*([^<]+)</a>', data)
    # print(site_title)
    # site_title = [BASE_URL + x[0] for x in site_title]
    for item in site_title:
        item = list(item)
        item[0] = BASE_URL + item[0]
        # print(item[0])
        # print(item[1])
        get_orare(item[0], item[1])

def get_orare(site, title):

    print(site)
    r = requests.get(site)
    # print(r.text)
    page = fromstring(r.text)
    # print(page)
    try:
        rows = page.xpath("body/table")[1].findall("tr")
    except:
        return {}
    data = list()
    for row in rows:
        data.append([c.text_content() for c in row.getchildren()])

    print(data)

    y = []
    for row in data:
        z = []
        for item in row:
            # print(item)
            item = re.sub(r'\r\n', '', item).strip()
            z.append(item)
        y.append(z)
        # print(item)

    # print(y)

    days = ['Luni', 'Marti', 'Miercuri', 'Joi', 'Vineri', 'Sambata', 'Duminica']
    index = []
    for i in range(len(y)):
        # print()
        if y[i][0].split(',')[0] in days:
            index.append(i)
    index.append(len(y))
    all_days = []
    for i in range(len(index) - 1):
        all_day = []
        for j in range(index[i], index[i + 1]):
            all_day.append(y[j])
        all_days.append(all_day)
    # print(index)
    # print(all_days)

    final_dict = {}
    final_dict['title'] = re.sub('\s+', ' ', title).strip()
    for item in all_days:
        day_dict = {}
        # print(item)
        day_dict['zi'] = item[0][0].split(',')[0]

        # item[0][0]
        for i in range(1, len(item)):
            # print(len(item[i]))
            subject_dict = {}
            subject_dict['incepe'] = item[i][0]
            subject_dict['termina'] = item[i][1]
            # subject_dict['grupa'] = re.sub(r'\s+', '', item[i][2])
            subject_dict['disciplina'] = item[i][2]
            subject_dict['tip'] = item[i][3]
            subject_dict['studenti'] = re.sub('\s+', ' ', item[i][4]).strip()
            subject_dict['sala'] = re.sub('\s+', ' ', item[i][5]).strip()
            subject_dict['pachet'] = item[i][6]

            day_dict['materie {}'.format(i)] = subject_dict
        final_dict['examen {}'.format(item[0][0])] = day_dict
        # print(day_dict)

    print(final_dict)
    with open(r'./orare_profesori_examen/{}'.format(final_dict['title']), 'w') as f:
        json.dump(final_dict, f, indent=4)
    f.close()

generate_orare()


# generate_orare()