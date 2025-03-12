<h1>🌍 Earthquake Magnitude Prediction using Random Forest Regression</h1>

<p>Prediksi magnitudo gempa bumi berbasis lokasi (<strong>latitude</strong>, <strong>longitude</strong>) dan <strong>kedalaman (depth)</strong> menggunakan algoritma <strong>Random Forest Regression</strong>. Proyek ini membahas pemrosesan data gempa, pelatihan model machine learning, evaluasi performa, dan visualisasi hasil prediksi.</p>

<hr>

<h2>📂 Dataset</h2>
<p>Dataset digunakan berasal dari data gempa bumi yang berisi:</p>
<ul>
  <li>Latitude (<code>lat</code>)</li>
  <li>Longitude (<code>lon</code>)</li>
  <li>Depth (<code>depth</code>)</li>
  <li>Magnitude (<code>mag</code>)</li>
</ul>

<p><strong>Contoh format CSV:</strong></p>

<pre><code>lat,lon,depth,mag
-6.2,106.8,10,5.2
...
</code></pre>

<hr>

<h2>🚀 Fitur Utama</h2>
<ul>
  <li>✅ Preprocessing data: hapus kolom tidak relevan, cek missing values</li>
  <li>✅ Train-test split 80-20</li>
  <li>✅ Model Machine Learning: <strong>Random Forest Regressor</strong></li>
  <li>✅ Evaluasi akurasi model: <strong>MSE, RMSE, dan R² Score</strong></li>
  <li>✅ Visualisasi perbandingan Magnitudo aktual vs prediksi</li>
  <li>✅ Prediksi magnitudo baru berbasis input lokasi dan kedalaman</li>
</ul>

<hr>

<h2>🛠️ Tech Stack</h2>
<ul>
  <li>Python 3</li>
  <li>Pandas</li>
  <li>NumPy</li>
  <li>Scikit-learn</li>
  <li>Matplotlib</li>
  <li>Seaborn</li>
  <li>Google Colab (rekomendasi)</li>
</ul>

<hr>

<h2>⚙️ Cara Menggunakan</h2>

<h3>1. Clone atau Download Repo</h3>
<pre><code>git clone https://github.com/japri099/earthquake-magnitude-prediction.git
</code></pre>

<h3>2. Jalankan di Google Colab</h3>
<ul>
  <li>Upload file CSV dari local storage</li>
  <li>Sesuaikan nama file di kode berikut:</li>
</ul>

<pre><code>from google.colab import files
uploaded = files.upload()
filename = list(uploaded.keys())[0]
data = pd.read_csv(filename)
</code></pre>

<h3>3. Jalankan Pipeline</h3>
<ul>
  <li>Preprocessing</li>
  <li>Training Random Forest Regressor</li>
  <li>Evaluasi Model</li>
  <li>Visualisasi</li>
</ul>

<hr>

<h2>📊 Hasil Evaluasi Model (Contoh)</h2>
<table>
  <tr>
    <th>Metric</th>
    <th>Score</th>
  </tr>
  <tr>
    <td><strong>MSE</strong></td>
    <td>0.3310</td>
  </tr>
  <tr>
    <td><strong>RMSE</strong></td>
    <td>0.5754</td>
  </tr>
  <tr>
    <td><strong>R²</strong></td>
    <td>0.1768</td>
  </tr>
</table>

<h3>📈 Visualisasi Hasil</h3>
<p>Gambar: Plot perbandingan antara Magnitudo Aktual dan Prediksi</p>
<img src="https://github.com/japri099/earthquake-magnitude-prediction/blob/main/plot.png" alt="Actual vs Predicted Magnitude">

<hr>

<h2>🔮 Prediksi Data Baru</h2>
<p>Contoh prediksi untuk titik koordinat baru:</p>

<pre><code>contoh_data = pd.DataFrame({
    'lat': [-7.0],
    'lon': [110.0],
    'depth': [10]
})
prediksi_mag = rf_model.predict(contoh_data)
print("Prediksi Magnitude untuk lokasi baru:", prediksi_mag[0])
</code></pre>

<hr>

<h2>📌 Catatan</h2>
<ul>
  <li>Model menggunakan fitur minimal (<code>lat</code>, <code>lon</code>, <code>depth</code>), sehingga hasil prediksi bisa ditingkatkan dengan data tambahan seperti strike, dip, rake, atau informasi geologi lainnya.</li>
  <li>Preprocessing dapat disesuaikan dengan karakteristik dataset yang kamu miliki.</li>
</ul>

<hr>

<h2>📚 Referensi</h2>
<ul>
  <li><a href="https://scikit-learn.org/stable/" target="_blank">Scikit-learn Documentation</a></li>
  <li><a href="https://pandas.pydata.org/docs/" target="_blank">Pandas Documentation</a></li>
  <li><a href="https://www.kaggle.com/datasets/kekavigi/earthquakes-in-indonesia" target="_blank">BMKG Earthquake Dataset Kaggle</a></li>
</ul>

<hr>

<h2>🤝 Kontribusi</h2>
<p>Pull request sangat welcome! Jika ingin menambahkan algoritma lain, seperti Linear Regression, Decision Tree, atau model Deep Learning, silakan kontribusi!</p>

<hr>

<!-- <h2>🧑‍💻 Author</h2>
<p><strong>Marco Sihombing</strong><br>
Mahasiswa / Data Science Enthusiast<br>
📫 Reach me: <a href="#">LinkedIn</a> | <a href="#">Email</a></p>
-->
