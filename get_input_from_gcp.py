import os

from path_config import EM_BACKUP_PATH, EM_INPUT_PATH
from services.gcp.gcp_libs import get_creds, get_gss_values
from services.gcp.env.get_app_env import APP_ENV
from utils.file_handler import write_to_json

def main() -> None:
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
  # 各種パスの設定
  input_json_path = os.path.join(EM_INPUT_PATH, 'input_store_list.json') 

  # GoogleSpreadSheetから対象データをリスト形式で抽出
  target_store_names = ['中野トータルヘルスケアクリニック', '北山さくらクリニック', 'コージ歯科']
  input_store_list = get_input_store_list(target_store_names)
  write_to_json(input_store_list, input_json_path)


def get_input_store_list(target_store_names):
  #環境依存値読み込み
  _APP_ENV = APP_ENV[APP_NAME]
  # Google Auth2.0認証情報取得
  creds = get_creds(_APP_ENV)
  gss_values_lists = get_gss_values(creds, _APP_ENV)
  stores_data_list = get_stores_data_list(gss_values_lists, target_store_names)

  return stores_data_list

# storesのテンプレート
def create_store_data_template():
    return {
        "accessMessages": [],
        "address": "",
        "description1": "",
        "description2": "",
        "facilitiesMessages": [],
        "header1": "",
        "header2": "",
        "holidayMessages": [],
        "images": [
            # {
            #     "description": "",
            #     "path": ""
            # }
        ],
        "menus": [
            # {
            #     "category": [],
            #     "genre": [],
            #     "imageUrl": "",
            #     "imageUrlLarge": "",
            #     "name": "",
            #     "price": 0,
            #     "procedure": "",
            #     "recommendMessages": [],
            #     "tag": [],
            #     "topImageUrl": "",
            # }
        ],
        "message": "",
        "name": "",
        "openingHoursMessages": [],
        "remarksMessages": [],
        "staffInfoMessages": [],
        "staffs": [
            # {
            #     "imageUrl": "",
            #     "message": "",
            #     "name": "",
            #     "position": ""
            # }
        ],
        "station": "",
        "tel": "",
        "type": "",
        "url": ""
    }

# GoogleSpreadSheet 各カラムのindexを取得
def get_index_by_name(target_list, element_name):
    # 要素名でリストを検索し、インデックスを取得
    try:
        return target_list.index(element_name)
    except ValueError:
        # 要素がリストに存在しない場合
        return None
    
# input対象の店舗のデータのみ抽出
def filter_store_info(store_info_lists, target_store_names):
    # 店舗名がtarget_store_namesのいずれかに一致するデータのリストを抽出
    filtered_store_list = [store_info for store_info in store_info_lists if store_info[1] in target_store_names]
    return filtered_store_list


# 各店舗のデータをstores_dataに挿入する関数
def get_stores_data_list(gss_values_lists, target_store_names):
    stores_data_list = []
    column_list = gss_values_lists[0]

    target_store_info = filter_store_info(gss_values_lists, target_store_names)
    # カラム名とそのインデックスを格納する辞書を作成
    column_indexes = {name: get_index_by_name(column_list, name) for name in column_list}

    for store_info in target_store_info:
        store_data = create_store_data_template()

        store_data["accessMessages"] = _get_new_access_messages_list(store_info, column_indexes)
        store_data["address"] =  store_info[column_indexes["住所"]] 
        store_data["description1"] = store_info[column_indexes["大見出しの説明"]] 
        store_data["description2"] = store_info[column_indexes["イチオシ大見出しの内容"]] 
        store_data["facilitiesMessages"] = _get_new_facilities_messages_list(store_info, column_indexes)
        store_data["header1"] = store_info[column_indexes["大見出し"]]
        store_data["header2"] = store_info[column_indexes["イチオシ大見出し(赤)"]]
        # store_data["holidayMessages"] = []
        store_data["images"] = _get_new_images_list(store_info, column_indexes)
        store_data["menus"] = _get_new_menu_info_list(store_info, column_indexes)
        store_data["message"] = store_info[column_indexes["店舗からのメッセージ"]]
        store_data["name"] = store_info[column_indexes["店舗名"]]
        store_data["openingHoursMessages"] = _get_new_opening_hours_messages_list(store_info, column_indexes)
        store_data["remarksMessages"] = _get_new_remarks_messages_list(store_info, column_indexes)
        store_data["staffInfoMessages"] = _get_new_staff_info_messages_list(store_info, column_indexes)
        store_data["staffs"] = _get_new_staffs_list(store_info, column_indexes)
        store_data["station"] = store_info[column_indexes["最寄駅"]]
        store_data["tel"] = store_info[column_indexes["電話番号"]]
        store_data["type"] = store_info[column_indexes["タイプ"]]
        store_data["url"] = store_info[column_indexes["店舗URL"]]

        stores_data_list.append(store_data)
    
    return stores_data_list


def _extract_path_from_url(url):
    """
    URLから特定のプレフィックスを取り除いた文字列を抽出する

    Parameters
    ----------
    url : str
        元のURL文字列

    Returns
    -------
    extracted_path : str
        プレフィックスを取り除いた後の文字列
    """
    prefix = 'gs://empowerme-bb3c5.appspot.com/'
    extracted_path = url.replace(prefix, '')
    return extracted_path


def _convert_price_to_int(price_str):
    """
    価格の文字列（例: '¥3,300'）を整数（例: 3300）に変換する

    Parameters
    ----------
    price_str : str
        価格の文字列

    Returns
    -------
    int
        変換後の整数価格
    """
    # 通貨記号とカンマを取り除く
    cleaned_price_str = price_str.replace('¥', '').replace(',', '')
    # 整数に変換
    try:
        price = int(cleaned_price_str)
    except ValueError:
        price = 0  # 変換できない場合はデフォルト値として0を返す
    return price


