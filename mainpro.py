import os
from roboflow import Roboflow

if not os.path.exists('output'):
    os.mkdir('output')

rf = Roboflow(api_key="oeNDFzKWWDyLjxNf0Cmp")
project = rf.workspace().project("animefaces")
model = project.version(2).model

input_folder = "D:/Anime_Face_Detection/input"
output_folder = "D:/Anime_Face_Detection/output"
confidence_threshold = 40
overlap_threshold = 30
  
input_files = os.listdir(input_folder)

for input_file in input_files:
    input_path = os.path.join(input_folder, input_file)
    output_path = os.path.join(output_folder, f"prediction_{input_file}")

    print(model.predict(input_path, confidence=confidence_threshold, overlap=overlap_threshold).json())

    prediction = model.predict(input_path, confidence=confidence_threshold, overlap=overlap_threshold)

    prediction.save(output_path)
    print(input_file)
