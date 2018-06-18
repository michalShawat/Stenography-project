from PIL import Image
import numpy as np

# to upload train_x faster
def save_to_bin():
    x = np.loadtxt("train_x")
    np.save("train_x.bin",x)

# create tags set for the images
def create_train_y(batch_size):
    print("create train_y")
    train_y=[]
    vec_0 = batch_size*[0]
    vec_1 = batch_size*[1]
    train_y = np.append(train_y, vec_0)
    train_y = np.append(train_y, vec_1)
    np.savetxt("train_y",train_y)

# create the unencoded half of train_x set
def batch1_in_train_x(batch_size):
    train_x = []
    for i in range(0,batch_size):
        img = Image.open("batch1/image"+str(i)+".png")
        arr = np.array(img)
        arr = arr.flatten()
        train_x.append(arr)
    print("done creating the first half of train_x")
    return train_x

# create the encoded half of train_x set
def batch2_in_train_x(train_x, batch_size, encode_num):
    for i in range(0,batch_size):
        img = Image.open("encoded"+encode_num+"/enc_image" + str(i) + ".png")
        arr = np.array(img)
        arr = arr.flatten()
        train_x.append(arr)
    # save to file
    file_loc = "train"+encode_num+"_x"
    file = open(file_loc,"w")
    np.savetxt(file_loc, train_x)
    file.close()
    print("adding encoded images to train"+encode_num+"_x")