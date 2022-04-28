import io

import cv2
import numpy as np
import argparse

from PIL import Image
from path import Path
import os
from keras.models import Model
from keras.layers import Dense, Dropout
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.applications.inception_resnet_v2 import preprocess_input
from keras.preprocessing.image import load_img, img_to_array
import tensorflow as tf
from utils.score_utils import mean_score, std_score
import base64

def run(num):
    print("进入模型!")
    img = []
    score_list1=[]
    for i in num:
        print(i)
        score_list1.append(i)
        # print(num[i])
        a = base64.b64decode(num[i])
        a = io.BytesIO(a)
        a = Image.open(a)
        a = a.resize((224, 224))
        a = np.array(a)
        if a.shape[2] == 4:
            # png图像改为3通道
            print("4！")
            a = a * 255.0
            newa = Image.fromarray(np.uint8(a))
            # print(newa)
            newa = newa.convert("RGB")
            newa = np.array(newa)
            img.append(newa)
        else:
            img.append(a)

    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    parser = argparse.ArgumentParser(description='Evaluate NIMA(Inception ResNet v2)')
    parser.add_argument('-dir', type=str, default='./dir/',
                        help='Pass a directory to evaluate the images in it')

    parser.add_argument('-img', type=str, default='./dir/*.png', nargs='+',
                        help='Pass one or more image paths to evaluate them')

    parser.add_argument('-resize', type=str, default='true',
                        help='Resize images to 224x224 before scoring')

    parser.add_argument('-rank', type=str, default='false',
                        help='Whether to tank the images after they have been scored')

    args = parser.parse_args()
    resize_image = args.resize.lower() in ("true", "yes", "t", "1")
    target_size = (224, 224) if resize_image else None
    rank_images = args.rank.lower() in ("true", "yes", "t", "1")

    # give priority to directory
    if args.dir is not None:
        print("Loading images from directory : ", args.dir)
        imgs = Path(args.dir).files('*.png')
        imgs += Path(args.dir).files('*.jpg')
        imgs += Path(args.dir).files('*.jpeg')

    elif args.img[0] is not None:
        print("Loading images from path(s) : ", args.img)
        imgs = args.img

    else:
        raise RuntimeError('Either -dir or -img arguments must be passed as argument')

    fins = {}

    score_list2 = []

    with tf.device('/CPU:0'):
        print("1ss")
        import keras.backend.tensorflow_backend as tb
        tb._SYMBOLIC_SCOPE.value = True
        base_model = InceptionResNetV2(input_shape=(None, None, 3), include_top=False, pooling='avg', weights=None)
        x = Dropout(0.5)(base_model.output)
        # 损失可以调整
        x = Dense(10, activation='softmax')(x)
        model = Model(base_model.input, x)
        model.load_weights('weights/inception_resnet_weights.h5')
        # for img_path in imgs:
        #     img = load_img(img_path, target_size=target_size)
        #     x = img_to_array(img)
        #     x = np.expand_dims(x, axis=0)
        for i, x in enumerate(img):
            # if x.shape[2] == 4:

            # print(x.shape)
            x = np.expand_dims(x, axis=0)
            # print(x.shape)
            x = preprocess_input(x)

            scores = model.predict(x, batch_size=1, verbose=0)[0]

            mean = mean_score(scores)
            print(f"num:{i}____{mean}")
            std = std_score(scores)
            # std表示额外分数
            # file_name = Path(img_path).name.lower()
            # score_list.append((file_name, mean))
            # score_list1.append(file_name)
            score_list2.append(mean)
            # print("Evaluating : ", img_path)
            # print("NIMA Score : %0.3f +- (%0.3f)" % (mean, std))
            # print()
        fins = dict(zip(score_list1, score_list2))
        # 这里默认输出dir下的文件评分
        print(fins)
        # for i, (name, score) in enumerate(score_list):
        #     f = open('./xyz.txt', 'a')
        #     print("%d)" % (i + 1), "%s : Score = %0.5f" % (name, score))
        #     f.write("%d)" % (i + 1) + "%s : Score = %0.5f" % (name, score) + '\n')
        #     f.close()
        #
        # if rank_images:
        #     print("*" * 40, "Ranking Images", "*" * 40)
        #     score_list = sorted(score_list, key=lambda x: x[1], reverse=True)
        return fins

# if __name__ == '__main__':
#     print(run())
# for i, (name, score) in enumerate(score_list):
#     f = open('./xyz.txt', 'a')
#     print("%d)" % (i + 1), "%s : Score = %0.5f" % (name, score))
#     f.write("%d)" % (i + 1) + "%s : Score = %0.5f" % (name, score) + '\n')
#     f.close()
