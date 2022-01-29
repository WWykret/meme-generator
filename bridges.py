from PIL import Image

class IUiBridge:
    def try_to_login(username: str, password: str, save_credentials: bool) -> bool:
        pass

    def is_logged_in(self) -> bool:
        pass

    def next(self) -> Image:
        pass

    def prev(self) -> Image:
        pass

    def rand(self) -> Image:
        pass

    def filter(self, filter_str: str) -> Image:
        pass

    def compile(self, text0: str, text1: str) -> Image:
        pass

    def save(self) -> None:
        pass