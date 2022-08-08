import random
import datetime


class Movie:
    """
    Class responsible for representing movies
    """

    def __init__(self, title, year, genre, number_of_playing) -> None:
        self.title = title
        self.year = year
        self.genre = genre
        self.number_of_playing = number_of_playing

    # def __str__(self) -> str:
    #     return f"{self.title} ({self.year})"

    def __repr__(self) -> str:
        return f"{self.title} ({self.year})"

    def play(self):
        self.number_of_playing += 1


class Series(Movie):
    """
    Class responsible for representing series
    """

    def __init__(
        self, title, year, genre, number_of_playing, series_number, season_number
    ) -> None:
        super().__init__(title, year, genre, number_of_playing)
        self.series_number = series_number
        self.season_number = season_number

    def __str__(self) -> str:
        return f"{self.title} S{self.season_number:02}E{self.series_number:02}"


def get_kind(m_s_list, content_type):
    """
    Returns only given kind of items from given library
    Arguments:
    - m_s_list - list of movies and series
    - content_type - movie/series
    """
    res = []
    for l in m_s_list:
        if type(l) == Movie and content_type == "movie":
            res.append(l)
        elif type(l) == Series and content_type == "series":
            res.append(l)
    return res


def get_movies(m_s_list) -> list:
    """
    Returns only movies from given library
    Arguments:
    - m_s_list - list of movies and series
    """
    return get_kind(m_s_list, content_type="movie")


def get_series(m_s_list) -> list:
    """
    Returns only series from given library
    Arguments:
    - m_s_list - list of movies and series
    """
    return get_kind(m_s_list, content_type="series")


def search(m_s_list, title):
    """
    Return movie or series with given title or None
    Arguments:
    - m_s_list - list of movies and series
    - title
    """
    for i in range(len(m_s_list)):
        if m_s_list[i].title == title:
            return m_s_list[i]
    return None


def generate_views(m_s_list):
    """
    Randomly assigns number of playing (1,100) to randomly
    chosen movie or series
    Arguments: 
    - m_s_list - list of movies and series
    """
    movie_index = random.randint(0, len(m_s_list) - 1)
    movie_or_series = m_s_list[movie_index]
    movie_or_series.number_of_playing += random.randint(1, 100)


def generate_views_times_10(m_s_list):
    """
    Randomly 10 times assigns number of playing (1,100) to randomly
    chosen movie or series
    Arguments: 
    - m_s_list - list of movies and series
    """
    for _ in range(10):
        generate_views(m_s_list)


def top_titles(m_s_list, top_number, content_type="both"):
    """
    Returns given number of the most popular movies and/or series
    Arguments: 
    - top_number - number of the most popular movies
    - content_type - both/series/movies
    - m_s_list - list of movies and series
    
    """

    list_to_process = []

    if content_type == "both":
        list_to_process = m_s_list
    elif content_type == "series":
        list_to_process = get_series(m_s_list)
    else:
        list_to_process = get_movies(m_s_list)

    by_popularity_desc = sorted(
        list_to_process,
        key=lambda movie_or_series: movie_or_series.number_of_playing,
        reverse=True,
    )

    return by_popularity_desc[:top_number]


if __name__ == "__main__":
    print("Biblioteka filmów.")
    library_of_movies_and_series = [
        Movie("Titanic", 1996, "catastrophic", 10),
        Movie("Avatar", 2004, "adventure", 10),
        Series("Friends", 1990, "comedy", 10, 1, 1),
        Series("Friends", 1990, "comedy", 10, 2, 1),
        Series("Friends", 1990, "comedy", 10, 3, 1),
        Series("Friends", 1990, "comedy", 10, 4, 1),
        Series("The Simpsons", 2000, "animation", 10, 1, 1),
        Series("The Simpsons", 2000, "animation", 10, 1, 2),
        Series("The Simpsons", 2000, "animation", 10, 2, 3),
        Series("The Simpsons", 2000, "animation", 10, 2, 4),
    ]

    generate_views_times_10(library_of_movies_and_series)

    print(f"Najpopularniejsze filmy i seriale dnia {datetime.datetime.now():%d.%m.%Y}:")

    top_ms = top_titles(library_of_movies_and_series, 3, "both")
    for ms in top_ms:
        print(f"{ms} - liczba odtworzeń: {ms.number_of_playing} ")
