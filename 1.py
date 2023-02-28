# 写训练、验证、测试的txt文件
import os
import cv2
from tqdm import tqdm





# f1 = open('/data1/zlf/OULU_NPU_zlf/2_dev/dev_8.txt','r')
# dir1 = '/data1/zlf/OULU_NPU_zlf/2_dev/dev_artificial_label_scene'
# f1a = open('/data1/zlf/OULU_NPU_zlf/2_dev/dev_add.txt','w')

# f2 = open('/data1/zlf/OULU_NPU_zlf/3_test/test_8.txt','r')
# dir2 = '/data1/zlf/OULU_NPU_zlf/3_test/test_artificial_label_scene'
# f2a = open('/data1/zlf/OULU_NPU_zlf/3_test/test_add.txt','w')

# add = 0
# lines = f1.readlines()
# for line in lines:
#     path_ = line.split(' ')[0]
#     name = path_.split('/')[8].replace('scene','depth')
#     if not os.path.exists( os.path.join(dir1,name) ):
#         f1a.write(line)
#         add += 1
# print(add)


# f1a = open('/data1/zlf/OULU_NPU_zlf/2_dev/dev_add.txt','r')
# lines = f1a.readlines()
# list1 = [] 
# for line in lines:
#     path_ = line.split(' ')[0]
#     name = path_.split('/')[7]
#     list1.append(name)
# list2 = list(set(list1))
# print(len(list2))

# f2 = open('/data1/zlf/OULU_NPU_zlf/2_dev/Dev.txt','r')
# f3 = open('/data1/zlf/OULU_NPU_zlf/2_dev/Dev_temp.txt','w')
# lines2 = f2.readlines()
# for x in lines2:
#     name2 = x.strip().split(',')[1]
#     if name2 not in list2:
#         f3.write(x)












# a = ('abcd','efg','ljh','dbd')
# print(a[0:3])
# print(a[2][0:2])




'''
# 每个ID间隔取8帧
root = '/data2/scy/face_data/OULU-NPU/OULU_pic/Test_images'  # TODO
f = open('/data1/zlf/OULU_NPU_zlf/3_test/test_all.txt','w')  # TODO
f8 = open('/data1/zlf/OULU_NPU_zlf/3_test/test_8.txt','w')   # TODO
for camera in range(1,7):
    for session in range(1,4):
        for user in range(36,56):   # TODO  # Train_images 1-20; Dev_images 21-35; Test_images 36-55  
            for file in range(1,6):
                if user < 10:
                    dirID = str(camera)+'_'+str(session)+'_0'+str(user)+'_'+str(file)
                else:
                    dirID = str(camera)+'_'+str(session)+'_'+str(user)+'_'+str(file)
                # print(dirID)  # x_x_xx_x
                if file == 1:
                    label = '1'
                else:
                    label = '0'

                path = os.path.join(root,dirID)  # /data2/scy/face_data/OULU-NPU/OULU_pic/Train_images/x_x_xx_x
                FileNames = os.listdir(path)
                framesAll = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])//3
                interval = framesAll//10

                for FileName in FileNames:   # FileName = x_x_xx_x_xxx_scene.jpg
                    if ( FileName[13:] == 'scene.jpg' ): # and ( FileName[9:12] in list ):
                        datName = FileName.replace('.jpg','.dat')
                        if  os.path.exists(os.path.join(path,FileName)) and os.path.exists(os.path.join(path,datName)):
                            f.write(os.path.join(path,FileName)+' '+ label +'\n')
                x = 0
                for i in range(8):
                    image_id = i*interval + 1
                    for temp in range(500):
                        _ = "_%03d_scene.jpg" % image_id
                        jpgFile = dirID + _
                        datFile = jpgFile.replace('.jpg','.dat')
                        if os.path.exists(os.path.join(path,jpgFile)) & os.path.exists(os.path.join(path,datFile)):    # some scene.dat are missing
                            f8.write(os.path.join(path,jpgFile)+' '+ label +'\n')
                            x += 1
                            break
                        else:
                            image_id +=1
                if x!= 8:
                    print('dirID:',dirID,'帧数：',x)
'''

