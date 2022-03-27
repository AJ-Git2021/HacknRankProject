from Google import CREATE_SERVICE, convert_to_RFC_datetime

CLIENT_SECRETE_FILE = 'client_secret_file.json'
API_NAME = 'tasks'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/tasks']

service = CREATE_SERVICE(CLIENT_SECRETE_FILE,API_NAME,API_VERSION,SCOPES)
print(dir(service))