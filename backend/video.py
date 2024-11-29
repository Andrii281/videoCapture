import cv2
import os

from utils import read_json

DATASET = "../dataset/img"

ANNOTATION = "../dataset/image_ann"

images = os.listdir(DATASET)
frame_rate = 30

if not images:
    print("No images found in the folder")
    exit()
    
cv2.namedWindow('Video Stream', cv2.WINDOW_NORMAL)

while True:
    for image_name in images:
        image_path = os.path.join(DATASET, image_name)
        image_annotation_path = os.path.join(ANNOTATION, image_name.replace(".jpg", ".json"))
        image_json = read_json(image_annotation_path)
        image = cv2.imread(image_path)

        if image is None:
            continue
        
        # print("asd: ", image_json["objects"][0]["points"])
        
        left_eye_points = image_json["objects"][0]["points"]
        
        left_eye_top_left = (left_eye_points["x"], left_eye_points["y"]) 
        left_eye_bottom_right = (left_eye_points["x"] + left_eye_points["w"], left_eye_points["y"] + left_eye_points["h"])
        
        right_eye_points = image_json["objects"][1]["points"]
        
        right_eye_top_left = (right_eye_points["x"], right_eye_points["y"]) 
        right_eye_bottom_right = (right_eye_points["x"] + right_eye_points["w"], right_eye_points["y"] + right_eye_points["h"])
        
        red_color = (255, 0, 0) 
        green_color = (0, 255, 0)
        thickness = 2
        
        cv2.rectangle(image, left_eye_top_left, left_eye_bottom_right, red_color, thickness)
        cv2.rectangle(image, right_eye_top_left, right_eye_bottom_right, green_color, thickness)
        
        cv2.imshow('Video Stream', image)
        

        if cv2.waitKey(int(1000 / frame_rate)) & 0xFF == ord('q'):
            break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.destroyAllWindows()
    
# -------------------------------------------------------

# image_name = images[0]

# image_path = os.path.join(DATASET, image_name)
# image_annotation_path = os.path.join(ANNOTATION, image_name.replace(".jpg", ".json"))

# image_json = read_json(image_annotation_path)
# print("image_annotation: ", image_json)
# image = cv2.imread(image_path)

# cv2.imshow('Video Stream', image)

