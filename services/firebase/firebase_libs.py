#参考UR+ https://firebase.google.com/docs/firestore/quickstart?hl=ja#python
import os.path
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from path_config import FIRE_BASE_CONF_PATH


def get_client(app_env):
    # 各種パスの設定
    service_account_key_path = os.path.join(FIRE_BASE_CONF_PATH, app_env['SERVICE_ACCOUNT_KEY']) 
        
    # Firebase Admin SDKを初期化
    cred = credentials.Certificate(service_account_key_path)
    firebase_admin.initialize_app(cred)

    # Firestoreのインスタンスを取得します。
    client = firestore.client()

    return client


def get_from_fire_store_collection(db, collection_name):
    stores_ref = db.collection(collection_name)
    docs = stores_ref.stream()

    return docs


def print_fire_store_docs(docs):
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")


def post_to_fire_store_collection(db, collection_name, target_list):
    # 投稿されたドキュメントのIDを格納するリスト
    posted_docs_info = []

    # データをFirestoreへ挿入。
    for target_data in target_list:
        _, doc_ref = db.collection(collection_name).add(target_data)

        # ドキュメントのIDと内容を辞書形式で格納
        doc_info = {
            "id": doc_ref.id,
            "data": target_data
        }
        posted_docs_info.append(doc_info)
    
    return posted_docs_info

