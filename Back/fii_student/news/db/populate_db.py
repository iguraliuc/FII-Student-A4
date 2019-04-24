import os
import json
import datetime

insert_command = "INSERT INTO news(title, body, author_name, category, published_time) VALUES("

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
    for f in os.listdir(os.path.join(os.getcwd(), 'jsons')):
        fpath = os.path.join(os.getcwd(), 'jsons', f)
        with open(fpath, 'rb') as fin:
            json_file = json.loads(fin.read())
            if 'FII' in json_file['source']:
                day = int(json_file['date'].split(' ')[0])
                month = MONTH[json_file['date'].split(' ')[1][:-1]]
                year = int(json_file['date'].split(' ')[2])
                published_date = datetime.datetime(year=year, month=month, day=day)
            else:
                published_date = "no_date"
            new_command = insert_command + '\'' + json_file['title'] + '\', \'' + json_file['content'] + \
                            '\', \'\', \'\', \'' + str(published_date) + '\')'
            # print(new_command)
            commands.append(new_command)
            # return commands
    return commands


if __name__ == "__main__":
    get_real_data()
