#参考UR+ https://firebase.google.com/docs/firestore/quickstart?hl=ja#python
import os.path
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from path_config import FIRE_BASE_CONF_PATH


def get_client(app_env):
    """
    Firebase Admin SDKを初期化し、Firestoreのクライアントインスタンスを取得する。

    Parameters:
    - app_env: アプリケーション環境設定を含む辞書。
               'SERVICE_ACCOUNT_KEY'キーでサービスアカウントキーのファイル名を指定する。

    Returns:
    - Firestoreのクライアントインスタンス。
    """

    # 各種パスの設定
    service_account_key_path = os.path.join(FIRE_BASE_CONF_PATH, app_env['SERVICE_ACCOUNT_KEY']) 
        
    # Firebase Admin SDKを初期化
    cred = credentials.Certificate(service_account_key_path)
    firebase_admin.initialize_app(cred)

    # Firestoreのインスタンスを取得。
    client = firestore.client()

    return client


def get_from_fire_store_collection(db, collection_name):
    """
    指定されたFirestoreコレクションからドキュメントを取得する。

    Parameters:
    - db: Firestoreのクライアントインスタンス。
    - collection_name: 取得するドキュメントが含まれるコレクションの名前。

    Returns:
    - コレクション内のドキュメントを表すイテレータ。
    """

    stores_ref = db.collection(collection_name)
    docs = stores_ref.stream()

    return docs


def print_fire_store_docs(docs):
    """
    Firestoreから取得したドキュメントの内容をコンソールに出力する。

    Parameters:
    - docs: ドキュメントのイテレータ。
    """

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")


def post_to_fire_store_collection(db, collection_name, target_list):
    """
    指定されたFirestoreコレクションに複数のドキュメントを追加する。

    Parameters:
    - db: Firestoreのクライアントインスタンス。
    - collection_name: ドキュメントを追加するコレクションの名前。
    - target_list: 追加するドキュメントのリスト。

    Returns:
    - 追加されたドキュメントのIDとデータを含む辞書のリスト。
    """

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


def fire_store_docs_to_dict_list(docs):
    """
    Firestoreから取得したドキュメントのイテレータを、辞書のリストに変換する。

    Parameters:
    - docs: ドキュメントのイテレータ。

    Returns:
    - ドキュメントのIDとデータを含む辞書のリスト。
    """

    docs_dict_list = []

    for doc in docs:
        # ドキュメントのIDと内容を辞書形式で格納
        doc_info = {
            "id": doc.id,
            "data": doc.to_dict()
        }
        docs_dict_list.append(doc_info)
    
    return docs_dict_list


def update_fire_store_doc(db, collection_name, document_id, target_field, updated_value):
    """
    Firestoreの指定されたコレクション内のドキュメントの特定フィールドを更新する。

    Parameters:
    - collection_name: コレクションの名前
    - document_id: 更新するドキュメントのID
    - updated_value: 特定フィールドに設定する新しい値
    """
    
    # ドキュメントの参照を取得
    doc_ref = db.collection(collection_name).document(document_id)

    # imageUrlLargeフィールドを更新
    doc_ref.update({target_field: updated_value})