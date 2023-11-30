import streamlit as st

st.title('Calculadora')

num1 = st.number_input('digite o primeiro numero: ')
num2 = st.number_input('digite o segundo numero: ')

soma = num1 + num2
subt = num1 - num2
mult = num1 * num2
divi = num1 / num2

if st.button('Calcular'):
    st.text(f'Resultado:\nsoma: {soma}\nsubt: {subt}\nmult: {mult}\ndivi: {divi}')