from ui import App
from api import ApiConnector
from credentials import LocalCredentialManager
from loggers import LocalLogger
from savers import LocalSaver

if __name__ == '__main__':
    logger = LocalLogger()
    credential_manager = LocalCredentialManager(logger)
    saver = LocalSaver()
    app = App(ApiConnector(credential_manager, saver, logger))