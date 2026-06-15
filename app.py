import streamlit as st
import pickle
import gdown
import os
import requests

@st.cache_resource
def fetch_posters(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=320261176e294c7a530d6725cbeae04b&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

movies= pickle.load(open('movies.pkl','rb'))
file_id = "1-EHGBW_MGdvZFpQGsIcNvq4dXRVbcwxG"
file_path = "similarity.pkl"
if not os.path.exists(file_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, file_path, quiet=False)

@st.cache_resource
# Load the pickle file
similarity = pickle.load(open(file_path, "rb"))
movies_list= movies['title'].values

@st.cache_resource
def recommend(movie):
    if movie not in movies_list:
        print("Movie not found")
        return
        
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_posters(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters 
    
@st.cache_resource
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.header("Movie Recommender System")

selected_movie = st.selectbox("Type or select a movie from the dropdown", movies_list)

@st.cache_resource
if st.button('Show Recommendation'):
    movie_name, movie_poster= recommend(selected_movie) 
    col1, col2, col3, col4, col5 = st.columns(5)    
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])  
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])     
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])     
