import streamlit as sl

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

