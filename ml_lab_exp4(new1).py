import pickle
import streamlit as st
import pickle
pickle_in=open('Flower_data.pkl','rb')
model=pickle.load(pickle_in)

sepal_length=st.number_input('sepal length (cm)')
sepal_width=st.number_input('sepal width (cm)')
petal_length=st.number_input('petal length (cm)')
petal_width=st.number_input('petal width (cm)')
r=""
if st.button("PREDICT"):
  result=model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
  if result==0:
    st.success("Predicted Flower is SETOSA")
  elif result==1:
    st.success("Predicted Flower is VERSICOLOR")
  else:
    st.success("Predicted Flower is VERGINICA")
