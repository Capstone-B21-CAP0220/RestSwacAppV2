from flask import Flask, jsonify, request, make_response
from flask_pymongo import PyMongo

app = Flask(__name__)


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
    return "<p>Hello, World! 2</p>"

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
        if not request.json or not 'email' in request.json:
            abort(400)

        # Definisi laporan
        laporan = {
            "nama_pelapor":"Rizki Sabyan",
            "jenis_pelapor":"Korban",
            "lokasi":"Bandung",
            "deskripsi_laporan":"Saya tidak tau harus cerita darimana. Tapi saya merasa diperjual belikan oleh teman saya. Saya memang bukan orang kaya. Tapi disitulah salahnya saya, demi mengikuti tren sekolah, saya mau saja ikut kebiasan teman saya yang kaya. Saya sering di ajak ke club dan ditawari minuman keras yang membuat saya mabuk. Bangun bangun, teman saya memberi saya sejumlah uang. Saya kaget tentang apa yang terjadi. Lama berteman dengan mereka, akhirnya saya sadar bahwa selama ini saya diperjual belikan oleh teman saya.",
            "jenis_kekerasan":"Trafiking",
            "penanganan_korban":"rehabilitas",
            "penanganan_kasus":"bantuan hukum",
            "email": request.json['email'],
            "no_telphone": 82362097321
        }

        # Clasifi menggunakan model ml
        

        # Add laporan to db
        db.laporan_swac.insert_one(laporan)


        return jsonify({'message': 'success'}), 201
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