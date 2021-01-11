from flask import Flask, render_template, request
import hjson
import joblib

# initialize flask server
app = Flask(__name__, static_url_path='/static')
app.config["DEBUG"] = True

# read and parse the config.hjson file
config = hjson.loads(open('config.hjson', 'r').read())

# read the model
model = joblib.load(config['joblibFilePath'])

# on get request to root
@app.route('/', methods=['GET'])
def sendHomepage():
    return render_template('main.html', config=config)

# on post request to /predict
@app.route('/predict', methods=['POST'])
def predict():
    independents = []
    try:
        for i in range (1, len(config['input']) + 1 ):
            independents.append( float(request.form[str(i)]) )
    except KeyError as e:
        return render_template('error.html', errorText=str(e))
    except ValueError:
        return render_template('error.html', errorText='Invalid data in request')
    except Exception as e:
        return render_template('error.html', errorText='Internal error occured. '+str(e))
    try:
        predictValue = model.predict([independents])[0]
        return render_template('prediction.html', prediction=predictValue, config=config)
    except Exception as e:
        return render_template('error.html',
            errorText='There was a problem with the model predicting the values. ' + str(e))

if __name__ == '__main__':
    app.run()