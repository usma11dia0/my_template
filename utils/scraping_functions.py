####　スクロールしてページを更新 ####
# モジュールimport
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

