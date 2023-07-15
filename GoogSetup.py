from urllib import request
import requests

with open("resources/PoolNum.txt", "w+") as f:
    lines = f.readlines()
    f.write(lines[0] + 1)
def CreateGoogleSheet():

    response = requests.get("https://sheets.googleapis.com/v4/spreadsheets/1zi9UaJCWSYMNuePZS3JNNK6-XM7vz_pNgc0Dt0ikOfw")
    sheet = response.text

    SPREADSHEET_ID = "1zi9UaJCWSYMNuePZS3JNNK6-XM7vz_pNgc0Dt0ikOfw"
    OLD_SHEET_ID = 1159631575
    NEW_SHEET_NAME = "Pool #" + lines[0]

    # Insert New Empty Row at A2
    body = {
        'requests': [
            {
                'duplicateSheet': {
                    'sourceSheetId': OLD_SHEET_ID,
                    'insertSheetIndex': 2,
                    'newSheetName': NEW_SHEET_NAME
                }
            }
        ]
    }
    # Using sheet.values().batchUpdate will trigger: Invalid JSON payload received. Unknown name "requests": Cannot find field.
    result = sheet.batchUpdate(spreadsheetId=SPREADSHEET_ID,
                               body=body).execute()
