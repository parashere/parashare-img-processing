===========================================
傘破損判定システム - README
===========================================

本プロジェクトは、傘の画像から「破損しているかどうか」を判定するAIモデルを使用した画像分類システムです。  
TensorFlowを用いて事前学習したCNNモデルを使い、コマンドラインから画像を判定できます。

-------------------------------------------
■ 動作環境
-------------------------------------------
- OS       : Windows 10 以降
- Python   : 3.8〜3.10
- TensorFlow : 2.10（GPU対応環境推奨）
- その他必要ライブラリは `requirements.txt` に記載

仮想環境の例:
conda create -n umbrella-cnn-gpu python=3.8
conda activate umbrella-cnn-gpu
pip install -r requirements.txt


-------------------------------------------
■ ディレクトリ構成（例）
-------------------------------------------

umbrella/
├── data/
│ └── augmented/ ← かさまし画像
│  ├── broken/
│  └── normal/
│ └── processed/ ← 整形画像
│  ├── broken/
│  └── normal/
│ └── raw/ ← 元画像
│  ├── broken/
│  └── normal/
├── models/
│ └── umbrella_damage_cnn.h5 ← 学習済みモデル
├── src/
│ ├── augment_data.py ← 画像かさましスクリプト
│ ├── predict.py ← 判定スクリプト
│ ├── prepare_data.py ← 画像整形スクリプト
│ └── train_model.py ← モデル学習用スクリプト
├── requirements.txt
└── README.txt


-------------------------------------------
■ 実行方法（判定）
-------------------------------------------

1. モデルが `models/umbrella_damage_cnn.h5` に保存されていることを確認
2. 判定したい画像のパスを指定して、以下のように実行：

例：python src/predict.py data/augmented/normal/normal_01_aug0.jpg


■ 補足
・GPUを使う場合、CUDA / cuDNN の設定が必要です

・TensorFlowがGPUを正しく認識しているかは、実行ログで確認できます