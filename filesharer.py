from filestack import Filelink, Client


class FileSharer:

    def __init__(self, filepath, api_key='AIMh72ZzHSEa1mDHz2g7Rz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):

        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath, intelligent=False)
        return new_filelink.url  # 'https://cdn.filestackcontent.com/FILE_HANDLE