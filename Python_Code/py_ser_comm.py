import serial
import firebase_admin
from firebase_admin import credentials, firestore

arduinoData = serial.Serial('/dev/ttyACM0', 9600)
arduinoData.flushInput()

# Use a service account
cred = credentials.Certificate('path/to/serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

rtag = ""
while(arduinoData.in_waiting > 0):
    rtag = arduinoData.readline()

rtag = rtag.strip()
print(type(rtag))
rtag = rtag.decode()
print(rtag)

users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
