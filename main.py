from google.oauth2 import service_account
from googleapiclient.discovery import build

from download_file_using_service_acc import download_file
from list_files_using_service_acc import list_files_in_drive

creds = service_account.Credentials.from_service_account_file('credentials.json',
                                                              scopes=['https://www.googleapis.com/auth/drive'])

service = build('drive', 'v3', credentials=creds)

# ID of the file to be downloaded
file_id = '1U6GT1M01m1MvTvR7pQCIdm-z-rF0nESB'

list_files_in_drive(service)
download_file(service, file_id)

# to je to moze da pocne da se radi
# load into some excel python library and work your magic
