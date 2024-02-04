import json

def write_to_json(data, filename):
    """
    データをJSON形式でファイルに書き出す

    Parameters
    ----------
    data : list or dict
        書き出すデータ
    filename : str
        保存するファイルの名前
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def read_from_json(filename):
    """
    JSON形式のファイルからデータを読み込む

    Parameters
    ----------
    filename : str
        読み込むファイルの名前

    Returns
    -------
    data : dict or list
        ファイルから読み込んだデータ
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data