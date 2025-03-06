import streamlit as st

# st.markdown('<h1 style="color: red; text-align: center; background-color:white; border: 2px solid red"> Welcome to my dashboard </h1>',
#              unsafe_allow_html=True)

st.markdown('<h1 style="color: maroon; background-color: white; text-align:center; margin:20px; border: 2px dashed yellow; font-family:sans serif">Welcome to my Dashboard</h1>', unsafe_allow_html=True)

image_url = "https://wallpaperboat.com/wp-content/uploads/2019/10/royalty-free-background-image-17.jpg"


st.markdown(f"<div style='text-align:center;'><img src='{image_url}'></div>", 
                    unsafe_allow_html=True)