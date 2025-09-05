'''Simple command line utility to make movie recommendations
based on KNN with cosine similarity.'''

import os
import pickle
from pathlib import Path


def get_movie_recommendations(movie_title, model, tfidf_matrix, encoded_data_df):
    '''Takes a movie title string, looks up TFIDF feature vector for that movie
    and returns title of top 5 most similar movies'''

    # Find the query movie in the encoded data, get the index
    movie_index = encoded_data_df[encoded_data_df['title'] == movie_title].index[0]

    # Get the distances and indexes of similar movies
    distances, indices = model.kneighbors(tfidf_matrix[movie_index])

    # Extract the titles of the similar movie
    similar_movies = [(encoded_data_df['title'][i], distances[0][j]) for j, i in enumerate(indices[0])]
    
    return similar_movies[1:]


def set_project_root() -> None:
    '''Set the current working directory to project root.'''
    
    current_directory = Path.cwd()
    working_directory = current_directory.parent if current_directory.name == 'src' else current_directory

    print(f'Working directory: {working_directory}')

    return working_directory


if __name__ == '__main__':

    working_directory = set_project_root()

    # Load the assets
    model = pickle.load(open(f'{working_directory}/models/model.pkl', 'rb'))
    tfidf_matrix = pickle.load(open(f'{working_directory}/data/processed/tfidf_matrix.pkl', 'rb'))
    encoded_data_df = pickle.load(open(f'{working_directory}/data/processed/encoded_features_df.pkl', 'rb'))

    # Loop until user breaks
    while True:

        # Get a movie title from the user
        input_movie = input("Enter a movie title: ")

        # Get the recommendations
        recommendations = get_movie_recommendations(
            input_movie,
            model,
            tfidf_matrix,
            encoded_data_df
        )

        # Print the results
        print("Film recommendations '{}'".format(input_movie))
        
        for movie, distance in recommendations:
            print('- Film: {}'.format(movie))
