"""Simple recommendation helpers for the Music Recommender Simulation."""

import csv
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class Song:
    """Store the song information used by the recommender."""

    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """Store a simple user preference profile."""

    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


def _normalize_text(value: Optional[str]) -> str:
    """Normalize text so simple comparisons are easier."""
    if value is None:
        return ""
    return value.strip().lower()


def _to_float(value: Optional[str]) -> Optional[float]:
    """Convert a CSV value to float when possible."""
    if value is None or value == "":
        return None
    return float(value)


def _song_to_dict(song: Song) -> Dict:
    """Convert a Song object into the dict format used by the functions."""
    return {
        "id": song.id,
        "title": song.title,
        "artist": song.artist,
        "genre": song.genre,
        "mood": song.mood,
        "energy": song.energy,
        "tempo_bpm": song.tempo_bpm,
        "valence": song.valence,
        "danceability": song.danceability,
        "acousticness": song.acousticness,
    }


def _user_to_prefs(user: UserProfile) -> Dict:
    """Convert a UserProfile object into the dict format used by the functions."""
    return {
        "genre": user.favorite_genre,
        "mood": user.favorite_mood,
        "energy": user.target_energy,
    }


class Recommender:
    """Small OOP wrapper around the scoring functions."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the highest scoring songs for one user."""
        user_prefs = _user_to_prefs(user)
        ranked_songs = []

        for song in self.songs:
            score, _ = score_song(user_prefs, _song_to_dict(song))
            ranked_songs.append((song, score))

        ranked_songs.sort(key=lambda item: item[1], reverse=True)
        return [song for song, _ in ranked_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a short explanation string for one song."""
        score, reasons = score_song(_user_to_prefs(user), _song_to_dict(song))

        if not reasons:
            return f"Score {score:.2f}: no strong matching features."

        return f"Score {score:.2f}: " + ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dictionaries."""
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            song = {}

            for key, value in row.items():
                song[key] = value.strip() if isinstance(value, str) else value

            if song.get("id"):
                song["id"] = int(song["id"])

            for field_name in (
                "energy",
                "tempo_bpm",
                "valence",
                "danceability",
                "acousticness",
            ):
                if field_name in song:
                    song[field_name] = _to_float(song.get(field_name))

            songs.append(song)

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song and explain the main reasons."""
    score = 0.0
    reasons = []

    # Experiment: lower genre weight and higher energy weight
    target_genre = _normalize_text(
        user_prefs.get("genre") or user_prefs.get("favorite_genre")
    )
    target_mood = _normalize_text(
        user_prefs.get("mood") or user_prefs.get("favorite_mood")
    )
    song_genre = _normalize_text(song.get("genre"))
    song_mood = _normalize_text(song.get("mood"))

    if target_genre and song_genre == target_genre:
        score += 1.0
        reasons.append("genre match (+1.0)")

    if target_mood and song_mood == target_mood:
        score += 1.0
        reasons.append("mood match (+1.0)")

    target_energy = user_prefs.get("energy")
    if target_energy is None:
        target_energy = user_prefs.get("target_energy")
    song_energy = song.get("energy")

    if target_energy is not None and song_energy is not None:
        energy_gap = abs(song_energy - target_energy)
        energy_score = max(0.0, 1.0 - energy_gap)
        energy_points = energy_score * 2.0

        if energy_points >= 0.1:
            score += energy_points
            reasons.append(f"energy close (+{energy_points:.2f})")

    target_tempo = user_prefs.get("tempo_bpm")
    if target_tempo is None:
        target_tempo = user_prefs.get("tempo")
    song_tempo = song.get("tempo_bpm")

    if target_tempo is not None and song_tempo is not None:
        tempo_gap = abs(song_tempo - target_tempo)
        tempo_score = max(0.0, 1.0 - (tempo_gap / 60.0)) * 0.5

        if tempo_score >= 0.05:
            score += tempo_score
            reasons.append(f"tempo close (+{tempo_score:.2f})")

    return round(score, 2), reasons

def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
) -> List[Tuple[Dict, float, List[str]]]:
    """Score every song, sort by score, and return the top matches."""
    ranked_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        ranked_songs.append((song, score, reasons))

    ranked_songs.sort(
        key=lambda item: (-item[1], item[0].get("title", ""))
    )
    return ranked_songs[:k]
