from ui import App
from api import ApiConnector
from credentials import LocalCredentialManager

if __name__ == '__main__':
    credential_manager = LocalCredentialManager()
    app = App(ApiConnector(credential_manager))