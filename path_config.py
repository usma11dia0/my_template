import os

# プロジェクトのルートディレクトリのパスを取得
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# FireBase
FIRE_BASE_CONF_PATH = os.path.join(ROOT_DIR, 'services', 'firebase', 'conf')
FIRE_BASE_ENV_PATH = os.path.join(ROOT_DIR, 'services', 'firebase', 'env')

# GCP
GCP_CONF_PATH = os.path.join(ROOT_DIR, 'services', 'gcp', 'conf')
GCP_ENV_PATH = os.path.join(ROOT_DIR, 'services', 'gcp', 'env')

# Empowerme
EM_BACKUP_PATH = os.path.join(ROOT_DIR, 'backup')
EM_INPUT_PATH = os.path.join(ROOT_DIR, 'input')
EM_LOGS_PATH = os.path.join(ROOT_DIR, 'logs')