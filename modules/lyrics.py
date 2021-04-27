import lyricsgenius as lg
import os


def get_lyrics(name):
    key = os.getenv('GENIUS_API_KEY')
    genius = lg.Genius(str(key), skip_non_songs=True, excluded_terms=["(Live)"], remove_section_headers=False)
    song = (genius.search_song(name))
    s = song.lyrics
    if len(s) > 1990:
        i = 1990
        while s[i] != '\n':
            i -= 1
        s1 = s[:i]
        s2 = s[i:]
        if len(s) > 3900:
            j = 3900
            while s[j] != '\n':
                j -= 1
            s2 = s[i:j]
            s3 = s[j:]
            return s1, s2, s3
        return s1, s2
    return s
