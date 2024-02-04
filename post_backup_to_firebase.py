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

    #各種パスの指定
    backup_file_path = os.path.join(EM_BACKUP_PATH, 'backup_2024-02-04_12-00-33_after_add_store.json')

    backup_store_list = read_from_json(backup_file_path)
   
    db = get_client(APP_ENV)
   
    post_to_fire_store_collection(db, 'stores', backup_store_list)


if __name__ == '__main__':\
    main()