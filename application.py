from flask import Flask, request, app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd


application = Flask(__name__)
app=application

model = pickle.load(open("model\\pipeline.pkl", "rb"))

## Route for homepage

@app.route('/')
def index():
    return render_template("index.html")

## Route for Single data point prediction
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    result = ""

    if request.method == 'POST':
        try:
            # Retrieve and convert form data
            data = {
                'radius_mean': float(request.form.get('radius_mean')),
                'texture_mean': float(request.form.get('texture_mean')),
                'perimeter_mean': float(request.form.get('perimeter_mean')),
                'area_mean': float(request.form.get('area_mean')),
                'smoothness_mean': float(request.form.get('smoothness_mean')),
                'compactness_mean': float(request.form.get('compactness_mean')),
                'concavity_mean': float(request.form.get('concavity_mean')),
                'concave points_mean': float(request.form.get('concave points_mean')),
                'symmetry_mean': float(request.form.get('symmetry_mean')),
                'fractal_dimension_mean': float(request.form.get('fractal_dimension_mean')),
                'radius_se': float(request.form.get('radius_se')),
                'texture_se': float(request.form.get('texture_se')),
                'perimeter_se': float(request.form.get('perimeter_se')),
                'area_se': float(request.form.get('area_se')),
                'smoothness_se': float(request.form.get('smoothness_se')),
                'compactness_se': float(request.form.get('compactness_se')),
                'concavity_se': float(request.form.get('concavity_se')),
                'concave points_se': float(request.form.get('concave points_se')),
                'symmetry_se': float(request.form.get('symmetry_se')),
                'fractal_dimension_se': float(request.form.get('fractal_dimension_se')),
                'radius_worst': float(request.form.get('radius_worst')),
                'texture_worst': float(request.form.get('texture_worst')),
                'perimeter_worst': float(request.form.get('perimeter_worst')),
                'area_worst': float(request.form.get('area_worst')),
                'smoothness_worst': float(request.form.get('smoothness_worst')),
                'compactness_worst': float(request.form.get('compactness_worst')),
                'concavity_worst': float(request.form.get('concavity_worst')),
                'concave points_worst': float(request.form.get('concave points_worst')),
                'symmetry_worst': float(request.form.get('symmetry_worst')),
                'fractal_dimension_worst': float(request.form.get('fractal_dimension_worst'))
            }

        
            df_new_data = pd.DataFrame([data])

            predict = model.predict(df_new_data)

            if predict[0] == 1:
                result = 'Cancer'
            else:
                result = 'Non-Cancer'

            return render_template('prediction.html', result=result)
        except Exception as e:
            print(f"Error: {e}")
            result = "Error in processing data."
            return render_template('prediction.html', result=result)
    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")