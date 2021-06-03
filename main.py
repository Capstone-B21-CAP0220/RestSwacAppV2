import numpy as np
import pickle5 as pickle
from tensorflow import keras
from flask_pymongo import PyMongo
from tensorflow.keras.preprocessing.sequence import pad_sequences
from flask import Flask, jsonify, request, make_response, render_template

app = Flask(__name__)

saved_model = keras.models.load_model('./my_model.h5')
with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

mongodb_client = PyMongo(app, uri="mongodb://ichlasul:Kelompok5@cluster0-shard-00-00.w9s2x.mongodb.net:27017,cluster0-shard-00-01.w9s2x.mongodb.net:27017,cluster0-shard-00-02.w9s2x.mongodb.net:27017/db_swac?ssl=true&replicaSet=atlas-14adoc-shard-0&authSource=admin&retryWrites=true&w=majority")
db = mongodb_client.db

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return render_template('index.html')
    # return "<p>Hello, World! 2</p>"

@app.route('/books', methods=['GET'])
def getBook():
    return jsonify(books)

@app.route('/tasks', methods=['GET'])
def getTask():
    return jsonify({'tasks': tasks})

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/laporan', methods=['GET', 'POST'])
def laporan():
    if request.method == 'POST':
        if not request.json or not 'name' in request.json:
            abort(400)

        # Definisi laporan
        laporan = {
            "nama_pelapor": request.json['name'],
            "jenis_pelapor": request.json['jenis_pelapor'],
            "lokasi":request.json['location'],
            "deskripsi_laporan": request.json['description'],
            "jenis_kekerasan":"Dari Hasil ML",
            "email": request.json['email'],
            "no_telphone": request.json['no_telp']
        }

        laporan['penanganan_korban']
        laporan['penanganan_kasus']

        # Clasifi menggunakan model ml
        class_name = ['Seksual', 'Trafiking', 'Migran', 'Fisik', 'Psikis', 'Ekonomi']
        
        new_sentence = []
        new_sentence.append(request.json['description'])
        
        new_sequences = tokenizer.texts_to_sequences(new_sentence)
        new_padded = pad_sequences(new_sequences, maxlen=100, padding='post', truncating='post')

        res = saved_model.predict(new_padded)
        # print("Hasil Clasifikasi kasus  : {}".format(class_name[np.argmax(res)]))

        index_class = np.argmax(res)

        laporan['penanganan_korban'] = class_name[index_class]

        if index_class == 0:
            laporan['penanganan_kasus'] = ''
        elif index_class == 1:
            laporan['penanganan_kasus'] = ''
        elif index_class == 2:
            laporan['penanganan_kasus'] = ''
        elif index_class == 3:
            laporan['penanganan_kasus'] = ''
        elif index_class == 4:
            laporan['penanganan_kasus'] = ''
        elif index_class == 5:
            laporan['penanganan_kasus'] = ''
        else :
            laporan['penanganan_kasus'] = 'Tanyakan Pada Diri Sendiri'

        
        # Add laporan to db
        db.laporan_swac.insert_one(laporan)

        # Response : name, email, no telpon, jenis kekerasan , tindakan kasus
        response_data = {
            "name": request.json['name'],
            "email": request.json['name'],
            "no_telphone": request.json['name'],
            "jenis_kekerasan": class_name[index_class],
            "tindakan_kasus": laporan['penanganan_kasus']
        }

        return jsonify({'message': 'Tindakan di process', 'data': response_data  }), 201

    else:
        daftar_laporan = db.laporan_swac.find()

        data = []

        for elemen in daftar_laporan:
            elemen['_id'] = str(elemen['_id'])
            data.append(elemen)

        return jsonify({'message': 'OK', 'Laporan': [laporan for laporan in data] })

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)