import streamlit as st
import joblib

st.title('House Price Prediction')

model = joblib.load('regression.joblib')
size = st.number_input('Enter the size of the house in square feet')
bedrooms = st.number_input('Enter the number of bedrooms')
garden = st.checkbox('Does the house have a garden?')
features = [size, bedrooms, garden]
price = model.predict([features])
if st.button('Predict price'):
    st.write(f'The price of the house is ${price[0]:,.2f}')