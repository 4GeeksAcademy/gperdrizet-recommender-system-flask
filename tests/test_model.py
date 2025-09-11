import src.movie_recommender as recommender


def test_model_output():
    '''Tests to see if the model is giving sane output.'''

    # Call then recommendation function with an input for which we know the expected output
    similar_movies=recommender.get_movie_recommendations(
        'Star Wars',
        recommender.MODEL,
        recommender.TFIDF_MATRIX,
        recommender.TAG_TITLE_DF
    )

    # Check that we received the expected answer
    assert similar_movies[0] == 'The Empire Strikes Back'