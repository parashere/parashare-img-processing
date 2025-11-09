import os
from PIL import Image, ImageEnhance
import random

INPUT_DIR = "data/processed"
OUTPUT_DIR = "data/augmented"
AUG_PER_IMAGE = 10  # 1枚の画像につき何枚拡張するか
IMAGE_SIZE = (512, 512)

os.makedirs(OUTPUT_DIR, exist_ok=True)

for class_name in ["normal", "damaged"]:
    input_class_dir = os.path.join(INPUT_DIR, class_name)
    output_class_dir = os.path.join(OUTPUT_DIR, class_name)
    os.makedirs(output_class_dir, exist_ok=True)

    for filename in os.listdir(input_class_dir):
        img_path = os.path.join(input_class_dir, filename)
        image = Image.open(img_path).convert("RGB")
        base_name = os.path.splitext(filename)[0]

        for i in range(AUG_PER_IMAGE):
            aug_image = image.copy()

            # ランダム回転
            angle = random.randint(-25, 25)
            aug_image = aug_image.rotate(angle)

            # 左右反転（50%）
            if random.random() > 0.5:
                aug_image = aug_image.transpose(Image.FLIP_LEFT_RIGHT)

            # 明るさ調整（0.8〜1.2倍）
            enhancer = ImageEnhance.Brightness(aug_image)
            factor = random.uniform(0.8, 1.2)
            aug_image = enhancer.enhance(factor)

            # 保存
            out_filename = f"{base_name}_aug{i}.jpg"
            out_path = os.path.join(output_class_dir, out_filename)
            aug_image.resize(IMAGE_SIZE).save(out_path)

        print(f"Augmented: {filename} -> {AUG_PER_IMAGE}枚")
