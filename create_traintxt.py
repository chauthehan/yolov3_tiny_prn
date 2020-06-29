import cv2
import os

paths = os.listdir('data/labels')

# if not os.path.exists('train.txt'):
#     os.mk
with open('train.txt', 'w') as infile:
    for path in paths:
        with open(os.path.join('data/labels', path), 'r') as label_file:
            path = os.path.splitext(path)[0]
            line_to_write = 'data/images/'+path+'.jpg'
            if not os.path.exists(line_to_write):
                line_to_write = 'data/images/'+path+'.png'
            image = cv2.imread(line_to_write)
            print(line_to_write)
            print(image.shape)
            (h, w, _) = image.shape
            lines = label_file.readlines()
            for line in lines:
                line = line.strip()
                parts = line.split(' ')
                x1 = int((float(parts[1]) - float(parts[3])/2)*w)
                y1 = int((float(parts[2]) - float(parts[4])/2)*h)
                x2 = int((float(parts[1]) + float(parts[3])/2)*w)
                y2 = int((float(parts[2]) + float(parts[4])/2)*h)                
                line_to_write = line_to_write+' '+str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+'0'
   
            infile.write(line_to_write)
            infile.write('\n')








