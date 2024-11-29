import json
import tensorflow as tf
import cv2
import numpy as np


def read_json(file):
    with open(file, 'r') as f:
        return json.load(f)
    

def write_json(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)
        

def preprocess_image(file_path):
    byte_img = tf.io.read_file(file_path)
    img = tf.io.decode_jpeg(byte_img)
    img = tf.image.resize(img, (768, 432))
    img = img / 255.0
    return img

def preprocess_img(frame, resize_h, resize_w):
#   img = cv2.imread(file_path)
  img = tf.image.resize(frame, (resize_h, resize_w))
  img = np.uint8(img.numpy())
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  img = img / 255.0
  img = np.expand_dims(img, axis=-1)
  img = np.expand_dims(img, axis=0)
  return img

def image_preprocess(img):
    img = tf.image.resize(img, (768, 432))
    img = img / 255.0
    return img


def image_tf_resize(img, resize_h, resize_w):
    resized_image = tf.image.resize(img, (resize_h, resize_w))
    image_arr = np.uint8(resized_image.numpy())
    return cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)
    

def image_resize(img, resize):
    return cv2.resize(img, (resize, resize))


def straightening(coords):
    return [coord * 1000 for coord in coords]


def convert(positions, resize_h, resize_w):
    coors = positions[0]
    return [coors[0] / resize_w, coors[1] / resize_h, coors[2] / resize_w, coors[3] / resize_h, coors[4] / resize_w, coors[5] / resize_h, coors[6] / resize_w, coors[7] / resize_h]