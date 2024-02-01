# 参考URL：https://developers.google.com/sheets/api/quickstart/python?hl=ja

import os.path

#Google API認証関連
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# 許容するスコープを指定
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# スプレッドシートID, シートIDをそれぞれ指定 (URLに記載あり)
SPREADSHEET_ID = "1xeV-3eIPEJS8FMEvGNWzrQ1VywMwMjAofgb20hRYzjA"
SHEET_ID = "Class Data!A2:E"

def get_cred():
  creds = None
  # token.jsonファイルは、ユーザーのアクセストークンとリフレッシュトークンを保存し、
  # 認証フローが初めて完了した時に自動的に作成。
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # 有効な認証情報がない場合は、ユーザーにログインを実行させる。
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    
    # 次回実行時にtoken.jsonを用いるため、保存先を指定
    with open("token.json", "w") as token:
      token.write(creds.to_json())

def main():
  creds = None
  # token.jsonファイルは、ユーザーのアクセストークンとリフレッシュトークンを保存し、
  # 認証フローが初めて完了した時に自動的に作成。
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # 有効な認証情報がない場合は、ユーザーにログインを実行させる。
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    
    # 次回実行時にtoken.jsonを用いるため、保存先を指定
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return

    print("Name, Major:")
    for row in values:
      # Print columns A and E, which correspond to indices 0 and 4.
      print(f"{row[0]}, {row[4]}")
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()


# サービスアカウントキーを使って認証
SERVICE_ACCOUNT_FILE = '/workspace/extended-study-382401-8676076ee48a.json'
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# gspreadのクライアントとGoogle Drive APIクライアントを設定
gc = gspread.authorize(credentials)
# Google Sheets API clientを作成
service = discovery.build('sheets', 'v4', credentials=credentials)
# Google Drive API clientを作成
drive_service = discovery.build('drive', 'v3', credentials=credentials)
# Google DriveフォルダIDを指定
folder_id = GOOGLE_DRIVE_FOLDER
page_token = None
items = []