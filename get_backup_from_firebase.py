import os
from datetime import datetime

from path_config import EM_BACKUP_PATH
from services.firebase.firebase_libs import get_client, get_from_fire_store_collection
from services.firebase.env.get_app_env import APP_ENV
from utils.file_handler import read_from_json, write_to_json

def main() -> None:
    """
    メイン処理

    Parameters
    ----------

    Returns
    -------
    None
    """
    # 現在の時刻をフォーマットされた文字列として取得
    # 例: 2023-01-01_12-00-00
    current_time_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # ファイル名に現在の時刻を付け加える
    backup_file_name = f"backup_{current_time_str}.json"

    #各種パスの指定
    backup_file_path = os.path.join(EM_BACKUP_PATH, backup_file_name)

    # firebase内のデータを取得
    db = get_client(APP_ENV)
    docs = get_from_fire_store_collection(db, 'stores')

    # backup用にリスト化
    backup_data_list = [doc.to_dict() for doc in docs]
    write_to_json(backup_data_list, backup_file_path)

if __name__ == '__main__':\
    main()