# # root = '/data2/scy/face_data/OULU-NPU/OULU_pic/Test_images'
# f2 = open('/data1/zlf/OULU_NPU_zlf/2_dev/dev_1_p1.txt','r')
# # f2 = open('/data1/zlf/OULU_NPU_zlf/Protocols/Protocol_1/Dev.txt','r')
# lines = f2.readlines()
# for line in lines:
#     # videoname = line.strip().split(',')[1]
#     # if videoname[-1] == '1':
#     #     label = '1'
#     # else:
#     #     label = '0'
#     # path = os.path.join(root,videoname)
#     # frame = videoname + '_001_scene.jpg'
#     # f.write(os.path.join(path,frame)+' '+ label +'\n')
#     # dir = os.path.join(path,frame)
#     dir = line.strip().split(' ')[0]
#     dat = dir.replace('.jpg','.dat')
#     if not (os.path.exists(dat)):
#         print(dir)




'''                    
# dirID: 1_2_09_4 帧数： 6
# dirID: 1_2_11_5 帧数： 8
# dirID: 2_1_01_5 帧数： 7   #
# dirID: 2_1_02_5 帧数： 6   #
# dirID: 2_1_03_5 帧数： 7   #
# dirID: 2_1_09_5 帧数： 8   #
# dirID: 2_1_10_5 帧数： 8   #
# dirID: 2_1_11_5 帧数： 7   #
# dirID: 2_1_12_5 帧数： 7   #
# dirID: 2_1_13_5 帧数： 6   #
# dirID: 2_1_14_5 帧数： 6   #
# dirID: 2_1_15_5 帧数： 9   #
# dirID: 2_1_16_5 帧数： 9   #
# dirID: 2_1_17_5 帧数： 6   #
# dirID: 2_1_18_5 帧数： 7   #
# dirID: 2_1_19_5 帧数： 8   #
# dirID: 2_1_20_5 帧数： 7   #
# dirID: 2_2_01_5 帧数： 9   #
# dirID: 2_2_07_5 帧数： 9   #
# dirID: 2_2_08_5 帧数： 8   #
# dirID: 2_2_09_5 帧数： 9   #
# dirID: 2_2_10_5 帧数： 8   #
# dirID: 2_2_11_5 帧数： 8   #
# dirID: 2_2_14_5 帧数： 9   #
# dirID: 2_2_15_5 帧数： 8   #
# dirID: 2_2_16_5 帧数： 8   #
# dirID: 2_2_17_5 帧数： 9   #
# dirID: 3_2_09_4 帧数： 3   # 20-70缺少很多帧
# dirID: 3_2_09_5 帧数： 3   # 60-120缺少很多帧
# dirID: 3_2_11_5 帧数： 1   # 缺少很多帧
# dirID: 3_2_16_3 帧数： 9   #
# dirID: 3_2_17_5 帧数： 3   # 缺少很多帧
# dirID: 4_2_11_4 帧数： 9
# dirID: 5_3_14_5 帧数： 9
# dirID: 6_3_12_5 帧数： 9
'''

'''
# 对fake人脸生成全零伪标签
f = open('/data1/zlf/OULU_NPU_zlf/1_train/train_rgb_fake.txt','r')
savefolder = '/data1/zlf/OULU_NPU_zlf/1_train/label_artifical'
lines = f.readlines()
for line in tqdm(lines):
    path = line.strip().split(' ')[0]
    image = cv2.imread(path)
    label_pic = image*0
    name = path.split('/')[-1].replace('face','depth')
    cv2.imwrite(os.path.join(savefolder,name),label_pic)
'''

