import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    for i in movie_list:
        movie_id = i[0]
        #fetch posters from api
        recommended_movie.append(movies.iloc[i[0]].title)

    return recommended_movie

movies = pickle.load(open("movies.pkl", "rb"))          # ✅ keep original DataFrame as "movies"
similarity = pickle.load(open("similarity.pkl", "rb"))

movies_list = movies['title'].values                     # ✅ separate variable just for the dropdown

st.title("Movie Recommendation System")
option = st.selectbox("Select an option", movies_list)

if st.button('recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)
