import os 
import json

# logging
from logging import (
    getLogger,
    config
)

# パスの設定
LOGGING_CONF_DIR = './conf/'
logging_config_path = os.path.join(LOGGING_CONF_DIR,'logging_config.json')

# カスタムロガーの設定
with open(logging_config_path, 'r') as f:
    logger_config = json.load(f)
config.dictConfig(logger_config)
logger = getLogger('main')

# 環境変数読み込み
env_first = os.environ.get('ENV_FIRST')
env_last = os.environ.get('ENV_LAST')

#結果出力
logger.info('こんにちは')
logger.info(f"ENV_FIRST: {env_first}")
logger.debug(f"ENV_LAST: {env_last}")