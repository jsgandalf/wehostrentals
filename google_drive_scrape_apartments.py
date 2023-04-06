import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set up Google Drive API client
def get_drive_api_client():
    creds = None
    try:
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json',
                                                                 ['https://www.googleapis.com/auth/drive'])
                creds = flow.run_local_server(port=0)

            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        return build('sheets', 'v4', credentials=creds)
        # Code to perform the Google Drive upload
    except HttpError as error:
        if error.resp.status == 403:
            # Refresh the access token
            os.remove('token.pickle')
            # Rerun the authentication flow and store the new credentials
        else:
            pass


def create_google_sheet(api_client, sheet_name):
    body = {
        'properties': {
            'title': sheet_name
        }
    }
    sheet = api_client.spreadsheets().create(body=body).execute()
    return sheet['spreadsheetId']

def write_data_to_sheet(api_client, spreadsheet_id, data):
    values = [['Name', 'URL', 'Phone Number']] + [[item['name'], item['url'], item['phone']] for item in data]
    body = {
        'values': values
    }
    result = api_client.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range='A1:C{}'.format(len(values)),
        valueInputOption='RAW',
        body=body
    ).execute()


#data = [
#    {'name': 'example', url': 'https://example.com', 'phone': '555-1234'},
#    {'name': 'example', 'url': 'https://example.org', 'phone': '555-5678'},
#]

def google_drive(data, sheet_name):
    # Authenticate and create the API client
    drive_api_client = get_drive_api_client()

    spreadsheet_id = create_google_sheet(drive_api_client, sheet_name)
    write_data_to_sheet(drive_api_client, spreadsheet_id, data)

    print(f'Successfully created Google Sheet "{sheet_name}" with ID "{spreadsheet_id}" and populated it with data.')