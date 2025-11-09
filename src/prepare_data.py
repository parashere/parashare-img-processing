import os
from PIL import Image

# 入出力ディレクトリ
RAW_DIR = "data/raw"
OUT_DIR = "data/processed"
CATEGORIES = ["normal", "damaged"]
IMG_SIZE = (512, 512) 

# 出力先ディレクトリを作成
os.makedirs(OUT_DIR, exist_ok=True)
for category in CATEGORIES:
    os.makedirs(os.path.join(OUT_DIR, category), exist_ok=True)

# 処理
for category in CATEGORIES:
    input_dir = os.path.join(RAW_DIR, category)
    output_dir = os.path.join(OUT_DIR, category)
    for filename in os.listdir(input_dir):
        if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
            continue 

        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        try:
            img = Image.open(input_path).convert("RGB")
            img = img.resize(IMG_SIZE)
            img.save(output_path)
            print(f"✔ Saved: {output_path}")
        except Exception as e:
            print(f"⚠ Failed: {input_path} ({e})")
