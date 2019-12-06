# This python script sets up a sample database in cloud firestore.

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('path/to/serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'users').document(u'rfidtag1')
doc_ref.set({
    u'first': u'Arna',
    u'last': u'Maity',
    u'DOB': 1815 ,
    u'Aadhar': '8745****2143',
    u'PAN': u'FXC******A',
    u'DLNO': u'WB-15-2009-xxxxxxx',
    u'PHNO': u'8815424723'
})

doc_ref = db.collection(u'users').document(u'rfidtag2')
doc_ref.set({
    u'first': u'Abhijeet',
    u'last': u'Choudhuri',
    u'DOB': 1912 ,
    u'Aadhar': '6234****1298',
    u'PAN': u'CXZ******B',
    u'DLNO': u'OD-16-2010-xxxxxxx',
    u'PHNO': u'8912735331'
})

doc_ref = db.collection(u'users').document(u'rfidtag3')
doc_ref.set({
    u'first': u'Auroshis',
    u'last': u'Ray',
    u'DOB': 1912 ,
    u'Aadhar': '5143****6198',
    u'PAN': u'LCX******D',
    u'DLNO': u'OD-13-2011-xxxxxxx',
    u'PHNO': u'8265159324'
})

doc_ref = db.collection(u'users').document(u'rfidtag4')
doc_ref.set({
    u'first': u'Ashish',
    u'last': u'Pradhan',
    u'DOB': 1912 ,
    u'Aadhar': '4194****1963',
    u'PAN': u'DCR******R',
    u'DLNO': u'OD-14-2010-xxxxxxx',
    u'PHNO': u'9286418643'
})

doc_ref = db.collection(u'users').document(u'rfidtag5')
doc_ref.set({
       u'first': u'Pranav',
    u'last': u'Donepudi',
    u'DOB': 1912 ,
    u'Aadhar': '6914****8954',
    u'PAN': u'BRX******C',
    u'DLNO': u'AP-14-2014-xxxxxxx',
    u'PHNO': u'9008352654'
})
