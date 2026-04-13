# Music Recommender Simulation

## Project Summary

This project is a small content-based music recommender written in Python. It loads songs from `data/songs.csv`, compares each song to a user preference profile, gives every song a score, and returns the top matches with human-readable reasons.

Real recommendation systems are usually much bigger than this. Apps like Spotify or YouTube often combine user history, behavior from many users, and content features. This project simulates just one simple part of that idea: matching song features to what a user says they want.

## What This Project Uses

The recommender looks at these song features:

- `genre`
- `mood`
- `energy`
- `tempo_bpm`

The current dataset has 10 songs with a small mix of genres and moods such as pop, lofi, rock, ambient, jazz, synthwave, happy, chill, intense, and focused.

## Algorithm Recipe

Each song starts at a score of `0`.

- Add `+2.0` if the genre matches the user's favorite genre
- Add `+1.0` if the mood matches the user's favorite mood
- Add up to `+1.0` for energy closeness using `1 - abs(song_energy - target_energy)`
- Add up to `+0.5` for tempo closeness using a simple 60 BPM gap formula if the profile includes a target tempo

After that, the program sorts all songs from highest score to lowest score and returns the top `k` songs.

Each recommendation also includes short reasons such as:

- `genre match (+2.0)`
- `mood match (+1.0)`
- `energy close (+0.92)`
- `tempo close (+0.44)`

## What This Project Simulates

This is a beginner-friendly simulation of a content-based recommender. It does not learn from listening history. Instead, it uses a transparent scoring rule that is easy to explain in class and easy to trace by hand.

## Biases and Limitations

- The catalog is very small, so the recommender can only choose from a few songs.
- It only uses a few features and ignores things like lyrics, vocals, language, and personal history.
- If a genre or mood is rare in the dataset, the system may not serve that taste very well.
- The hand-made scoring weights reflect my design choices, so they can favor some matches more than others.

## How to Run

Run the project from the repo root:

```bash
python -m src.main
```

Run the tests:

```bash
pytest
```

## Example Profiles

`src/main.py` includes three sample profiles:

- High-Energy Pop
- Chill Lofi
- Deep Intense Rock

These profiles make it easy to show different recommendation results in the terminal.

## Terminal Output Screenshots

These screenshots show example recommendations for multiple user profiles in the terminal.

Save the screenshot files in: `images/`

### High-Energy Pop

![High-Energy Pop Output](images/high-energy-pop.png)

### Chill Lofi

![Chill Lofi Output](images/chill-lofi.png)

### Deep Intense Rock

![Deep Intense Rock Output](images/deep-intense-rock.png)

### Test Results

![Pytest Output](images/pytest-results.png)

## Extra Documents

- [Model Card](model_card.md)
- [Reflection](reflection.md)
