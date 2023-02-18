import requests
from pprint import pprint


class YaUploader:
    file_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    @property
    def headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }

    def get_upload_link(self, file_path):
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(self.upload_url, params=params, headers=self.headers)
        jsonify = response.json()
        pprint(jsonify)
        return jsonify

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self.get_upload_link(file_path).get("href")
        if not href:
            return

        with open(file_path, 'rb') as file:
            response = requests.put(href, data=file)
            if response.status_code == 201:
                print("Файл загружен")
                return True
            print("Файл не загружен. Ошибка", response.status_code)
            return False


def get_token(file):
    with open(file, 'r') as open_token:
        return open_token.readline()


if __name__ == '__main__':
    path_to_file = 'test.txt'
    token = 'token.txt'
    client = YaUploader(get_token(token))
    client.get_upload_link(path_to_file)
    client.upload(path_to_file)
    