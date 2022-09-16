import sqlite3


def get_movie_by_title(title):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""
            SELECT "title", "country", "release_year", "type", "description"
            FROM netflix
            WHERE "title" LIKE '{title}%'
            ORDER BY "release_year" DESC
            LIMIT 1"""
        )
        for line in cursor.fetchall():
            result = {
                "title": line[0],
                "country": line[1],
                "release_year": line[2],
                "genre": line[3],
                "description": line[4].strip(),
            }
            return result


def sort_movies_by_year(start_year, end_year):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""
            SELECT "title", "release_year"
            FROM netflix
            WHERE "release_year" BETWEEN '{start_year}' AND '{end_year}'
            LIMIT 100
            """
        )
    result = []
    for line in cursor.fetchall():
        result_line = {
            "title": line[0],
            "release_year": line[1],
        }
        result.append(result_line)
    return result


def sort_movies_by_rating(rating):
    if rating == 'family':
        rating_list = ['G', 'PG', 'PG-13']
    elif rating == 'adult':
        rating_list = ['R', 'NC-17']
    elif rating == 'children':
        rating_list = ['G']
    result = []
    for rating in rating_list:
        with sqlite3.connect("netflix.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""
                   SELECT "title", "description"
                   FROM netflix
                   WHERE "rating" LIKE '%{rating}%'
                   LIMIT 10
                   """
            )
        for line in cursor.fetchall():
            movie = {
                "title": line[0],
                "rating": f'{rating}',
                "description": line[1].strip(),
            }
            result.append(movie)
    return result


def sort_movies_by_genre(genre):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""
            SELECT "title", "description"
            FROM netflix
            WHERE "listed_in" LIKE '%{genre}%'
            ORDER BY "release_year" DESC
            LIMIT 10"""
        )
        result = []
        for line in cursor.fetchall():
            movie = {
                "title": line[0],
                "description": line[1].strip(),
            }
            result.append(movie)
        return result


def find_actors(actor_1, actor_2):
    casts = []
    result = []
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""
            SELECT "cast"
            FROM netflix
            WHERE "cast" LIKE '%{actor_1}%'
            OR "cast" LIKE '%{actor_2}%'
            """
        )
        for line in cursor.fetchall():
            line = list(''.join(line).split(', '))
            for name in line:
                casts.append(name)
    casts_dict = dict(
        (x, casts.count(x)) for x in casts if casts.count(x) > 2 and x not in [f'{actor_1}', f'{actor_2}']
    )
    for actor in casts_dict.keys():
        result.append(actor)
    print(result)


def sort_movies(movie_type, release_year, genre):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""
            SELECT "title", "description"
            FROM netflix
            WHERE "type" LIKE '%{movie_type}%'
            AND "release_year" == {release_year}
            AND "listed_in" LIKE '%{genre}%'
            """
        )
        result = []

        for line in cursor.fetchall():
            movie = {
                "title": line[0],
                "description": line[1].strip(),
            }
            result.append(movie)
        return result
