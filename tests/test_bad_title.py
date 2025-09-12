import src.movie_recommender as recommender


def test_title_error():
    '''Tests error handling when user submits a title that is not in
    the movies database'''

    # Call then recommendation function with an input for which we know the expected output
    similar_movies = recommender.get_movie_recommendations(
        'sdthtdhsftjdfhj',
        recommender.MODEL,
        recommender.TFIDF_MATRIX,
        recommender.TAG_TITLE_DF
    )

    # Check that we received the expected answer
    assert similar_movies == 'Movie not found'