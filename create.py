import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = {
  "Code": "3420",
  "Course": "企業資源規劃",
  "Leacture": "莊育維",
  "Time" : "四2、3、4",
  "Room" : "主顧322"
}

doc_ref = db.collection("111").document("3420")
doc_ref.set(doc)
