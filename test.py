# check_tel_numbers.py
import os
from pathlib import Path

import firebase_admin
from firebase_admin import credentials, firestore

# 환경 변수 또는 기본 파일 경로
cred_path = os.getenv(
    "G2B_FIREBASE_CRED_PATH",
    Path(__file__).resolve().parent / "g2b-bid-finder-firebase-adminsdk-fbsvc-aae6f1c96d.json",
)

collection_name = os.getenv("G2B_FIREBASE_COLLECTION", "bid_pblanc_list")

if not Path(cred_path).exists():
    raise FileNotFoundError(f"Firebase credential not found: {cred_path}")

if not firebase_admin._apps:
    cred = credentials.Certificate(str(cred_path))
    firebase_admin.initialize_app(cred)

db = firestore.client()
docs = db.collection(collection_name).stream()

for doc in docs:
    data = doc.to_dict()
    tel = data.get("ntceInsttOfclTelNo")
    print(f"{doc.id}: {repr(tel)}")