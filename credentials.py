from typing import Tuple
import json
import os.path
from loggers import ILogger

class ICredentialManager:
    def __init__(self, logger: ILogger) -> None:
        pass

    def try_to_login(self, username: str, password: str) -> bool:
        pass

    def save_credentials(self, username: str, password: str) -> None:
        pass

    def load_credentials(self) -> Tuple[str, str]:
        pass

class LocalCredentialManager(ICredentialManager):
    def __init__(self, logger: ILogger):
        self.logger = logger
        self.credential_file = 'credentials.json'

    def try_to_login(self, username: str, password: str) -> bool:
        if (not username or not password):
            return False

        return True

    def save_credentials(self, username: str, password: str) -> None:
        data = {
            'username': username,
            'password': password
        }
        with open(self.credential_file, 'w') as cred_file:
            json.dump(data, cred_file)

    def load_credentials(self) -> Tuple[str, str]:
        if os.path.isfile(self.credential_file):
            with open(self.credential_file, 'r') as cred_file:
                data = json.load(cred_file)
                try:
                    return data['username'], data['password']
                except KeyError:
                    self.logger.log('credentials file corrupted!', include_date=True)
        
        return None, None