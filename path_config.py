import os

# プロジェクトのルートディレクトリのパスを取得
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# FireBase
FB_ENV_PATH = os.path.join(ROOT_DIR, 'utils', 'firebase', 'env')

# GCP
GCP_CONF_PATH = os.path.join(ROOT_DIR, 'utils', 'gcp', 'conf')
GCP_ENV_PATH = os.path.join(ROOT_DIR, 'utils', 'gcp', 'env')