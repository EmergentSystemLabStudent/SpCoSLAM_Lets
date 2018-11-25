[rviz上に位置分布を描画する方法]
$ roscore
$ rviz -d ./saveSpCoMAP_online.rviz 
$ python ./autovisualization.py test5

個別指定の場合
$ rosrun map_server map_server ./test5/map/map361.yaml
$ python ./new_place_draw.py test5 50 23 