from bridges import IUiBridge
from PIL import Image
import requests
import random
from io import BytesIO
from credentials import ICredentialManager
from loggers import ILogger
from savers import IImageSaver

class ApiConnector(IUiBridge):
    def __init__(self, credential_manager: ICredentialManager, saver: IImageSaver, logger: ILogger):
        self.url_to_save = None
        self.username = None
        self.password = None

        self.credential_manager = credential_manager
        self.saver = saver
        self.logger = logger
        
        self.api_endpoint = 'https://api.imgflip.com'
        self.get_templates_from_filter('')

    def get_templates_from_filter(self, filter_str):
        all_tempaltes = requests.get(f'{self.api_endpoint}/get_memes').json()['data']['memes']
        correct_box_templates = filter(lambda template: template['box_count'] == 2, all_tempaltes)
        self.templates = list(filter(lambda template: filter_str.lower() in template['name'].lower(), correct_box_templates))
        self.template_index = 0

    def try_to_login(self, username, password, save_credentials):
        if not self.credential_manager.try_to_login(username, password):
            return False

        self.username = username
        self.password = password
        
        if save_credentials:
            self.credential_manager.save_credentials(username, password)

        return True

    def is_logged_in(self):
        if self.username is not None and self.password is not None:
            return True

        self.username, self.password = self.credential_manager.load_credentials()

        return self.username is not None and self.password is not None

    def get_current_template(self):
        self.url_to_save = None
        response = requests.get(self.templates[self.template_index]['url'])
        return Image.open(BytesIO(response.content))

    def get_template(self, url):
        self.url_to_save = None
        response = requests.get(url)
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

    def compile(self, text0, text1):
        data = {
            'username':self.username,
            'password':self.password,
            'text0':text0,
            'text1':text1,
            'template_id':self.templates[self.template_index]['id']
        }
        response = requests.post(f'{self.api_endpoint}/caption_image', data).json()
        if not response['success']:
            self.logger.log(response['error_message'], include_date=True)
            return None

        meme = self.get_template(response['data']['url'])
        self.url_to_save = response['data']['url']
        return meme

    def save(self):
        if not self.url_to_save:
            return

        meme = self.get_template(self.url_to_save)

        self.saver.save_image(meme)