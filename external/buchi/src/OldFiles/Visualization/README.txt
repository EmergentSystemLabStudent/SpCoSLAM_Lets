[rviz��Ɉʒu���z��`�悷����@]
$ roscore
$ rviz -d ./saveSpCoMAP_online.rviz 
$ python ./autovisualization.py test5

�ʎw��̏ꍇ
$ rosrun map_server map_server ./test5/map/map361.yaml
$ python ./new_place_draw.py test5 50 23 