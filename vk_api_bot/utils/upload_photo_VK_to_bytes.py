"""Модуль загрузки медиа(картинок)"""

from io import BufferedReader, BytesIO

from vk_api import VkUpload
from vk_api.upload import FilesOpener


class FilesOpenerCustom(FilesOpener):
    """
    Класс контекст менеджер, родитель vk_api.upload.FilesOpener.
    Даёт возможность загружать в VK_API картинки из bytes
    """
    def __init__(self, paths, bim=None, key_format='file{}') -> None:
        super().__init__(paths, key_format)
        self.bim = bim

    def open_files(self) -> list:
        """
        Функция класса позволяет загружать в VK_API картинки из bytes
        """
        self.close_files()

        files = []

        for x, file in enumerate(self.paths):
            if hasattr(file, 'read'):
                f = file

                if hasattr(file, 'name'):
                    filename = file.name
                else:
                    filename = '.jpg'
            else:
                filename = file
                if self.bim:
                    file_bytes = BytesIO(self.bim)
                    f = BufferedReader(file_bytes)

                else:
                    f = open(filename, 'rb')
                self.opened_files.append(f)

            files.append(
                (self.key_format.format(x), ('file{}.{}'.format(x, "jpg"), f))
            )
        return files


class VkUploadCustom(VkUpload):
    """ Загрузка файлов через API (https://vk.com/dev/upload_files)

    :param vk: объект :class:`VkApi` или :class:`VkApiMethod`
    """
    def photo_messages(
            self,
            photos=None,
            bim: bytes = None,
            peer_id=None
    ):
        """ Загрузка изображений в сообщения
        :param photos: путь к изображению(ям) или file-like объект(ы)
        :type photos: str or list
        :param peer_id: peer_id беседы
        :param bim: картинка в байтах
        :type peer_id: int
        :type bim: bytes
        """
        url = self.vk.photos.getMessagesUploadServer(
            peer_id=peer_id
        )['upload_url']

        with FilesOpenerCustom(photos, bim) as photo_files:
            response = self.http.post(url, files=photo_files)

        return self.vk.photos.saveMessagesPhoto(**response.json())
