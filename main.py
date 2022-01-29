from ui import App
from api import ApiConnector
from credentials import LocalCredentialManager
from loggers import LocalLogger

if __name__ == '__main__':
    logger = LocalLogger()
    credential_manager = LocalCredentialManager(logger)
    app = App(ApiConnector(credential_manager, logger))