import pandas as pd
import numpy as np

from pickle import load
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Movie Recommendation System", page_icon="🎞️",layout="wide")
#st.title("Movie Recommendation System- Collaborative Based")
st.markdown(f'<h1 style="color:#ffffff;font-size:39px;background-color:#000000">{"Movie Recommendation System- Collaborative Based"}</h1>', unsafe_allow_html=True)
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-attachment: fixed;
             background-position: center;
             background-repeat:no-repeat;
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('backgroundj1.jpg') 
#image = Image.open('backgroundj1.jpg')
#st.image(image)

model_knn = load(open('Movie_R1/knn_model.pkl', 'rb'))

df = load(open('Movie_R1/collaborative_cosine_similarity.pkl', 'rb'))
df = pd.DataFrame(df)

#st.subheader('Top 5 Movies: ')
st.markdown(f'<h1 style="color:#ffffff;font-size:24px;background-color:#000000">{"Top 5 Movies: "}</h1>', unsafe_allow_html=True)
st.text("")
st.markdown(f'<h1 style="color:#ffffff;font-size:24px;background-color:#000000">{"Type or select a movie from the dropdown "}</h1>', unsafe_allow_html=True)
#movie_name = st.selectbox("Type or select a movie from the dropdown",df.index.values)
movie_name = st.selectbox(" ",
                              df.index.values)

if st.button('Show Recommendation'):
    distances, indices = model_knn.kneighbors(df.loc[movie_name,:].values.reshape(1, -1), n_neighbors = 11)
    for i in range(0, len(distances.flatten())):
        if i == 0:
            #st.text('Recommendations for ' + movie_name)
            st.markdown(f'<h1 style="color:#ffffff;font-size:20px;background-color:#000000">{"Recommendations for "}{movie_name}{" :"}</h1>', unsafe_allow_html=True)
            #st.markdown(f'<h1 style="color:#ffffff;font-size:20px;background-color:#000000">{movie_name}</h1>', unsafe_allow_html=True)
            #st.text(movie_name)
        else:
            #st.text('{0}: {1}'.format(i, df.index[indices.flatten()[i]]))
            st.markdown(f'<h1 style="color:#ffffff;font-size:20px;background-color:#000000">{i}{"  "}{df.index[indices.flatten()[i]]}</h1>', unsafe_allow_html=True)
            
