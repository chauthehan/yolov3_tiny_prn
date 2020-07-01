# yolov3_tiny_prn

Source build lại yolov3-tiny-prn bằng tensorflow 2.0 để detect lửa cháy sớm, về kiến trúc prn (partial residual network), tham khảo paper https://github.com/WongKinYiu/PartialResidualNetworks/blob/master/pdf/iccvw-prn.pdf

CÁC BƯỚC TRAINING:

1. Tạo data với định dạng yolo sử dụng các tool như LabelImg, lưu list data như trong file train.txt:
Định dạng mỗi dòng: <đường dẫn tới ảnh> <box1> <box2> .. <boxN>
Định dạng của box: x_min,y_min,x_max,y_max,class_id (không có dấu cách)

2. Sử dụng yolo3-tiny.conv.11.weights là file pretrained. file convert.py để chuyển từ file pre-trained từ dạng .weights sang .h5
Command: python convert.py -w yolov3-tiny-conv.11.cfg model_data/yolov3-tiny.conv.11.weights model_data/conv.11.h5

3. Chỉnh sửa file train.py và bắt đầu train
Command: python train.py
Sử dụng file trọng số đã được train trước hoặc file checkpoint với option --model model_file.

TEST:
- Chỉnh sửa file yolo_video.py để test.
Sử dụng --help để xem cách sử dụng của yolo_video.py.

NOTE:
1. Độ chính xác sẽ không khác biệt nhiều so với khi train với darknet
2. Tốc độ train sẽ chậm hơn so với Darknet.

Line demo: https://www.youtube.com/watch?v=4nqMgHINvGQ&feature=youtu.be&fbclid=IwAR0ZdDzLPP7L5qSPV7iSgwMFBVwcU4oB-zzRhrWl_mNCKv_k40DzyXzASyc



