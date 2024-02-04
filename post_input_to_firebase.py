import os
from datetime import datetime

from path_config import EM_INPUT_PATH, EM_BACKUP_PATH, EM_LOGS_PATH
from services.firebase.firebase_libs import get_client, get_from_fire_store_collection, post_to_fire_store_collection
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
    logs_file_name = f"backup_{current_time_str}.json"

    #各種パスの指定
    input_file_path = os.path.join(EM_INPUT_PATH, 'input_store_list.json')
    logs_file_path = os.path.join(EM_LOGS_PATH, 'post_input_to_firebase', logs_file_name)

    db = get_client(APP_ENV)

    input_store_list = read_from_json(input_file_path)
    posted_docs_info = post_to_fire_store_collection(db, 'stores', input_store_list)

    # posted_docs_info リストをJSONファイルに保存
    if os.environ['ENV'] == 'dev':
        write_to_json(posted_docs_info, logs_file_path)

if __name__ == '__main__':\
    main()