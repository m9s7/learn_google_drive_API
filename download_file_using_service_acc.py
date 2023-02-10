import io
import sys


def download_file(service, file_id):
    file = service.files().get(fileId=file_id, fields='*').execute()
    file_name = file['name']
    mimetype = file['mimeType']

    if mimetype == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        request = service.files().get_media(fileId=file_id)
        file = io.BytesIO(request.execute())
        print(f"{file_name}: {sys.getsizeof(file) / (1 << 10):,.0f} KB")

    return file
