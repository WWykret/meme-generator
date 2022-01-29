from bridges import IUiBridge
import json
import os.path
from PIL import Image
import requests
import random
from io import BytesIO

class ApiConnector(IUiBridge):
    def __init__(self):
        self.get_templates_from_filter('')

    def get_templates_from_filter(self, filter_str):
        all_tempaltes = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
        correct_box_templates = filter(lambda template: template['box_count'] == 2, all_tempaltes)
        self.templates = list(filter(lambda template: filter_str.lower() in template['name'].lower(), correct_box_templates))
        self.template_index = 0
        for i, tmp in enumerate(self.templates):
            print(i, tmp['name'])

    def try_to_login(self, username, password, save_credentials):
        if (not username or not password):
            return False

        print(username,password,save_credentials)
        self.username = username
        self.password = password
        
        if save_credentials:
            data = {'username':username, 'password':password}
            with open('credentials.json', 'w') as cred_file:
                json.dump(data, cred_file)

        return True

    def is_logged_in(self):
        if hasattr(self, 'username') and hasattr(self, 'password'):
            return True

        if os.path.isfile('credentials.json'):
            with open('credentials.json', 'r') as cred_file:
                data = json.load(cred_file)
                try:
                    self.username = data['username']
                    self.password = data['password']
                    return True
                except KeyError:
                    print('credentials file corrupted!')
        return False

    def get_current_template(self):
        response = requests.get(self.templates[self.template_index]['url'])
        return Image.open(BytesIO(response.content))

    def rand(self):
        self.template_index = random.randint(0, len(self.templates) - 1)
        return self.get_current_template()

    def next(self):
        self.template_index += 1
        if self.template_index >= len(self.templates):
            self.template_index = 0
        return self.get_current_template()

    def prev(self):
        self.template_index -= 1
        if self.template_index < 0:
            self.template_index = len(self.templates) - 1
        return self.get_current_template()

    def filter(self, filter_str):
        self.get_templates_from_filter(filter_str)
        if len(self.templates) == 0:
            return None
        return self.get_current_template()