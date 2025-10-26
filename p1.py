print('jeller')
import streamlit as st
import pandas as pd
st.header('Hello, Streamlit!')
st.write('This is a simple Streamlit app.')
st.title('Streamlit Example')
st.subheader('DataFrame Example')
df = pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': ['A', 'B', 'C']
})
print(df)
st.dataframe(df)
st.line_chart(df['Column 1'])
st.bar_chart(df['Column 1'])
st.write('This is a simple line chart and bar chart.')