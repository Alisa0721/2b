import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.document("111")
docs = collection_ref.where("Code","==", "3423").get()
for doc in docs:
    print("課程為： " + result["Course"])
    print("老師為： " + result["Leacture"])

