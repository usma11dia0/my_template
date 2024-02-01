# 参考URL：https://developers.google.com/sheets/api/quickstart/python?hl=ja
import os.path

#Google API認証関連
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#環境依存値読み込み
from env.get_env import ENV_JSON

def get_creds() -> Credentials:
  """
    Google OAuth2.0認証情報を取得する
    
    Parameters
    ----------

    Returns
    -------
    creds : Credentials
        Google OAuth2.0認証情報
  """

  creds = None
  # token.jsonファイルは、ユーザーのアクセストークンとリフレッシュトークンを保存し、
  # 認証フローが初めて完了した時に自動的に作成。
  if os.path.exists(ENV_JSON["TOKEN_JSON_PATH"]):
    creds = Credentials.from_authorized_user_file("token.json", ENV_JSON["SCOPES"])
  # 有効な認証情報がない場合は、ユーザーにログインを実行させる。
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", ENV_JSON["SCOPES"]
      )
      creds = flow.run_local_server(port=0)
    
    # 次回実行時にtoken.jsonを用いるため、保存先を指定
    with open(ENV_JSON["TOKEN_JSON_PATH"], "w") as token:
      token.write(creds.to_json())


def get_gss_values(creds):
  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=ENV_JSON["SPREADSHEET_ID"], range=ENV_JSON["RANGE_NAME"])
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
# SERVICE_ACCOUNT_FILE = '/workspace/extended-study-382401-8676076ee48a.json'
# credentials = service_account.Credentials.from_service_account_file(
#     SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# # gspreadのクライアントとGoogle Drive APIクライアントを設定
# gc = gspread.authorize(credentials)
# # Google Sheets API clientを作成
# service = discovery.build('sheets', 'v4', credentials=credentials)
# # Google Drive API clientを作成
# drive_service = discovery.build('drive', 'v3', credentials=credentials)
# # Google DriveフォルダIDを指定
# folder_id = GOOGLE_DRIVE_FOLDER
# page_token = None
# items = []