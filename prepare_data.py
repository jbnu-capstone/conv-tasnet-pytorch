import os
import subprocess
import argparse
import sys
import shutil
import zipfile

# parser = argparse.ArgumentParser()
# parser.add_argument('--gd_id', type=str, default="109HEAeIQqfRS4NB_GnVvaq3TkXJ3BXMq")
# parser.add_argument('-f', action='store_true')
# args = parser.parse_args()

EXTRACT_DIR = "./dataset/data"
ZIP_NAME = "data.zip"

# # 기존 폴더가 존재하고 -f 옵션이 없으면 종료
# if os.path.exists(EXTRACT_DIR) and not args.f:
#     print("dataset already exists. try -f option to force overwrite")
#     sys.exit(1)

# # 기존 압축 해제 폴더 삭제 (강제 덮어쓰기)
# if os.path.exists(EXTRACT_DIR):
#     shutil.rmtree(EXTRACT_DIR)

# # gdown 설치
# subprocess.run(["pip", "install", "-q", "gdown"])

# # 다운로드
# subprocess.run(["gdown", f"https://drive.google.com/uc?id={args.gd_id}", "-O", ZIP_NAME])

# # 압축 해제
# os.makedirs(EXTRACT_DIR, exist_ok=True)
# with zipfile.ZipFile(ZIP_NAME, 'r') as zip_ref:
#     zip_ref.extractall(EXTRACT_DIR)

# # __MACOSX 제거
# macosx_path = os.path.join(EXTRACT_DIR, "__MACOSX")
# if os.path.exists(macosx_path):
#     shutil.rmtree(macosx_path)

# Find cv, tt, tr directories regardless of their nesting level
for root, dirs, files in os.walk(EXTRACT_DIR):
    if any(dir_name in dirs for dir_name in ['cv', 'tt', 'tr']):
        # Found the directories, move them to EXTRACT_DIR
        for dir_name in ['cv', 'tt', 'tr']:
            if dir_name in dirs:
                src_path = os.path.join(root, dir_name)
                dst_path = os.path.join(EXTRACT_DIR, dir_name)
                # If destination already exists, remove it first
                if os.path.exists(dst_path):
                    shutil.rmtree(dst_path)
                shutil.move(src_path, dst_path)
        break  # Exit after moving the directories

# zip 삭제
if os.path.exists(ZIP_NAME):
    os.remove(ZIP_NAME)

# 후처리 스크립트 실행
subprocess.run(["python", "create_scp.py"])