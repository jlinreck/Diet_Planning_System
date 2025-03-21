import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Path to your Firebase credentials
cred_path = "dietplanningsystem-firebase-adminsdk-fbsvc-f52d76285d.json"  

# Initialize Firebase
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

# Get Firestore database client
db = firestore.client()