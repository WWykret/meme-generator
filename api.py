from bridges import IUiBridge

class ApiConnector(IUiBridge):

    def try_to_login(self, username, password, save_credentials):
        if (not username or not password):
            return False

        print(username,password,save_credentials)
        self.username = username
        self.password = password
        
        if save_credentials:
            pass

        return True

    def is_logged_in(self):
        if hasattr(self, 'username') and hasattr(self, 'password'):
            return True

        return False