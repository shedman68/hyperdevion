import numpy as np
import spacy
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_md")

def read_movie_descriptions(file_path):
    """Read movie descriptions from the file."""
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

def get_word_vectors(movie_descriptions):
    """Convert movie descriptions to word vector representations."""
    word_vectors = []
    for desc in movie_descriptions:
        doc = nlp(desc)
        vector = doc.vector
        word_vectors.append(vector)
    return np.array(word_vectors)

def recommend_movies(user_watched_description, movie_descriptions):
    """Recommend movies based on similarity to the user's watched description."""
    user_vector = nlp(user_watched_description).vector
    movie_vectors = get_word_vectors(movie_descriptions)
    similarity_scores = cosine_similarity([user_vector], movie_vectors)[0]

    # Get the index of the most similar movie
    most_similar_index = np.argmax(similarity_scores)
    recommended_movie = movie_descriptions[most_similar_index]

    # Explanation:
    # 1. read movie descriptions from the 'movies.txt' file.
    # 2. Convert each description into a dense word vector using spaCy's word embedding model.
    # 3. Calculate cosine similarity between the user's watched description and all other movie descriptions.
    # 4. The movie with the highest similarity score is recommended.

    # Breakdown of similarity scores:
    print("Similarity scores with all movies:")
    for i, score in enumerate(similarity_scores):
        print(f"Movie {i + 1}: Score = {score:.4f}")

    return recommended_movie

if __name__ == "__main__":
    movies_file = "movies.txt"
    user_watched = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

    all_movie_descriptions = read_movie_descriptions(movies_file)
    recommended_movie = recommend_movies(user_watched, all_movie_descriptions)

    print(f"Recommended movie based on similarity to 'Planet Hulk': {recommended_movie}")

