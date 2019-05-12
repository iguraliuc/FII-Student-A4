import os
import json
import datetime

insert_command = "INSERT INTO news(title, body, author_name, category, published_time, expire_time, source) VALUES("

MONTH = {
    'ianuarie': 1,
    'februarie': 2,
    'martie': 3,
    'aprilie': 4,
    'mai': 5,
    'iunie': 6,
    'iulie': 7,
    'august': 8,
    'septembrie': 9,
    'octombrie': 10,
    'noiembrie': 11,
    'decembrie': 12,
}

def get_real_data():
    commands = []
    #commands.append("CREATE INDEX ir_translation_ltns ON news ((md5(body)))")
    for f in os.listdir(os.path.join(os.getcwd(), 'jsons')):
        fpath = os.path.join(os.getcwd(), 'jsons', f)
        with open(fpath, 'rb') as fin:
            jfile = json.loads(fin.read().decode('utf-8'))
            jfile['content'] = jfile['content'].replace('\'', '')
            if 'FII' in jfile['source']:
                day = int(jfile['date'].split(' ')[0])
                month = MONTH[jfile['date'].split(' ')[1].split(',')[0]]
                year = int(jfile['date'].split(' ')[2])
                published_date = datetime.datetime(year=year, month=month, day=day)
                valabil_date = datetime.datetime(year=2020, month=month, day=day)
            elif 'UAIC' in jfile['source']:
                day = int(jfile['date'].split(' ')[0])
                month = MONTH[jfile['date'].split(' ')[1].split(',')[0]]
                year = int(jfile['date'].split(' ')[2])
                published_date = datetime.datetime(year=year, month=month, day=day)
                valabil_date = datetime.datetime(year=2020, month=month, day=day)
            elif 'ORAR' in jfile['source']:
                day = int(jfile['publish_date'].split('.')[0])
                month = int(jfile['publish_date'].split('.')[1])
                year = int(jfile['publish_date'].split('.')[2])
                published_date = datetime.datetime(year=year, month=month, day=day)
                day = int(jfile['valabil_date'].split('.')[0])
                month = int(jfile['valabil_date'].split('.')[1])
                year = int(jfile['valabil_date'].split('.')[2])
                valabil_date = datetime.datetime(year=year, month=month, day=day)

            #contor = News.objects.raw('SELECT COUNT(*) FROM news WHERE body=\'' + jfile['content']+'\'');
            #print(contor);

            new_command = insert_command + '\'' + jfile['title'] + '\', \'' + jfile['content'] + \
                            '\', \'\', \'\', \'' + str(published_date) + '\', \'' + str(valabil_date) + '\',' + '\'' + jfile['source'] + '\') '
            # print(new_command)
            commands.append(new_command)
            # return commands
    return commands


if __name__ == "__main__":
    get_real_data()

