import sqlite3
import os
import time
import datetime

from flask import Flask
from flask import render_template
from flask import jsonify

#TODO implement flask and create a simple html page to fetch images from the server based on the paths read from the DB 

#TODO add a function to delete a row from the table (ie remove a file from the server)


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

    photoPath = "/" + photoPath[photoPath.find('static'):]
    print(photoPath)


    con = sqlite3.connect("images.db")
    cur = con.cursor()
    cur.execute(f"INSERT INTO images (image_path,date_created) VALUES ('{photoPath}','{date}')")
    con.commit()
    cur.close()
    con.close()


def RemovePhotoFromDB(photoPath):
    con = sqlite3.connect("images.db")
    cur = con.cursor()
    cur.execute(f"DELETE FROM images WHERE image_path IS '{photoPath}'")
    con.commit()
    cur.close()
    con.close()


#AddPhotoToDB("G:/PhotoServer/static/Images/AmericanCyp.png")
#RemovePhotoFromDB("G:/PhotoServer/Images/CypFocused.png")

app = Flask(__name__)

@app.route('/')
def hello():
   
    return render_template('index.html')

@app.route('/getImages', methods=['GET'])
def GetImages():
    con = sqlite3.connect("images.db")

    cur = con.cursor()

    cur.execute("SELECT image_path FROM images WHERE date_created BETWEEN '1900-01-01' AND '2050-01-01' ORDER BY date_created LIMIT 30 OFFSET 0") #TODO: Change these dates used for the between and change limit and offset
    response = cur.fetchall()
    cur.close()
    con.close()

    return jsonify({"responses":response})

app.run(debug=True)
