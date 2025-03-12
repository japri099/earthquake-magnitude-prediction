import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

from google.colab import files
uploaded = files.upload()

filename = list(uploaded.keys())[0]
data = pd.read_csv(filename)

print("\n5 data pertama:")
print(data.head())

print("\nInfo DataFrame:")
print(data.info())

drop_cols = ['remark', 'strike1', 'dip1', 'rake1']
data_clean = data.drop(columns=drop_cols, errors='ignore')

print("\nCek data kosong:")
print(data_clean.isnull().sum())

data_clean = data_clean.dropna()

X = data_clean[['lat', 'lon', 'depth']]
y = data_clean['mag']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

rf_model = RandomForestRegressor(
    n_estimators=100,  # Jumlah pohon
    random_state=42
)

rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nHasil Evaluasi Model:")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"R-squared (R2 Score): {r2:.4f}")

plt.figure(figsize=(8,6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel('Actual Magnitude')
plt.ylabel('Predicted Magnitude')
plt.title('Actual vs Predicted Magnitude (Random Forest)')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # Garis ideal
plt.grid()
plt.show()

contoh_data = pd.DataFrame({
    'lat': [-7.0],
    'lon': [110.0],
    'depth': [10]
})

prediksi_mag = rf_model.predict(contoh_data)
print("\nPrediksi Magnitude untuk lokasi baru:", prediksi_mag[0])
