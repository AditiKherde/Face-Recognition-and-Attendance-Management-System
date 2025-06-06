import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendencerealtime-53f21-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendencerealtime-53f21.appspot.com"
})

# IMPORTING THE STUDENT IMAGES INTO A LIST
folderPath = 'Images'
PathList = os.listdir(folderPath)
print(PathList)
imgList = []
studentIds = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])   # here we re splitting the image path "id.png" into ("id","png") and using the index 1 i.e id only by providing [0]
    # print(path)
    # print(os.path.splitext(path)[0])
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
print(studentIds)

# loop through all the images and encode every single image
def findEncoding(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncoding(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
# print(encodeListKnown)  # result of encoding for self knowledge
print("Encoding Complete")

# saving encoding of image in a pickle file so, that we can use/import it while using webcam
# we need to save both encodings as well as the id files representing the encoding to respective ids done in line 31

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File saved")