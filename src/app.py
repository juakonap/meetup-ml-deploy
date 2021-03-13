import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True
#server = app.server

from flask_cors import CORS
CORS(app)

# main index page route
@app.route('/')
def home():
    return '<h1> La aplicación está funcionando!</h1>'


@app.route('/predict',methods=['POST'])
def predict():
    import pickle
    lgbm = pickle.load(open('hr_ds-lgbm-model.ml', 'rb'))
    target = lgbm.predict([[int(request.args['city']),
                            float(request.args['city_development_index']),
                            int(request.args['gender']),
                            int(request.args['relevent_experience']),
                            int(request.args['enrolled_university']),
                            int(request.args['education_level']),
                            int(request.args['major_discipline']),
                            int(request.args['experience']),
                            int(request.args['company_size']),
                            int(request.args['company_type']),
                            int(request.args['last_new_job']),
                            int(request.args['training_hours'])
                           ]])
    return str(round(target[0],3))

'''
if __name__ == "__main__":
    app.run(debug=True)
'''

#http://127.0.0.1:5000/predict?city=5&city_development_index=0.92&gender=1&relevent_experience=0&enrolled_university=3&education_level=3&major_discipline=1&experience=21&company_size=8&company_type=3&last_new_job=0&training_hours=36