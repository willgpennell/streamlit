import streamlit as sl
import pandas as pd
table=pd.DataFrame({"Column 1": [1,2,3,4,5,6,7], "Column 2": [11,12,13,14,15,16,17]})

sl.title('Hi! am I streamlit')
sl.subheader('Hi I am a subheader')
sl.header("This is a header")
sl.text('This is text')
sl.markdown('**Hello** *world*')
sl.markdown('# Hello world')
sl.markdown('---')
sl.markdown('[Google](https://www.google.com)')
sl.markdown('---')
sl.caption('Hi I am caption')

# latex works in this software aswell
sl.latex(r'\begin{pmatrix}a&b\\c&d\end{pmatrix}')
json = {"a":"1,2,3",
        "b":"4,5,6"}
sl.json(json)

code=""" 
print("Hello World!!")
    def function():
        return 0;
"""

sl.code(code, language="python")
sl.write("## H2")
sl.metric(label="Wind Speed", value="120ms⁻¹", delta="-1.4⁻¹")
sl.table(table)
sl.dataframe(table)