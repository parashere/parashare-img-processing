import sys
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

MODEL_PATH = "models/umbrella_damage_cnn.h5"
IMAGE_PATH = sys.argv[1] 
THRESHOLD = 0.9  # 正常と判断するには高い確信が必要

IMG_SIZE = (512, 512)

model = load_model(MODEL_PATH)

# 画像読み込みと前処理
img = image.load_img(IMAGE_PATH, target_size=IMG_SIZE)
img_array = image.img_to_array(img)
img_array = img_array / 255.0  # 正規化
img_array = np.expand_dims(img_array, axis=0)

prediction = model.predict(img_array)[0][0]

if prediction > THRESHOLD:
    print(f"🟢 正常と判定 (score: {prediction:.3f})")
else:
    print(f"🔴 破損と判定 (score: {prediction:.3f})")
