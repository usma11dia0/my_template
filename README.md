# プロジェクト名
自分用テンプレートリポジトリ

## シールド一覧
<!-- 使用技術一覧 -->
<!-- 該当するプロジェクトの中から任意のものを選ぶ-->
<p style="display: inline">
  <!-- フロントエンドのフレームワーク一覧 -->
  <img src="https://img.shields.io/badge/-Node.js-000000.svg?logo=node.js&style=for-the-badge">
  <img src="https://img.shields.io/badge/-Next.js-000000.svg?logo=next.js&style=for-the-badge">
  <img src="https://img.shields.io/badge/-TailwindCSS-000000.svg?logo=tailwindcss&style=for-the-badge">
  <img src="https://img.shields.io/badge/-React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB">
  <!-- バックエンドのフレームワーク一覧 -->
  <img src="https://img.shields.io/badge/-Django-092E20.svg?logo=django&style=for-the-badge">
  <!-- バックエンドの言語一覧 -->
  <img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">
  <!-- ミドルウェア一覧 -->
  <img src="https://img.shields.io/badge/-Nginx-269539.svg?logo=nginx&style=for-the-badge">
  <img src="https://img.shields.io/badge/-MySQL-4479A1.svg?logo=mysql&style=for-the-badge&logoColor=white">
  <img src="https://img.shields.io/badge/-Gunicorn-199848.svg?logo=gunicorn&style=for-the-badge&logoColor=white">
  <!-- インフラ一覧 -->
  <img src="https://img.shields.io/badge/-Docker-1488C6.svg?logo=docker&style=for-the-badge">
  <img src="https://img.shields.io/badge/-githubactions-FFFFFF.svg?logo=github-actions&style=for-the-badge">
  <img src="https://img.shields.io/badge/-Amazon%20aws-232F3E.svg?logo=amazon-aws&style=for-the-badge">
  <img src="https://img.shields.io/badge/-terraform-20232A?style=for-the-badge&logo=terraform&logoColor=844EBA">
</p>

## 目次
1. サンプル1
2. サンプル2
3. サンプル3
4. サンプル4
5. サンプル5

## プロジェクトについて
<!-- プロジェクトの概要を記載 -->
サンプル

## 環境
<!-- 言語、フレームワーク、ミドルウェア、インフラの一覧とバージョンを記載 -->

| 言語・フレームワーク    | バージョン |
| --------------------- | ---------- |
| Python                | 3.11.4     |
| Django                | 4.2.1      |
| Django Rest Framework | 3.14.0     |
| MySQL                 | 8.0        |
| Node.js               | 16.17.0    |
| React                 | 18.2.0     |
| Next.js               | 13.4.6     |
| Terraform             | 1.3.6      |

その他のパッケージのバージョンは pyproject.toml と package.json を参照してください

## ディレクトリ構成
<!-- Treeコマンドを使ってディレクトリ構成を記載 -->
<!-- ❯ tree -a -I "node_modules|.next|.git|.pytest_cache|static" -L 2 -->

```text
backend
├── .gitignore
├── api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── japanese_quiz_api
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── media
│   ├── audios
│   └── images
├── model
│   ├── japanese_classification.pt
│   └── predict.py
├── requirements-dev.txt
└── requirements.txt
```

## 開発環境構築
### 1. 手順1
### 2. 手順2

http://127.0.0.1:8000 にアクセスできるか確認
アクセスできたら成功

### 環境変数の一覧

| 変数名                 | 役割                                      | デフォルト値                       | DEV 環境での値                           |
| ---------------------- | ----------------------------------------- | ---------------------------------- | ---------------------------------------- |
| MYSQL_ROOT_PASSWORD    | MySQL のルートパスワード（Docker で使用） | root                               |                                          |
| MYSQL_DATABASE         | MySQL のデータベース名（Docker で使用）   | django-db                          |                                          |
| MYSQL_USER             | MySQL のユーザ名（Docker で使用）         | django                             |                                          |
| MYSQL_PASSWORD         | MySQL のパスワード（Docker で使用）       | django                             |                                          |
| MYSQL_HOST             | MySQL のホスト名（Docker で使用）         | db                                 |                                          |
| MYSQL_PORT             | MySQL のポート番号（Docker で使用）       | 3306                               |                                          |
| SECRET_KEY             | Django のシークレットキー                 | secretkey                          | 他者に推測されないランダムな値にすること |
| ALLOWED_HOSTS          | リクエストを許可するホスト名              | localhost 127.0.0.1 [::1] back web | フロントのホスト名                       |
| DEBUG                  | デバッグモードの切り替え                  | True                               | False                                    |
| TRUSTED_ORIGINS        | CORS で許可するオリジン                   | http://localhost                   |                                          |
| DJANGO_SETTINGS_MODULE | Django アプリケーションの設定モジュール   | project.settings.local             | project.settings.dev                     |

### コマンド一覧

| Make                | 実行する処理                   | 元のコマンド                                                  |
| ------------------- | ----------------------------- | ------------------------------------------------------------ |
| make pdoc           | pdoc ドキュメントの作成         | docker-compose exec app env CI_MAKING_DOCS=1 poetry run pdoc -o docs application |
| make init           | Terraform の初期化             | docker-compose -f infra/docker-compose.yml run --rm terraform init               |
| make fmt            | Terraform の設定ファイルをフォーマット | docker-compose -f infra/docker-compose.yml run --rm terraform fmt          |
| make validate       | Terraform の構成ファイルが正常であることを確認 | docker-compose -f infra/docker-compose.yml run --rm terraform validate |
| make show           | 現在のリソースの状態を参照                    | docker-compose -f infra/docker-compose.yml run --rm terraform show     |
| make apply          | Terraform の内容を適用                       | docker-compose -f infra/docker-compose.yml run --rm terraform apply    |
| make destroy        | Terraform で構成されたリソースを削除          | docker-compose -f infra/docker-compose.yml run --rm terraform destroy  |