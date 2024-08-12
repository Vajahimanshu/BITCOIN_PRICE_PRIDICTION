import pandas as pd # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.preprocessing import MinMaxScaler # type: ignore
from sklearn.ensemble import RandomForestRegressor # type: ignore
import joblib # type: ignore

def train_model():
    # Load and preprocess the data
    data = pd.read_csv('data.csv', parse_dates=['Date'])
    data = data[['Date', 'Open', 'High', 'Low', 'Close']]

    # Feature engineering
    data['Day'] = data['Date'].dt.day
    data['Month'] = data['Date'].dt.month
    data['Year'] = data['Date'].dt.year
    data = data[['Open', 'High', 'Low', 'Close', 'Day', 'Month', 'Year']]

    # Train/test split
    X = data[['Open', 'High', 'Low', 'Day', 'Month', 'Year']]
    y = data['Close']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scaling features
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Save the model and scaler
    joblib.dump(model, 'model.pkl')
    joblib.dump(scaler, 'scaler.pkl')

if __name__ == "__main__":
    train_model()
