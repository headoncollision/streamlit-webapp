import streamlit as st

st.title('Webapp to calculate largest of 3 numbers')

st.header('_Enter your inputs here:_ ')

number1 = st.number_input('Insert first number')
number2 = st.number_input('Insert second number')
number2 = st.number_input('Insert third number')

def maximum(n1,n2,n3):
  lis = [number1 , number2 , number3]
  a = max(lis)
  st.success(f"Maximum = {a}")

if st.button("Calculate result"):
    maximum(number1 , number2 , number3)

