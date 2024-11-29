import os
from utils import read_json, write_json

DATASET = "../dataset/ann"

JSON_DATASET = "../dataset/image_ann"


def getFiles(path):
    json_files = []
    for file in os.listdir(path):
        json_files.append({"file_name": file, "path": os.path.join(path, file)})
    return json_files


def serialize_json(file):
    json = read_json(file["path"])
    
    file_name = file["file_name"].replace(".jpg", "")
    
    left_eye_index = 0
    
    if json["objects"][0]["tags"][0]["value"] == 1223196538:
        left_eye_index = 1
    
    left_eye_x = json["objects"][left_eye_index]["points"]["exterior"][0][0]
    left_eye_y = json["objects"][left_eye_index]["points"]["exterior"][0][1]
    left_eye_w = json["objects"][left_eye_index]["points"]["exterior"][1][0] - left_eye_x
    left_eye_h = json["objects"][left_eye_index]["points"]["exterior"][1][1] - left_eye_y
    left_eye = {"x": left_eye_x, "y": left_eye_y, "w": left_eye_w, "h": left_eye_h}
    
    right_eye_x = json["objects"][1 if left_eye_index == 0 else 0]["points"]["exterior"][0][0]
    right_eye_y = json["objects"][1 if left_eye_index == 0 else 0]["points"]["exterior"][0][1]
    right_eye_w = json["objects"][1 if left_eye_index == 0 else 0]["points"]["exterior"][1][0] - right_eye_x
    right_eye_h = json["objects"][1 if left_eye_index == 0 else 0]["points"]["exterior"][1][1] - right_eye_y
    right_eye = {"x": right_eye_x, "y": right_eye_y, "w": right_eye_w, "h": right_eye_h}
    
    data = {"file": file_name, "size":json["size"] ,"objects": [{"label": "left_eye", "points": left_eye}, {"label": "right_eye", "points": right_eye}]}
    
    write_json(data, os.path.join(JSON_DATASET, file_name))
    
    
def convert_files(files):
    for file in files:
        serialize_json(file)


files = getFiles(DATASET)
convert_files(files)