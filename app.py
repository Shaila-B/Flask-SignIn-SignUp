from flask import Flask
import pymongo
app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.yjgy4.mongodb.net/user?retryWrites=true&w=majority")
db = client.test

@app.route('/')
def index():
    return render('HOME')

if __name__ == '__main__':
    app.run()
