# ref : https://pub.towardsai.net/how-to-create-a-new-custom-dataset-from-images-9b95977964ab

from PIL import Image
import numpy as np
import sys
import os
import csv
# default format can be changed as needed
def createFileList(myDir, format='.jpg'):
    fileList = []
    print(myDir)
    labels = []
    names = []
    keywords = {
    "A_0_": "0", "A_1_": "1", "A_2_": "2", "A_3_": "3", "A_4_": "4",
    "A_5_": "5", "A_6_": "6", "A_7_": "7", "A_8_": "8", "A_9_": "9",
    "A_10_": "10", "A_11_": "11", "A_12_": "12", "A_13_": "13", "A_14_": "14",
    "A_15_": "15", "A_16_": "16", "A_17_": "17", "A_18_": "18", "A_19_": "19",
    "A_20_": "20"
}
    for root, dirs, files in os.walk(myDir, topdown=True):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
            for keyword in keywords:
                if keyword in name:
                    labels.append(keywords[keyword])
                else:
                    continue
            names.append(name)
    return fileList, labels, names
# load the original image
myFileList, labels, names  = createFileList('./imgs/20 - copia')
i = 0
for file in myFileList:
    print(file)
    img_file = Image.open(file)
    # img_file.show()
# get original image parameters...
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode
# Make image Greyscale
    img_grey = img_file.convert('L')
    #img_grey.save('result.png')
    #img_grey.show()
# Save Greyscale values
    value = np.asarray(img_grey.getdata(), dtype=np.int64).reshape((width, height))
    value = value.flatten()
    
    value = np.append(value,labels[i])
    i +=1
    
    print(value)
    with open("data20.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(value)
        
