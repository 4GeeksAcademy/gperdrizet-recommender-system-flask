'''Movie recommendation web app with Flask.'''

import pickle
from flask import Flask, request, render_template

# Load the assets
MODEL = pickle.load(open('models/model.pkl', 'rb'))
TFIDF_MATRIX = pickle.load(open('data/processed/tfidf_matrix.pkl', 'rb'))
ENCODED_DATA_DF = pickle.load(open('data/processed/encoded_features_df.pkl', 'rb'))

# Define the flask application
app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':

        input_movie = request.form['title']
        recommendations = get_movie_recommendations(
            input_movie,
            MODEL,
            TFIDF_MATRIX,
            ENCODED_DATA_DF
        )

        print(f'User input: {input_movie}')
        print(f'Result: {recommendations}')

    else:
        recommendations = None

    return render_template('index.html', recommendations = recommendations)


def get_movie_recommendations(movie_title, model, tfidf_matrix, encoded_data_df):
    '''Takes a movie title string, looks up TFIDF feature vector for that movie
    and returns title of top 5 most similar movies'''

    # Find the query movie in the encoded data, get the index
    try:
        movie_index = encoded_data_df[encoded_data_df['title'] == movie_title].index[0]

    except IndexError:
        return 'Movie not found'

    # Get the indexes of similar movies
    _, indices = model.kneighbors(tfidf_matrix[movie_index])

    # Extract the titles of the similar movie
    similar_movies = [encoded_data_df['title'][i] for i in indices[0]]
    
    return similar_movies[1:]