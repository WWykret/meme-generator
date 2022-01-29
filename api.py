from bridges import IUiBridge
import json
import os.path

class ApiConnector(IUiBridge):

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