#!/usr/bin/env python
# coding: utf-8
#
# [FILE] yolo_detect.py
#
# [DESCRIPTION]
#   ImageAIを用いた物体検出に関わるメソッドを定義する
#
from imageai.Detection import ObjectDetection

#
# [FUNCTION] yolo_detect_objects()
#
# [DESCRIPTION]
#  YOLOモデルを用いて物体を検出する
#
# [INPUTS]
#  input_image_file - 入力画像ファイル名
#  output_image_file - 出力画像ファイル名
#  model_file - YOLOモデルファイル名
#
# [OUTPUTS]
#  true  - 物体が1つ以上検出された
#  false - 物体が何も検出されなかった
#
# [NOTES]
#
def yolo_detect_objects(input_image_file, output_image_file, model_file):
    found = False

    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(model_file)
    detector.loadModel()

    detections = detector.detectObjectsFromImage(input_image=input_image_file, output_image_path=output_image_file)

    # 検出した対象物、認識精度、位置をコンソールに表示する
    for eachObject in detections:
        print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
        found = True
    
    return found
#
# END OF FILE
#