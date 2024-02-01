from firebase_libs import get_client


def post_fire_store(collection, target_json):

    db = get_client()
    # データをFirestoreに挿入します。
    db.collection('clinics').add(clinic_data)


def get_input_json(target_file):
    
    # 挿入するデータを定義。
    stores_data = {
        "accessMessages": [""],
        "address": "",
        "description1": "",
        "description2": "",
        "facilitiesMessages": [""],
        "header1": "",
        "header2": "",
        "holidayMessages": [""],
        "images": [
            {
                "description": "",
                "path": ""
            }
        ],
        "menus": [
            {
                "category": [""],
                "genre": [""],
                "imageUrl": "",
                "imageUrlLarge": "",
                "name": "",
                "price": 40000,
                "procedure": "",
                "recommendMessages": [""],
                "tag": [""],
                "topImageUrl": "",
            }
        ],
        "message": "",
        "name": "",
        "openingHoursMessages": [""],
        "remarkMessages": [""],
        "staffInfoMessages": [""],
        "staff": [
            {
                "imageUrl": "",
                "message": "",
                "name": "",
                "position": ""
            }
        ],
        "station": "",
        "tel": "",
        "type": "",
        "url": ""
    }



if __name__ == '__main__':
    
    input_json = get_input_json()
    post_fire_store('stores', input_json)