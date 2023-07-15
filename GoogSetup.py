import requests
from Google import Create_Service
import os
from InfoGetter import getInfo


def CreateGoogleSheet():

    CLIENT_SECRET_FILE = 'credentials.json'
    API_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    with open("resources/PoolNum.txt", "r") as f:
        lines = f.readlines()
    with open("resources/PoolNum.txt", "w") as f:
        num = int(lines[0])
        num = num + 1
        x = str(num)
        f.write(x)

    SPREADSHEET_ID = "1zi9UaJCWSYMNuePZS3JNNK6-XM7vz_pNgc0Dt0ikOfw"
    OLD_SHEET_ID = 1159631575
    NEW_SHEET_NAME = "Pool #" + lines[0]

    request_body = {
        'requests' : [
            {
                'duplicateSheet' : {
                    'sourceSheetId' : OLD_SHEET_ID,
                    'newSheetName' : NEW_SHEET_NAME,
                    'insertSheetIndex' : 2
                }
            }
        ]
    }

    response = service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body=request_body
    ).execute()

def populateSheet():

    with open("resources/PoolNum.txt", "r") as f:
        lines = f.readlines()

    num = int(lines[0])
    num = num - 1
    NEW_SHEET_NAME = "Pool #" + num
    CLIENT_SECRET_FILE = 'credentials.json'
    API_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    SPREADSHEET_ID = "1zi9UaJCWSYMNuePZS3JNNK6-XM7vz_pNgc0Dt0ikOfw"
    worksheet_name = NEW_SHEET_NAME

    cell_range_insert = 'A2'
    values = getInfo()
    value_range_body = {
        'majorDimension': 'ROWS',
        'values' : values
    }

    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        valueInputOption='USER ENTERED',
        range=worksheet_name + cell_range_insert,
        body=value_range_body
    ).execute



