import streamlit as st
import re
st.markdown("<h1 style=text-align:center>KeyWord Density Checker</h1>",unsafe_allow_html=True)
st.markdown("---")
text=st.text_area("paragraph")
col1,col2,col3=st.columns(3)
word_dict=dict()
if text:
    col1.markdown("<h6 style=text-align:center>Keywords</h1>",unsafe_allow_html=True)
    col2.markdown("<h6 style=text-align:center>Values</h1>",unsafe_allow_html=True)
    col3.markdown("<h6 style=text-align:center>Desnsity</h1>",unsafe_allow_html=True)
    sim_text=re.sub("[:;'.,&#]","",text)
    words=sim_text.lower().split(" ")
    t_len=len(words)
    for word in words:
        if word in word_dict:
            word_dict[word]=word_dict[word]+1
        else:
            word_dict[word]=1
keys=list(word_dict.keys())
value=list(word_dict.values())
for i in range(len(keys)):
    col1.markdown(f"<h6 style=text-align:center>{keys[i]}</h1>",unsafe_allow_html=True)
    col2.markdown(f"<h6 style=text-align:center>{value[i]}</h1>",unsafe_allow_html=True)
    col3.markdown(f"<h6 style=text-align:center>{(value[i]/t_len)*100}%</h1>",unsafe_allow_html=True)
