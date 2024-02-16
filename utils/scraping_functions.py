####　スクロールしてページを更新 ####
# 必要モジュール
import time

# 環境変数定義
MAX_SCROLL_ATTEMPTS = 5
SCROLL_PAUSE_TIME = 1

def scroll_page(driver):
    """
    指定されたWebDriverを使用して、ページの最下部までスクロールする。
    ページがロードされた後にさらにコンテンツが動的にロードされる場合に対応するため、
    ページの高さが変化しなくなる(新しいコンテンツがなくなる)まで、または最大試行回数に達するまでスクロールを繰り返す。

    Parameters:
    ----------
    driver: スクロールを実行するブラウザのWebDriverオブジェクト。

    """
    last_height = driver.execute_script("return document.body.scrollHeight")
    attempts = 0
    while attempts < MAX_SCROLL_ATTEMPTS:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        attempts += 1


####　文字列を置換して正規化 ####
# 必要モジュール
import re
import unicodedata

def preprocess_texts(text):
    """
    与えられたテキストを正規化し、特定の文字を置換または除去する。
    具体的には、全角文字を半角に変換(NFKC正規化)、英字を大文字に変換、
    特定の記号を除去し、メンションを除去し、数字を除去する。

    Parameters:
    ----------
    text: 正規化する前のテキスト文字列。

    Returns:
    ----------
    replaced_text: 正規化後のテキスト文字列。
    """

    replaced_text = unicodedata.normalize("NFKC",text)
    replaced_text = replaced_text.upper()
    replaced_text = re.sub(r'[【】 () （） 『』　「」]', '' ,replaced_text) #【】 () 「」　『』の除去
    replaced_text = re.sub(r'[\[\]［］]', ' ', replaced_text) # 正方形の括弧[]と［］をスペースに置換
    replaced_text = re.sub(r'[@＠]\w+', '', replaced_text)  # メンションの除去
    replaced_text = re.sub(r'\d+\.*\d*', '', replaced_text) #数字(小数点を含む)を除去

    return replaced_text