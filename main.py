import numpy as np
import pickle5 as pickle
from bson import ObjectId
from flask_cors import CORS
from tensorflow import keras
from flask_pymongo import PyMongo
from tensorflow.keras.preprocessing.sequence import pad_sequences
from flask import Flask, jsonify, request, make_response, render_template

app = Flask(__name__)
CORS(app)

saved_model = keras.models.load_model('./my_model.h5')
with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

mongodb_client = PyMongo(app, uri="mongodb://ichlasul:Kelompok5@cluster0-shard-00-00.w9s2x.mongodb.net:27017,cluster0-shard-00-01.w9s2x.mongodb.net:27017,cluster0-shard-00-02.w9s2x.mongodb.net:27017/db_swac?ssl=true&replicaSet=atlas-14adoc-shard-0&authSource=admin&retryWrites=true&w=majority")
db = mongodb_client.db

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/laporan', methods=['GET', 'POST', 'DELETE'])
def laporan():
    if request.method == 'POST':
        
        # Definisi laporan
        laporan = {
            "nama_pelapor": request.json['name'],
            "jenis_pelapor": request.json['jenis_pelapor'],
            "lokasi":request.json['location'],
            "deskripsi_laporan": request.json['description'],
            "email": request.json['email'],
            "no_telphone": request.json['no_telp']
        }

        # Clasifi menggunakan model ml
        class_name = ['Seksual', 'Trafiking', 'Migran', 'Fisik', 'Psikis', 'Ekonomi']
        
        new_sentence = []
        new_sentence.append(request.json['description'])
        
        new_sequences = tokenizer.texts_to_sequences(new_sentence)
        new_padded = pad_sequences(new_sequences, maxlen=100, padding='post', truncating='post')

        res = saved_model.predict(new_padded)
        # print("Hasil Clasifikasi kasus  : {}".format(class_name[np.argmax(res)]))

        prediksi = res[0]
        index_class = np.argmax(prediksi[1:])
            
        laporan['penanganan_korban'] = class_name[index_class]
        if index_class == 0:
            laporan['penanganan_kasus'] = 'Penegak Hukum'
        elif index_class == 1:
            laporan['penanganan_kasus'] = 'Penegak Hukum'
        elif index_class == 2:
            laporan['penanganan_kasus'] = 'Penegak Hukum'
        elif index_class == 3:
            laporan['penanganan_kasus'] = 'Penegak Hukum'
        elif index_class == 4:
            laporan['penanganan_kasus'] = 'Rehabilitasi'
        elif index_class == 5:
            laporan['penanganan_kasus'] = 'Penegak Hukum'
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

        return jsonify({'message': 'Tindakan di process', 'data': response_data }), 201
    elif request.method == 'DELETE':
        if 'id' in request.args:
            id = request.args['id']
            db_response = db.laporan_swac.delete_one({'_id': ObjectId(id)})
            
            if db_response.deleted_count == 1:
                response = {'ok': True, 'message': 'record deleted'}
            else:
                response = {'ok': True, 'message': 'no record found'}
        else:
            return "Error: No id field provided. Please specify an id."
        return jsonify(response), 200
    else:

        if 'id' in request.args:
            id = request.args['id']
            data = db.laporan_swac.find_one({'_id': ObjectId(id)})
            data['_id'] = str(data['_id'])
            return jsonify(data), 200
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