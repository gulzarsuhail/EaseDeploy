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
    return render_template('main.html', config=config)

@app.route('/', methods=['POST'])
def predict():
    return render_template('prediction.html', prediction=12345, config=config)

if __name__ == '__main__':
    app.run()