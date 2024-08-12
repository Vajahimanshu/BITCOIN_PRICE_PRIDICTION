
from flask import Flask, render_template, request, jsonify # type: ignore
import joblib # type: ignore

# Define the path to the template directory if it's custom
template_folder_path = 'E://download//elevate//BITCOIN PRICE PREDICTION//'

app = Flask(__name__, template_folder=template_folder_path)

# Load model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
\
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    open_price = data['Open']
    high_price = data['High']
    low_price = data['Low']
    day = data['Day']
    month = data['Month']
    year = data['Year']

    # Prepare input features
    features = [[open_price, high_price, low_price, day, month, year]]
    features_scaled = scaler.transform(features)

    # Predict the price
    prediction = model.predict(features_scaled)[0]
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(debug=True)
