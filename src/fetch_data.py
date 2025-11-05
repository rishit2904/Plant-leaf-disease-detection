from spinner import *
import threading
import requests
import cv2
import numpy as np
import pandas as pd
import random

#Defining events and thread for spinner
stop_event = threading.Event()
spinner_thread = threading.Thread(target=spinner_task, args=(stop_event,))
spinner_thread.start()


class_labels=[
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
    ]

train=[]
test=[]

for label in class_labels:
    url = "https://api.github.com/repos/spMohanty/PlantVillage-Dataset/contents/raw/segmented/"+label
    with open(r"G:\My Drive\Codes\Tokens\github_token.txt", "r") as f:
        token = f.read().strip()
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url,headers=headers)
    
    if response.status_code == 200:
        files = response.json()
        file_names = [f["download_url"] for f in files]
        file_names=[(x,label) for x in file_names]
        split_factor=[0.75,0.25]         #split_factor
        split_index = int(len(file_names) * split_factor[0])
        train_data = file_names[:split_index]
        test_data = file_names[split_index:]
        train.extend(train_data)
        test.extend(test_data)
    else:
        print("Error:", response.status_code)      
random.shuffle(train)
random.shuffle(test)

df = pd.DataFrame(train+test, columns=["image_url", "class"])
df.to_csv("G:\My Drive\Codes\Python Programming\Mini Projects\leaf_disease_ml_project\data\csv\data.csv", index=False)



# resp = requests.get(url, stream=True).content
# img_array = np.asarray(bytearray(resp), dtype=np.uint8)
# img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
# functions to train model, put image as a parameter
#display image
# cv2.imshow("Tomato Leaf", img)
# cv2.waitKey(0)

    



#spinner
stop_event.set()
spinner_thread.join()