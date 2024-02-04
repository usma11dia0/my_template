import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TMP_PATH = os.path.join(ROOT_DIR, 'tmp')

# FireBase
FIRE_BASE_CONF_PATH = os.path.join(ROOT_DIR, 'services', 'firebase', 'conf')
FIRE_BASE_ENV_PATH = os.path.join(ROOT_DIR, 'services', 'firebase', 'env')

# GCP
GCP_CONF_PATH = os.path.join(ROOT_DIR, 'services', 'gcp', 'conf')
GCP_ENV_PATH = os.path.join(ROOT_DIR, 'services', 'gcp', 'env')