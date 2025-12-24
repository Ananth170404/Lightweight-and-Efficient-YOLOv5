# Predict.py
# Ensure all YOLO Config are downloaded before running this

!python [Path-to-val.py] --weights [Path-to-.onnx-weights] \
               --data [Path-to-data.yaml] \
               --img 1024 \
               --task val \
               --batch-size 1
