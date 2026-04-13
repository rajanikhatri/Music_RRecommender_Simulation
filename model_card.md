# Model Card

## Model Name

Simple Vibe Match Recommender

## Goal / Task

The goal of this model is to recommend songs from a small CSV file based on a user's preferred genre, mood, energy level, and tempo. It is meant for classroom exploration, not for a real music product.

## Data Used

The system uses `data/songs.csv`, which currently has 10 songs. The file includes fields such as title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. The catalog has a small variety of genres and moods, but it is still too small to represent the full range of music taste.

## Algorithm Summary

This is a content-based recommender with simple hand-made scoring rules. It does not learn from user history. Instead, it compares each song to one user profile and gives points when the song looks like a good match.

Each song gets:

- `+2.0` for a genre match
- `+1.0` for a mood match
- up to `+1.0` for energy closeness
- up to `+0.5` for tempo closeness inside a simple 60 BPM gap window

The songs are then sorted from highest score to lowest score, and the top results are returned. The program also explains each recommendation with short reason strings.

## Observed Behavior / Biases

The recommender works best when the user's taste clearly matches the features in the dataset. It tends to reward exact genre and mood matches strongly, so songs in those categories often rise to the top. That can be useful, but it also means the system can be biased toward whatever genres and moods appear most clearly in the small dataset.

Because the catalog is tiny, some user tastes are not represented well. The system also ignores lyrics, artists the user already knows, cultural context, and changing taste over time. Another limitation is that the current profile only uses one favorite genre and one mood, so it cannot fully represent more mixed or complicated music taste.

## Evaluation Process

I evaluated the model by running three sample profiles in `src/main.py`:

- High-Energy Pop
- Chill Lofi
- Deep Intense Rock

I checked whether the top songs felt reasonable based on the score recipe. I also ran the starter tests to make sure the ranking logic and explanation behavior were working.

## Intended Use and Non-Intended Use

Intended use:

- a classroom assignment
- a simple demo of content-based recommendation
- a transparent example that is easy to explain

Non-intended use:

- real music streaming recommendations
- high-stakes decision making
- large-scale personalization for real users

## Ideas for Improvement

- Add more songs so the catalog has better coverage
- Support multiple favorite genres or moods instead of only one
- Add a diversity rule so the top results are not too similar
- Use more features, such as lyrics, release year, or user listening history
