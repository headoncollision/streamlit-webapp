import streamlit as st

st.title('Webapp to calculate largest of 3 numbers')

st.header('_Enter your inputs here:_ ')

number1 = st.number_input('Insert first number')
number2 = st.number_input('Insert second number')
number2 = st.number_input('Insert third number')

'''lis = [number1 , number2 , number3]

a = max(lis)'''

st.write('The largest number is ' , max(number1 , number2 , number3))
