from flask import *
import json,time

app = Flask(__name__)

@app.route('/')
def home_page():
    data_set = {'Page':'Home','Message':'Successfully loaded the Home Page','Timestamp':time.time()}
    json_dump = json.dumps(data_set)
    print(json_dump)
    return json_dump
    #return jsonify({'Data Set:':data_set[0]})

if __name__ == '__main__':
    app.run()