def _get_new_access_messages_list(store_info, column_indexes):
    new_access_messages_list = []
    access_messages_key = "アクセス"
    access_messages = store_info[column_indexes[access_messages_key]]
    new_access_messages_list.append(access_messages)

    return new_access_messages_list


def _get_new_facilities_messages_list(store_info, column_indexes):
    new_facilities_messages_list = []
    facilities_messages_key = "設備"
    facilities_messages = store_info[column_indexes[facilities_messages_key]]
    new_facilities_messages_list.append(facilities_messages)

    return new_facilities_messages_list


def _get_new_images_list(store_info, column_indexes):
    new_images_list = [] 
    # images
    i = 0
    while True:
        i += 1
        image_description_key = f"イチオシ店舗Sub{i}説明(90文字前後)"
        image_path_key = f"イチオシ店舗Sub{i}"

        # カラムインデックスが存在しない、または説明が空の場合はループを抜ける
        if image_description_key not in column_indexes or store_info[column_indexes[image_description_key]] == '':
            break
        
        image_description = store_info[column_indexes[image_description_key]]
        image_path = _extract_path_from_url(store_info[column_indexes[image_path_key]])

        # 新しい画像情報の辞書を作成
        new_image_info = {
            "description": image_description,
            "path": image_path
        }
        
        new_images_list.append(new_image_info)

    return new_images_list


def _get_new_menu_info_list(store_info, column_indexes):
    new_menu_info_list = []

    new_menu_info = {
        "category": _get_new_category_list(store_info, column_indexes),
        "genre": _get_new_genre_list(store_info, column_indexes),
        "imageUrl": _extract_path_from_url(store_info[column_indexes["正方形メニュー(トップ一覧)"]]),
        "imageUrlLarge": _extract_path_from_url(store_info[column_indexes["長方形メニュー(施術メニューのイラストを兼用)"]]),
        "name": store_info[column_indexes["掲載メニュー名"]],
        "price": _convert_price_to_int(store_info[column_indexes["金額"]]),
        "procedure": store_info[column_indexes["施術の流れ"]],
        "recommendMessages": _get_new_recommend_messages_list(store_info, column_indexes),
        "tag": _get_new_tags_list(store_info, column_indexes),
        "topImageUrl": _extract_path_from_url(store_info[column_indexes["正方形メニュー"]]),
    }
    
    new_menu_info_list.append(new_menu_info)

    return new_menu_info_list


def _get_new_category_list(store_info, column_indexes):
    new_category = store_info[column_indexes["カテゴリー"]]

    # 改行で文字列を分割し、リストに追加
    new_category_list = new_category.split('\n')

    return new_category_list


def _get_new_genre_list(store_info, column_indexes):
    new_genre = store_info[column_indexes["ジャンル"]]

    # 改行で文字列を分割し、リストに追加
    new_genre_list = new_genre.split('\n')

    return new_genre_list


def _get_new_recommend_messages_list(store_info, column_indexes):
    new_recommend_messages = store_info[column_indexes["こんな方におすすめ"]]

    # 改行で文字列を分割し、リストに追加
    new_recommend_messages_list = new_recommend_messages.split('\n')

    return new_recommend_messages_list


def _get_new_tags_list(store_info, column_indexes):
    new_tags = store_info[column_indexes["タグ"]]

    # 改行で文字列を分割し、リストに追加
    new_tags_list = new_tags.split('\n')

    return new_tags_list


def _get_new_opening_hours_messages_list(store_info, column_indexes):
    new_opening_hours_messages = store_info[column_indexes["営業時間"]]

    # 改行で文字列を分割し、リストに追加
    new_opening_hours_messages_list = new_opening_hours_messages.split('\n')

    return new_opening_hours_messages_list


def _get_new_remarks_messages_list(store_info, column_indexes):
    new_remarks_messages_list = []
    remarks_messages_key = "備考"
    remarks_messages = store_info[column_indexes[remarks_messages_key]]
    new_remarks_messages_list.append(remarks_messages)

    return new_remarks_messages_list


def _get_new_staff_info_messages_list(store_info, column_indexes):
    new_staff_info_messages_list = []
    staff_info_messages_key = "スタッフ数"
    staff_info_messages = store_info[column_indexes[staff_info_messages_key]]
    new_staff_info_messages_list.append(staff_info_messages)

    return new_staff_info_messages_list

def _get_new_staffs_list(store_info, column_indexes):
    new_staffs_list = [] 
    # staffs
    i = 0
    while True:
        i += 1
        staff_image_url_key = f"スタッフ{i}URL"
        staff_message_key = f"スタッフ{i}メッセージ"
        staff_name_key = f"スタッフ{i}名前"
        staff_position_key = f"スタッフ{i}役職"

        # カラムインデックスが存在しない、または説明が空の場合はループを抜ける
        if staff_image_url_key not in column_indexes or store_info[column_indexes[staff_image_url_key]] == '':
            break
        
        staff_image_url = _extract_path_from_url(store_info[column_indexes[staff_image_url_key]])
        staff_message = store_info[column_indexes[staff_message_key]]
        staff_name = store_info[column_indexes[staff_name_key]]
        staff_position = store_info[column_indexes[staff_position_key]]

        # 新しいstaff情報の辞書を作成
        new_staff_info = {
            "imageUrl": staff_image_url,
            "message": staff_message,
            "name": staff_name,
            "position": staff_position 
        }
        
        new_staffs_list.append(new_staff_info)

        return new_staffs_list


if __name__ == "__main__":
  # # コマンドライン引数を取得
  # target = sys.argv[1]
  APP_NAME = "empowerme"
  main()