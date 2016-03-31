from flask import Flask
from pynetgear import Netgear
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return json.dumps(Netgear().get_attached_devices())

if __name__ == '__main__':
    app.run()
