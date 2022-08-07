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

if __name__ == "__main__":
    library_of_movies_and_series = [
        Movie("Titanic", 1996, "catastrophic", 45000,),
        Movie("Avatar", 2004, "adventure", 10000),
        Series("Friends", 1990, "comedy", 10000, 1, 1),
        Series("Friends", 1990, "comedy", 10001, 2, 1),
        Series("Friends", 1990, "comedy", 10002, 3, 1),
        Series("Friends", 1990, "comedy", 10003, 4, 1),
        Series("The Simpsons", 2000, "animation", 20000, 1, 1),
        Series("The Simpsons", 2000, "animation", 30000, 1, 2),
        Series("The Simpsons", 2000, "animation", 40000, 2, 3),
        Series("The Simpsons", 2000, "animation", 50000, 2, 4),
    ]

    top_both = top_titles(library_of_movies_and_series, 2)
    top_movies = top_titles(library_of_movies_and_series, 2, "movies")
    top_series = top_titles(library_of_movies_and_series, 2, "series")

    print('1: TOP_BOTH-----------------------------')
    for m in top_both:
        print(f"{m} - number of paying: {m.number_of_playing}")
    
    print('2: TOP_MOVIES -----------------------------')
    for m in top_movies:
        print(f"{m} - number of paying: {m.number_of_playing}")
    
    print('3: TOP_SERIES-----------------------------')
    for m in top_series:
        print(f"{m} - number of paying: {m.number_of_playing}")

    print('4: SEARCH_TITANIC-----------------------------')

    titanic = search(library_of_movies_and_series,"Titanic")
    print(titanic.title)

    generate_views_times_10(library_of_movies_and_series)
    
    only_movies = get_movies(library_of_movies_and_series)
    only_series = get_series(library_of_movies_and_series)

    print('5: ONLY MOVIES WITH GENERATE VIEWS-----------------------------')

    for m in only_movies:
        print(f"{m} - number of paying: {m.number_of_playing}")

    print('5: ONLY SERIES WITH GENERATE VIEWS-----------------------------')
    for s in only_series:
        print(f"{s} - number of paying: {s.number_of_playing}")  