'''
# 写训练CDCN的list —— trainCDCN.txt
# /data2/scy/face_data/OULU-NPU/OULU_pic/Train_images/6_3_09_1/6_3_09_1_011_face.jpg  /data1/zlf/OULU_NPU_zlf/1_train/label_artifical/6_3_09_1_011_depth.jpg 
f1 = open('/data1/zlf/OULU_NPU_zlf/3_test/test_1_p11.txt','r')
f2 = open('/data1/zlf/OULU_NPU_zlf/3_test/test_1_p1.txt','w')
label_root = '/data1/zlf/OULU_NPU_zlf/3_test/test_artificial_label_scene'
lines = f1.readlines()
for line in tqdm(lines):
    rgb_path = line.strip().split(' ')[0]
    b_label = line.strip().split(' ')[1]
    label = rgb_path.split('/')[-1].replace('scene','depth')
    label_path = os.path.join(label_root,label)
    f2.write(rgb_path + ' ' + label_path + ' ' + b_label + '\n')
'''


'''
f1 = open('/data1/zlf/OULU_NPU_zlf/1_train/trainCDCN_1.txt','r')
f2 = open('/data1/zlf/OULU_NPU_zlf/1_train/trainCDCN.txt','w')
lines = f1.readlines()
for line in tqdm(lines):
    rgb_path = line.strip().split(' ')[0]
    name = rgb_path.split('/')[7]
    print(name)
    session = name.split('_')[1]
    if session == '1' or session == '2':
        f2.write(line)
'''


import math
import imgaug.augmenters as iaa

'''
seq = iaa.Sequential([
    iaa.Add(value=(-40,40), per_channel=True), # Add color 
    iaa.GammaContrast(gamma=(0.5,1.5)) # GammaContrast with a gamma of 0.5 to 1.5
])

def crop_face_from_scene(image,face_name_full, scale):
    ## image = 未裁剪的RGB图像
    ## face_name_full = bbox_path
    ## scale = face_scale       ## 1.2~1.5
    f=open(face_name_full,'r')
    lines=f.readlines()
    y1,x1,w,h=[float(ele) for ele in lines[:4]]
    print('y1:',y1,'x1:',x1,'w:',w,'h:',h)
    f.close()
    y2=y1+w
    x2=x1+h

    y_mid=(y1+y2)/2.0
    x_mid=(x1+x2)/2.0
    h_img, w_img = image.shape[0], image.shape[1]
    print('h_img:',h_img,'w_img:', w_img)

    # w_img,h_img=image.size
    w_scale=scale*w
    h_scale=scale*h
    y1=y_mid-w_scale/2.0
    x1=x_mid-h_scale/2.0
    y2=y_mid+w_scale/2.0
    x2=x_mid+h_scale/2.0
    y1=max(math.floor(y1),0)
    x1=max(math.floor(x1),0)
    y2=min(math.floor(y2),w_img)
    x2=min(math.floor(x2),h_img)
   
    region=image[x1:x2,y1:y2]   # region = image[y1:y2,x1:x2]
    
    return region

image = cv2.imread('/data1/zlf/zlf_some_pics/1_1_01_1_001_scene.jpg')
face_name_full = '/data1/zlf/zlf_some_pics/1_1_01_1_001_scene.dat'
scale = 13
scale = scale/10.0

image_crop = crop_face_from_scene(image, face_name_full, scale)
cv2.imwrite('/data1/zlf/zlf_some_pics/1_1_01_001_1crop_1.3.jpg',image_crop)

image_x = cv2.resize(crop_face_from_scene(image, face_name_full, scale), (256, 256))
cv2.imwrite('/data1/zlf/zlf_some_pics/1_1_01_001_2resize_1.3.jpg',image_x)

image_x_aug = seq.augment_image(image_x) 
cv2.imwrite('/data1/zlf/zlf_some_pics/1_1_01_001_3aug_1.3.jpg',image_x_aug)
'''