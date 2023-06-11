import flask

from model import anlysis





app = flask.Flask(__name__)


@app.route("/",methods=['POST'])
def hello():
    image=flask.request.files['image']
    image.save('static/'+image.filename)
    return anlysis('static/'+image.filename)

app.run()