# 参考URL：https://developers.google.com/sheets/api/quickstart/python?hl=ja
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from path_config import GCP_CONF_PATH


def get_creds(app_env) -> Credentials:
  """
    Google OAuth2.0認証情報を取得する
    
    Parameters
    ----------
    app_env : String
        アプリ固有の環境変数 

    Returns
    -------
    creds : Credentials
        Google OAuth2.0認証情報
  """
  
  # 各種パスの設定
  cred_json_path = os.path.join(GCP_CONF_PATH, app_env['CRED_JSON']) 
  token_json_path = os.path.join(GCP_CONF_PATH, app_env['TOKEN_JSON'])

  creds = None
  # token.jsonファイルは、ユーザーのアクセストークンとリフレッシュトークンを保存し、
  # 認証フローが初めて完了した時に自動的に作成。
  if os.path.exists(token_json_path):
    creds = Credentials.from_authorized_user_file(token_json_path, app_env["SCOPES"])
  # 有効な認証情報がない場合は、ユーザーにログインを実行させる。
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          cred_json_path, app_env["SCOPES"]
      )
      creds = flow.run_local_server(port=0)
    
    # 次回実行時にtoken.jsonを用いるため、保存先を指定
    with open(token_json_path, "w") as token:
      token.write(creds.to_json())

  return creds


def get_gss_values(creds, app_env):
  """
    GoogleSpreadSheetの値を取得する
    
    Parameters
    ----------
    cred : Credentials
        Google OAuth2.0認証情報
    app_env : String
        アプリ固有の環境変数 

    Returns
    -------
    values : Any
        GoogleSpreadSheet内の値
  """
  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=app_env["SPREADSHEET_ID"], range=app_env["RANGE_NAME"])
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return

    return values
  except HttpError as err:
    print(err)



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