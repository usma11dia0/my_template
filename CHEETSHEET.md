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
| conda install -c condaforge [パッケージ名]  | 取得先チャネルを追加して、パッケージをインストール         |
| conda config --remove channels [チャネル名] | 取得先チャネルを削除                                    |

## Docker
| Command                     | 実行する処理                                                          |
| --------------------------  | -------------------------------------------------------------------- | 
