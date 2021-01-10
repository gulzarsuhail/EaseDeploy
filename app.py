from flask import Flask, render_template
import hjson
import joblib

app = Flask(__name__, static_url_path='/static')
app.config["DEBUG"] = True

# read and parse the config.hjson file
config = hjson.loads(open('config.hjson', 'r').read())

# read the model
model = joblib.load(config['joblibFilePath'])

@app.route('/', methods=['GET'])
def sendHomepage():
    return render_template('index.html', config=config)

@app.route('/', methods=['POST'])
def predict():
    model = joblib.load(config['joblibFilePath'])

if __name__ == '__main__':
    app.run()