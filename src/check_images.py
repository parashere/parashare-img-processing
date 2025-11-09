import os
from PIL import Image

def is_valid_image(path):
    try:
        with Image.open(path) as img:
            img.verify()
        return True
    except Exception:
        return False

def check_images(base_dirs):
    result = {}

    for base_dir in base_dirs:
        print(f"\n[確認対象ディレクトリ]: {base_dir}")
        result[base_dir] = {}
        for label in ['normal', 'damaged']:
            folder_path = os.path.join(base_dir, label)
            valid = 0
            invalid = 0
            invalid_files = []

            if not os.path.isdir(folder_path):
                print(f"⚠ フォルダが見つかりません: {folder_path}")
                continue

            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path):
                    if is_valid_image(file_path):
                        valid += 1
                    else:
                        invalid += 1
                        invalid_files.append(file_path)

            result[base_dir][label] = {
                "valid": valid,
                "invalid": invalid,
                "invalid_files": invalid_files
            }

            print(f"  ├─ {label} - 有効: {valid}枚, 無効: {invalid}枚")
            if invalid > 0:
                print(f"  └─ 無効ファイル一覧:")
                for f in invalid_files:
                    print(f"      - {f}")

    return result

# 実行
base_dirs = ["data/raw", "data/test"]
check_images(base_dirs)
