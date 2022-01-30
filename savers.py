from PIL import Image
import os.path

class IImageSaver:
    def save_image(self, img: Image) -> None:
        pass

class LocalSaver(IImageSaver):
    def __init__(self) -> None:
        self.save_dir = 'saved_memes'
        self.save_prefix = 'meme'
        self.save_extension = 'jpg'

    def save_image(self, img: Image) -> None:
        if not os.path.isdir(self.save_dir):
            os.makedirs(self.save_dir)

        counter = 1
        while os.path.isfile(f'{self.save_dir}/{self.save_prefix}{counter}.{self.save_extension}'):
            counter += 1

        img.save(f'{self.save_dir}/{self.save_prefix}{counter}.{self.save_extension}')