csv_send.py のみ必須


【ファイル】
CNN_place.py：CNNの特徴量をそのまま保存する.(PlaceCNN版)
README.txt：このファイル
SpCoSLAM.sh：オンライン学習実行用基本ファイル
SpCoSLAM_visualization.sh：自動で学習結果を逐次描画するためのシェルスクリプト（実際はこちらはあまり使ってない）・（下記参照[rviz上に位置分布を描画する方法]）
__init__.py：ハイパーパラメータなどの初期値やファイルパス指定用のファイル
autovisualization.py：自動で学習結果を逐次描画するためのプログラム(保存は別でしなければならない)

gmapping.sh：FastSLAM実行用のシェルスクリプト
learnSpCoSLAM3.2.py：SpCoSLAM online learning program (無駄なコメントアウトコードを省いたバージョン+bugfix)、かつ、SpCoAのオンライン版（SpCoSLAMから言語モデル更新と画像特徴を除けるバージョン）
map_saver.py：地図を逐次的に保存していくプログラム（rospy使用）

new_place_draw.py：学習した場所領域のサンプルをrviz上に可視化するプログラム
new_place_draw_online.py：オンライン可視化用
new_position_draw_online.py：ロボットの自己位置描画用

run_FastSLAM.py：FastSLAMを実行するための子プログラム
run_SpCoSLAM.py：SpCoSLAMを実行するための子プログラム
run_gmapping.sh：gmappingを実行するための子プログラム
run_mapviewer.py：map_serverコマンドを実行する小プログラム（未使用？）
run_mapviewer.sh：run_mapviewer.pyを実行するためのシェルスクリプト（未使用？）
run_rosbag.py：rosbagを実行するための子プログラム
run_roscore.sh：roscoreを実行するための子プログラム
saveSpCoMAP.rviz：rvizファイル
saveSpCoMAP_online.rviz：rvizファイル（オンライン描画用）



【実行準備】
・学習データセットのパス指定、トピック名を合わせるなど（__init__.py、run_gmapping.sh）
・パーティクル数の指定は、__init__.pyとrun_gmapping.shの両方変更する必要がある。


-----
[rviz上に位置分布を描画する方法]
roscore
rviz -d ./Dropbox/SpCoSLAM/learning/saveSpCoMAP_online.rviz 
python ./autovisualization.py p30a20g10sfix008

個別指定の場合
rosrun map_server map_server ./p30a20g10sfix008/map/map361.yaml
python ./new_place_draw.py p30a20g10sfix008 50 23 

-------------------------------------------------
更新日時
2017/02/12 Akira Taniguchi
2017/03/12 Akira Taniguchi
