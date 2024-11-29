import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import cv2

import tensorflow as tf

from tensorflow.keras.models import load_model

from keras.models import load_model
from keras.metrics import MeanSquaredError

from utils import preprocess_image, image_preprocess, image_tf_resize, preprocess_img, straightening, convert

DATASET = "../dataset/img"

# Load the saved model from the specified file path
model = load_model("model_v_0_4.h5", custom_objects={'mse': MeanSquaredError()})

files = [os.path.join(DATASET, file) for file in os.listdir(DATASET)]

# file = preprocess_image(files[0])

# input_data_resized = tf.expand_dims(file, axis=0)
# print("files: ", input_data_resized.shape)

# model_out = model.predict(input_data_resized)
# print("model_out: ", model_out)
# print("model_out: ", model_out)

# Вказуємо шлях до вашого відеофайлу
# video_path = "istockphoto-684455148-640_adpp_is.mp4"
video_path = "test_1.mp4"

# Відкриваємо відео за допомогою cv2.VideoCapture
cap = cv2.VideoCapture(video_path)

# ret, frame = cap.read()

resize_w = 400
resize_h = 200

h_coef = resize_h / 432
w_resize = resize_w / 768

# out = preprocess_img(frame, resize_h, resize_w)

# print(out.shape)

# model_out = model.predict(out)

# straightforward = straightening(model_out)

# print("straightforward: ", straightforward[0])


# input_data_resized = tf.expand_dims(out, axis=0)

# model_out = model.predict(input_data_resized)
# print("model_out: ", model_out)

# # print("frame: ", frame)

# input_data_resized = tf.expand_dims(frame, axis=0)

# model_out = model.predict(input_data_resized)

# # print("model_out: ", model_out)

# left_eye_points = model_out[0][:4]

# right_eye_points = model_out[0][4:]

# left_eye_top_left = (left_eye_points[0], left_eye_points[1])
# left_eye_bottom_right = (left_eye_points[2] + left_eye_points[0], left_eye_points[3] + left_eye_points[1])

# right_eye_top_left = (right_eye_points[0], right_eye_points[1])
# right_eye_bottom_right = (right_eye_points[2] + right_eye_points[0], right_eye_points[3] + right_eye_points[1])

# print("left_eye_top_left: ", left_eye_top_left)
# print("left_eye_bottom_right: ", left_eye_bottom_right)

# print("right_eye_top_left: ", right_eye_top_left)
# print("right_eye_bottom_right: ", right_eye_bottom_right)





frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # Use a different codec if needed (e.g., 'MJPG', 'MP4V')
cv_out = cv2.VideoWriter('output_1.mp4', fourcc, 20.0, (frame_width, frame_height))

# Перевіряємо, чи вдалося відкрити відеофайл
if not cap.isOpened():
    print("Не вдалося відкрити відеофайл.")
else:
    while True:
        # Зчитуємо кадр
        ret, frame = cap.read()
        
        out = preprocess_img(frame, resize_h, resize_w)
        
        model_out = model.predict(out)
        
        straightforward = straightening(model_out)
        
        left_eye_points = straightforward[0][:4]

        right_eye_points = straightforward[0][4:]

        left_eye_top_left = (int(left_eye_points[0]), int(left_eye_points[1]))
        left_eye_bottom_right = (int(left_eye_points[2] + left_eye_points[0]), int(left_eye_points[3] + left_eye_points[1]))

        right_eye_top_left = (int(right_eye_points[0]), int(right_eye_points[1]))
        right_eye_bottom_right = (int(right_eye_points[2] + right_eye_points[0]), int(right_eye_points[3] + right_eye_points[1]))
        
        red_color = (255, 0, 0) 
        green_color = (0, 255, 0)
        thickness = 2
        
        try:
            cv2.rectangle(frame, left_eye_top_left, left_eye_bottom_right, red_color, thickness)
            cv2.rectangle(frame, right_eye_top_left, right_eye_bottom_right, green_color, thickness)
        except Exception as e:
            print("error: ", e)
            print("error: model_out", model_out, " left_eye_top_left: ", left_eye_top_left, " left_eye_bottom_right: ", left_eye_bottom_right)


        
        # Якщо кадр вдалося зчитати, відображаємо його
        if ret:
            cv_out.write(frame)
            # cv2.imshow('Відео', frame)
        else:
            break  # Якщо кадри закінчились, вийдемо з циклу

        # Вихід з відображення відео при натисканні клавіші 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Закриваємо відео та всі вікна
cap.release()
cv2.destroyAllWindows()