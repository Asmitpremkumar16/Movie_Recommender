import streamlit as st
import pickle
import gdown
import os
import requests


def fetch_posters(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=1b7c9bd68af2e3bb30fb791a10ff85c0&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['file_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


movies= pickle.load(open('movies.pkl','rb'))
file_id = "1-EHGBW_MGdvZFpQGsIcNvq4dXRVbcwxG"
file_path = "similarity.pkl"

# Download only if not already present
if not os.path.exists(file_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, file_path, quiet=False)

# Load the pickle file
similarity = pickle.load(open(file_path, "rb"))
movies_list= movies['title'].values


st.set_page_config(page_title="Movie Recommender", layout="wide")
st.header("Movie Recommender System")

selected_movie= st.selectbox('Select a movie',movies_list)


def recommend(selected_movie, n=5):
    if selected_movie not in movies['title'].values:
        print("Movie not found")
        return

    movie_index = movies[movies['title'] == selected_movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        enumerate(distances),
        key=lambda x: x[1],
        reverse=True
    )[1:n+1]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_posters(movie_id))

    return recommended_movies, recommended_posters


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
