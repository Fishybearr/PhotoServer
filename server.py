import sqlite3
import os
import time
import datetime

#TODO implement flask and create a simple html page to fetch images from the server based on the paths read from the DB


#TODO: add a try catch or some kind of exception to this function when adding an image.
#need to make sure that the image is actually added and isn't already in the DB

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

    con = sqlite3.connect("images.db")
    cur = con.cursor()
    cur.execute(f"INSERT INTO images (image_path,date_created) VALUES ('{photoPath}','{date}')")
    con.commit()
    cur.close()
    con.close()

    
con = sqlite3.connect("images.db")

cur = con.cursor()

cur.execute("SELECT image_path FROM images WHERE date_created BETWEEN '1900-01-01' AND '2050-01-01' ORDER BY date_created") #TODO: Change these dates used for the between
response = cur.fetchall()
cur.close()

print(response)
con.close()

AddPhotoToDB("G:/PhotoServer/Images/CypFocused.png")