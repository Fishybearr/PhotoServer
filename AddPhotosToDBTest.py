import sqlite3
import datetime
import os

def AddPhotoToDB(photoPath):
    print("adding photo to DB:\n")
    
    date = "";

    mTime =  os.path.getmtime(photoPath)
    mDate = datetime.datetime.fromtimestamp(mTime)
    mDate = mDate.strftime("%Y-%m-%d %H:%M:%S")
    print(mDate)

    cTime = os.path.getctime(photoPath)
    cDate = datetime.datetime.fromtimestamp(cTime)
    cDate = cDate.strftime("%Y-%m-%d %H:%M:%S")
    print(cDate)

    if(cTime < mTime):
        print("createdFirst")
        date = cDate
    else:
        print("modifedFirst")
        date = mDate

    photoPath = "/" + photoPath[photoPath.find('static'):]
    print(photoPath)


    con = sqlite3.connect("images.db")
    cur = con.cursor()
    cur.execute(f"INSERT INTO images (image_path,date_created) VALUES ('{photoPath}','{date}')")
    con.commit()
    cur.close()
    con.close()

directory = "G:/PhotoServer/static/Images"

for file in os.listdir(directory):
    file = os.path.join(directory,file)
    print(file)

#AddPhotoToDB("G:/PhotoServer/static/Images/BrightTrees.png")
#AddPhotoToDB("G:/PhotoServer/static/Images/AmericanCyp.png")
#AddPhotoToDB("G:/PhotoServer/static/Images/RidgeLine.png")
