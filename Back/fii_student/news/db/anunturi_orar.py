import requests
import json
import re
from lxml.html import fromstring
import os
import html2text

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
jsons_director = os.path.join(SCRIPT_PATH, 'anon_orar')
if not os.path.isdir(jsons_director):
    os.mkdir(jsons_director)

BASE_URL = r"https://profs.info.uaic.ro/~orar/"
ORAR_URL = r"https://profs.info.uaic.ro/~orar/orar_studenti.html"

# counter = 1

# final_list = []
# profesori = []

def generate_anon():

    global final_list
    request = requests.get(ORAR_URL)
    data = request.text
    # site_title = re.findall(r'<ul>\s*<li><a href="([^"]+)">([^<]+)</a></li>', data)
    site_title = [
        ('participanti/orar_MIS.html', 'Master ingineria sistemelor soft'),
        ('participanti/orar_MLC.html', 'Master lingvistica computationala'),
        ('participanti/orar_MOC.html', 'Master optimizare computationala'),
        ('participanti/orar_MSD.html', 'Master sisteme distribuite'),
        ('participanti/orar_MSI.html', 'Master securitatea informatiei'),
        ('participanti/orar_I1.html', 'Informatica, anul 1'),
        ('participanti/orar_I2.html', 'Informatica, anul 2'),
        ('participanti/orar_I3.html', 'Informatica, anul 3')
    ]
    for item in site_title:
        print(item)
        item = list(item)
        item[0] = BASE_URL + item[0]
        get_anon(item[0], item[1])

def get_anon(site, title):

    dictionar = {}
    r = requests.get(site)
    response = r.text
    try:
        data = re.search(r'<h3>Anunturi</h3>\s*([^$]+</ul>)', response).group(1)
    except:
        return

    if data:

        dictionar['source'] = "Orar"
        dictionar['title'] = title
        publish_date = re.findall(r'<small>Publicat la ([^<]+)</small>', data)
        valabil_date = re.findall(r'<small>Anuntul este valabil '
                                              r'doar pana la\s*([^<]+)</small>', data)
        # dictionar['publish_date'] = re.findall(r'<small>Publicat la ([^<]+)</small>', data)
        # dictionar['valabil_date'] = re.findall(r'<small>Anuntul este valabil '
        #                                       r'doar pana la\s*([^<]+)</small>', data)
        # print(dictionar)
        content = re.findall(r'(<li>[^$]+?<br>[^$]+?<br>)', data)

        for i in range(len(publish_date)):
            dictionar['publish_date'] = publish_date[i]
            dictionar['valabil_date'] = valabil_date[i]
            # dictionar['content'] = html2text.html2text(content[i])
            dictionar['content'] = content[i]
            with open("./anon_orar/{}_{}".format(dictionar["title"], i), "w", encoding='utf-8') as f:
                json.dump(dictionar, f, indent=4, ensure_ascii=False)
            f.close()
generate_anon()