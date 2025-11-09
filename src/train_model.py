import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models

# データセットのディレクトリ
DATA_DIR = "data/processed" 

# パラメータ
IMG_SIZE = (512, 512)
BATCH_SIZE = 8
EPOCHS = 10

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_gen = datagen.flow_from_directory(
    DATA_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='training'
)

val_gen = datagen.flow_from_directory(
    DATA_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='validation'
)

# CNNモデルの構築
model = models.Sequential([
    layers.Input(shape=(*IMG_SIZE, 3)),
    layers.Conv2D(16, (3,3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, (3,3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# モデル概要を表示
model.summary()

# 学習の実行
history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=EPOCHS
)

# モデル保存
os.makedirs("models", exist_ok=True)
model.save("models/umbrella_damage_cnn.h5")
print("✅ モデル保存完了: models/umbrella_damage_cnn.h5")
