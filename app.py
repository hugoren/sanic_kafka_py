from sanic import Sanic
from endpoint import bp_zk

app = Sanic(__name__)
app.blueprint(bp_zk)

if __name__ == '__main__':
    app.run(host='0.0.0.0', workers=3, port=10030, debug=True)