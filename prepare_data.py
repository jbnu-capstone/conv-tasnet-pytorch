import os
import subprocess
import argparse
import sys
import shutil
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument('--gd_id', type=str, default="1AeLxV4qEaPs0GYZgkQCkQTitz5egT_MV")
parser.add_argument('-f', action='store_true')
args = parser.parse_args()

EXTRACT_DIR = "./dataset/data"
ZIP_NAME = "data.zip"

# 기존 폴더가 존재하고 -f 옵션이 없으면 종료
if os.path.exists(EXTRACT_DIR) and not args.f:
    print("dataset already exists. try -f option to force overwrite")
    sys.exit(1)

# 기존 압축 해제 폴더 삭제 (강제 덮어쓰기)
if os.path.exists(EXTRACT_DIR):
    shutil.rmtree(EXTRACT_DIR)

# gdown 설치
subprocess.run(["pip", "install", "-q", "gdown"])

# 다운로드
subprocess.run(["gdown", f"https://drive.google.com/uc?id={args.gd_id}", "-O", ZIP_NAME])

# 압축 해제
os.makedirs(EXTRACT_DIR, exist_ok=True)
with zipfile.ZipFile(ZIP_NAME, 'r') as zip_ref:
    zip_ref.extractall(EXTRACT_DIR)

# __MACOSX 제거
macosx_path = os.path.join(EXTRACT_DIR, "__MACOSX")
if os.path.exists(macosx_path):
    shutil.rmtree(macosx_path)

# zip 삭제
if os.path.exists(ZIP_NAME):
    os.remove(ZIP_NAME)

# 후처리 스크립트 실행
subprocess.run(["python", "create_scp.py"])