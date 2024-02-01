import sys
from gcp_libs import get_creds, get_gss_values

def main(target) -> None:
  """
    メイン処理
    
    Parameters
    ----------
    target : String
        関数実行対象のアプリ名等

    Returns
    -------
    creds : Credentials
        Google OAuth2.0認証情報
  """

  # Google Auth2.0認証情報取得
  creds = get_creds(target)
  gss_values = get_gss_values(creds)
  

if __name__ == "__main__":
  # コマンドライン引数を取得
  target = sys.argv[1]
  main(target)