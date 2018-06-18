# this file extracts the cifar-10 data set
import mxnet as mx
import numpy as np
import cPickle
import cv2

def extract_images(path, file):
    f = open(path + file, 'rb')
    dict = cPickle.load(f)
    images = dict['data']
    images = np.reshape(images, (10000, 3, 32, 32))
    image_array = mx.nd.array(images)
    return image_array

def save_cifar_image(array, path, file):

    # array is 3x32x32. cv2 needs 32x32x3
    array = array.asnumpy().transpose(1,2,0)

    # array is RGB. cv2 needs BGR
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)

    # save to PNG file
    return cv2.imwrite(path+file+".png", array)

def extract_batch(batch_path, new_location):
    img_array = extract_images("cifar-10-batches-py/", batch_path)
    num_of_images = img_array.shape[0]
    for i in range(0, num_of_images):
        save_cifar_image(img_array[i], new_location, "image" + (str)(i))
        print "saved " + str(i)