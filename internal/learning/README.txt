csv_send.py �̂ݕK�{


�y�t�@�C���z
CNN_place.py�FCNN�̓����ʂ����̂܂ܕۑ�����.(PlaceCNN��)
README.txt�F���̃t�@�C��
SpCoSLAM.sh�F�I�����C���w�K���s�p��{�t�@�C��
SpCoSLAM_visualization.sh�F�����Ŋw�K���ʂ𒀎��`�悷�邽�߂̃V�F���X�N���v�g�i���ۂ͂�����͂��܂�g���ĂȂ��j�E�i���L�Q��[rviz��Ɉʒu���z��`�悷����@]�j
__init__.py�F�n�C�p�[�p�����[�^�Ȃǂ̏����l��t�@�C���p�X�w��p�̃t�@�C��
autovisualization.py�F�����Ŋw�K���ʂ𒀎��`�悷�邽�߂̃v���O����(�ۑ��͕ʂł��Ȃ���΂Ȃ�Ȃ�)

gmapping.sh�FFastSLAM���s�p�̃V�F���X�N���v�g
learnSpCoSLAM3.2.py�FSpCoSLAM online learning program (���ʂȃR�����g�A�E�g�R�[�h���Ȃ����o�[�W����+bugfix)�A���ASpCoA�̃I�����C���ŁiSpCoSLAM���猾�ꃂ�f���X�V�Ɖ摜������������o�[�W�����j
map_saver.py�F�n�}�𒀎��I�ɕۑ����Ă����v���O�����irospy�g�p�j

new_place_draw.py�F�w�K�����ꏊ�̈�̃T���v����rviz��ɉ�������v���O����
new_place_draw_online.py�F�I�����C�������p
new_position_draw_online.py�F���{�b�g�̎��Ȉʒu�`��p

run_FastSLAM.py�FFastSLAM�����s���邽�߂̎q�v���O����
run_SpCoSLAM.py�FSpCoSLAM�����s���邽�߂̎q�v���O����
run_gmapping.sh�Fgmapping�����s���邽�߂̎q�v���O����
run_mapviewer.py�Fmap_server�R�}���h�����s���鏬�v���O�����i���g�p�H�j
run_mapviewer.sh�Frun_mapviewer.py�����s���邽�߂̃V�F���X�N���v�g�i���g�p�H�j
run_rosbag.py�Frosbag�����s���邽�߂̎q�v���O����
run_roscore.sh�Froscore�����s���邽�߂̎q�v���O����
saveSpCoMAP.rviz�Frviz�t�@�C��
saveSpCoMAP_online.rviz�Frviz�t�@�C���i�I�����C���`��p�j



�y���s�����z
�E�w�K�f�[�^�Z�b�g�̃p�X�w��A�g�s�b�N�������킹��Ȃǁi__init__.py�Arun_gmapping.sh�j
�E�p�[�e�B�N�����̎w��́A__init__.py��run_gmapping.sh�̗����ύX����K�v������B


-----
[rviz��Ɉʒu���z��`�悷����@]
roscore
rviz -d ./Dropbox/SpCoSLAM/learning/saveSpCoMAP_online.rviz 
python ./autovisualization.py p30a20g10sfix008

�ʎw��̏ꍇ
rosrun map_server map_server ./p30a20g10sfix008/map/map361.yaml
python ./new_place_draw.py p30a20g10sfix008 50 23 

-------------------------------------------------
�X�V����
2017/02/12 Akira Taniguchi
2017/03/12 Akira Taniguchi
