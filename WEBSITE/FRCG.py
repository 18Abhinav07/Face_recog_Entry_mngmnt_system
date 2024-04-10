import face_recognition
import os

def get_name(known_image, db_path):
    known_image = face_recognition.load_image_file(known_image)
    print("image loaded")
    
    known_encoding = face_recognition.face_encodings(known_image)[0]
    for file in os.walk(db_path):
        print("files in db path------------>" ,file)
        for f in file[2]:
            if f.endswith('.jpg'):
                #print(f)
                unknown_image = face_recognition.load_image_file(os.path.join(db_path + f))
                unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
                #print(len(unknown_encoding))
                #print(f)
                results = face_recognition.compare_faces([known_encoding], unknown_encoding)
                if results[0]:
                    return db_path

def res(file):
    print('file sent by user :',file)
    file_path = './WEBSITE/train/'
    for dirs in os.walk(file_path):
        print("----------->")
        print(dirs)
        for d in dirs[1]:
            db_path = './WEBSITE/train/'+d+'/'
            print("------------>" ,file)
            print("db_path",db_path)
            print('dirs', d)
            print("----------->" ,file) 
            res = get_name(file, db_path)
            print('result',res)
        if res:
            return res
        else:
            return 0
           

