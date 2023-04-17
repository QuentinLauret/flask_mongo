from flask import Flask, render_template, request, jsonify, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('localhost', 27017, username='quent', password='598c5391')
db = client.flask_db
guitars = db.guitars



@app.route('/', methods=('GET', 'POST'))
def index():
    
    if request.method=='POST':
        name = request.form['name']
        isElectric = isElectric = bool(request.form('isElectric'))
        price = request.form['price']
        color = request.form['color']
        guitars.insert_one({'name': name, 'isElectric': isElectric, "price" : price, "color" : color})
        return redirect(url_for('index'))
    all_guitars = guitars.find()
    return render_template('index.html', guitars = all_guitars)

@app.route('/<id>/delete/', methods=['POST'])
def delete(id):
    guitars.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))


if __name__ == '__main__':

    app.run(debug=True)