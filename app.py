from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)
app.run(debug=True)

#read file
with open('cotacao.json','r') as myfile:
    data=myfile.read()

#parse file
obj = json.loads(data)

@app.route('/api/v1/cota',methods=['GET'])

def getTasks():
    return jsonify(obj)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")