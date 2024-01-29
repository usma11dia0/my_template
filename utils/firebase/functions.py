from service import get_client


def post_fire_store(collection, target_json):

    db = get_client()

    # 挿入するデータを定義します。
    clinic_data = {
        'accessMessages': ["JR中央・総武線 飯田橋駅より徒歩1分", "JR中央・総武線 水道橋駅より徒歩10分"],
        'address': "東京都新宿区 下宮比町1-1相沢ビル3F",
        # その他のフィールドも同様に定義します。
    }

    # データをFirestoreに挿入します。
    db.collection('clinics').add(clinic_data)


def get_input_json(target_file):
    pass


if __name__ == '__main__':
    
    input_json = get_input_json()

    post_fire_store('stores', input_json)