from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("models/brain_tumor_rf.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    biomarkers = np.array(data['biomarkers']).reshape(1, -1)
    prediction = model.predict(biomarkers)
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)
