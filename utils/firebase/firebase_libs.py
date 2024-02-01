import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Firebase Admin SDKを初期化
cred = credentials.Certificate('path/to/your/serviceAccountKey.json')
firebase_admin.initialize_app(cred)


def get_client():

    # Firestoreのインスタンスを取得します。
    client = firestore.client()

    return client