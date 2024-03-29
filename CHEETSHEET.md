### コマンド一覧

## Git
| Command                     | 実行する処理                                                          |
| --------------------------  | -------------------------------------------------------------------- | 
| git reset --soft HEAD^      | 直前のコミットを取り消す                                               |
| git reflog                  | 変更履歴を確認                                                        |
| git reset --hard HEAD@{num} | 対象コミットまで変更取消 ※powershell上では'HEAD@{num}'のように''で囲む  |
| git stash list              | 退避させた変更差分のリスト一覧を表示                                    |
| git stash -u save [変更名]　 | untracked fileも含めて変更差分を退避。変更名で保存                      |
| git stash apply num         | num番目の変更をソースへ戻す                                            |
| git stash drop num          | num番目の変更を削除                                                   |
| git stash clear             | 退避リストを全削除                                                    |
| git rm --cached [ファイル名] | ファイルをgitの追跡対象から外す                                        |
| git remote prune origin     | リモート追跡ブランチを削除                                             |

## Miniconda
| Command                     | 実行する処理                                                          |
| --------------------------  | -------------------------------------------------------------------- | 
| conda create -n [env名] python==3.x.x      | pythonのバージョンを指定して仮想環境構築                  |
| conda config --show channels               | 取得先のパッケージコレクション一覧表示                    |
| conda install -c conda-forge [パッケージ名]  | 取得先チャネルを指定して、パッケージをインストール        |
| conda config --remove channels [チャネル名] | 取得先チャネルを削除                                    |

## Node Version Manager
| Command                     | 実行する処理                                                          |
| --------------------------  | -------------------------------------------------------------------- | 
| nvm use v●.●.●              | 利用するnodeを変更(バージョンを指定)                                    |
| nvm ls-remote               | 利用可能なnodeのバージョンを確認 ※Linux,macOS                          |
| nvm list available          | 利用可能なnodeのバージョンを確認 ※Windows    　                        |
| nvm list                    | installしたnodeのバージョンを確認            　                        |
| $echo "●.●.●" > .nvmrc      | PJで利用するNodeを指定する.nvmrcファイル作成。※Linux,macOS ※作成後nvm useを実行する |

## Windows
| Command                     | 実行する処理                                                          |
| --------------------------  | -------------------------------------------------------------------- | 
| Get-Acl . \| Format-List    | カレントディレクトリの権限を確認                                        |
| whoami                      | 現在のユーザ名を確認                                                   |
| whoami                      | 現在のユーザ名を確認                                                   |

## Linux
| Command                     | 実行する処理                                                          |
| --------------------------  | -------------------------------------------------------------------- | 
| ss -tap                     | ポートの状態を確認 (-t:tcp, -a:all, -p:port)                           |
| curl ifconfig.me            | ローカルPCのグローバルIPアドレス確認                                    |
| df -h                       | ディスク容量の確認                                                     |
| du -sh [ファイル名]          | ファイルサイズの確認                                                   |
| sh -x [ファイル名]           | .shファイルの実行中に、用いることが出来るコマンドを出力                   |
| dpkg --get-selections       | apt-getでインストールしたパッケージ一覧出力                              |
| ls -la                      | ファイル一覧 + 権限表示                                                |
| chmod -R 744 .  | 現在のディレクトリ全てのファイル権限を変更する (4:read, 2:write, 1:execute, 0:no permission) |
| export PATH="$PATH:追加パス" | パスを更新 (bash設定ファイルパス ユーザ毎：/.bashrc システム全体：/etc/bash.bashrc)|
| tree -a -I "node_modules|.next|.git|.pytest_cache|static" -L 2    | カレントディレクトリのディレクトリ構成を出力 |

## Docker
| Command                     | 実行する処理                                                          |
| --------------------------  | -------------------------------------------------------------------- | 


