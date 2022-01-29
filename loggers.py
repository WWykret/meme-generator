from datetime import datetime

class ILogger:
    def log(self, msg: str, include_date: bool) -> None:
        pass

class LocalLogger(ILogger):
    def __init__(self) -> None:
        self.log_file = 'logs.txt'

    def log(self, msg: str, include_date: bool = True) -> None:
        with open(self.log_file, 'a') as logs:
            if include_date:
                now = datetime.now()
                logs.write(f'{now.strftime("%d/%m/%Y %H:%M")} --- {msg}\n')
            else:
                logs.write(f'{msg}\n')