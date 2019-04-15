import os
import json

insert_command = "INSERT INTO news(title, body, author_name, category) VALUES("

def get_real_data():
    commands = []
    for f in os.listdir(os.path.join(os.getcwd(), 'jsons')):
        fpath = os.path.join(os.getcwd(), 'jsons', f)
        with open(fpath, 'rb') as fin:
            json_file = json.loads(fin.read())
            new_command = insert_command + '\'' + json_file['title'] + '\', \'' + json_file['content'] + '\', \'\', \'\')'
            # print(new_command)
            commands.append(new_command)
            # return commands
    return commands

if __name__ == "__main__":
    get_real_data()
