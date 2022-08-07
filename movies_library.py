import random
from re import T


class Movie:
    """
    Class responsible for representing movies
    """
    def __init__(self, title, year, genre, number_of_playing) -> None:
        self.title = title
        self.year = year
        self.genre = genre
        self.number_of_playing = number_of_playing

    def __str__(self) -> str:
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


def get_movies(m_s_list) -> list:
    """
    Returns only movies from given library
    Arguments:
    - m_s_list - list of movies and series
    """    
    res = []
    for l in m_s_list:
        if isinstance(l, Series):
            pass
        else:
            res.append(l)
    return res


def get_series(m_s_list) -> list:
    """
    Returns only series from given library
    Arguments:
    - m_s_list - list of movies and series
    """   
    res = []
    for l in m_s_list:
        if isinstance(l, Series):
            res.append(l)
    return res


def search(m_s_list, title):
    """
    Return movie or series with given title or None
    Arguments:
    - m_s_list - list of movies and series
    - title
    """
    found = False
    i = 0
    while not found:
        if m_s_list[i].title == title:
            found = True
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
    movie_or_series.number_of_playing = random.randint(1, 100)


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
    res = []
    list_to_process = []

    if content_type == "both":
        list_to_process = m_s_list
    elif content_type == "series":
        list_to_process = get_series(m_s_list)
    else:
        list_to_process = get_movies(m_s_list)

    by_popularity_desc = sorted(
        list_to_process,
        key=lambda movie_or_series: -1 * movie_or_series.number_of_playing,
    )
    for i in range(top_number):
        res.append(by_popularity_desc[i])
    return res

 