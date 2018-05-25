import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=['POST'])
def upload():
    target = '/home/kartik/Desktop/Orangewood_gerber/'
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("complete.html")


if __name__ == "__main__":
    app.run(port=80, host='0.0.0.0', thread=True)


"""
Inside the request.files.getlist("") : We get the list of files that we are trying to upload the file 
Then we save that file in the traget directory .

TO know about flask file upload framework , refer here : https://www.youtube.com/watch?v=Exf8RbgKmhM


How to change the Location of File being Uploaded to : 
Search for the "target " , then change its value accordingly.

Always make sure to run the python app usig super user privelages , as 
running the python app on port 80 requires those privelages . 

Refer here : https://stackoverflow.com/questions/38298652/permissionerror-errno-13-permission-denied-flask-run?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa


"""