import pickle
import streamlit as st

model = pickle.load(open("estimasi_mobil.sav", "rb"))
st.title("Estimasi Harga Mobil Bekas")

Year = st.number_input("Masukkan tahun mobil")
mileage = st.number_input("Masukkan kilometer mobil")
tax = st.number_input("Masukkan pajak mobil")
mpg = st.number_input("Masukkan konsumsi bahan bakar mobil")
engineSize = st.number_input("Masukkan ukuran mesin mobil")
predict = ''
if st.button('Estimasi Harga'):
    predict = model.predict([[Year, mileage, tax, mpg, engineSize]])
    st.write("Estimasi Harga mobil bekas dalam EUR : ", predict)
    st.write("Estimasi Harga mobil bekas dalam IDR : ", predict * 15000)





