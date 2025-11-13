import os
from datetime import datetime
from pathlib import Path

import firebase_admin
from firebase_admin import credentials, firestore


FIREBASE_CRED_PATH = Path(
    os.getenv(
        "G2B_FIREBASE_CRED_PATH",
        Path(__file__).resolve().parent / "g2b-bid-finder-firebase-adminsdk-fbsvc-aae6f1c96d.json",
    )
)
FIREBASE_COLLECTION = os.getenv("G2B_FIREBASE_COLLECTION", "bid_pblanc_list")
BATCH_SIZE = 400


def get_client() -> firestore.Client:
    if not FIREBASE_CRED_PATH.exists():
        raise FileNotFoundError(f"Firebase credential file not found: {FIREBASE_CRED_PATH}")
    if not firebase_admin._apps:
        cred = credentials.Certificate(str(FIREBASE_CRED_PATH))
        firebase_admin.initialize_app(cred)
    return firestore.client()


def update_collected_at():
    client = get_client()
    collected_at = datetime.now().isoformat()
    docs = list(client.collection(FIREBASE_COLLECTION).stream())

    if not docs:
        print("⚠️ 업데이트할 문서가 없습니다.")
        return

    print(f"총 {len(docs)}건의 문서에 collectedAt='{collected_at}'을(를) 설정합니다.")

    batch = client.batch()
    updated = 0

    for idx, doc in enumerate(docs, start=1):
        batch.update(doc.reference, {"collectedAt": collected_at})
        if idx % BATCH_SIZE == 0:
            batch.commit()
            updated += BATCH_SIZE
            print(f"  {updated}건 완료")
            batch = client.batch()

    if docs and len(docs) % BATCH_SIZE != 0:
        batch.commit()
        updated = len(docs)
        print(f"  {updated}건 완료")

    print("✅ 업데이트가 완료되었습니다.")


if __name__ == "__main__":
    update_collected_at()

