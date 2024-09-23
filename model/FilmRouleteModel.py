import requests


class FilmRouleteModel:
    # initilianze
    def __init__(self):
        pass

    def fetchFilm(self) -> dict:
        try:
            url: str = (
                "https://api.reelgood.com/v3.0/content/random?availability=onSources&content_kind=both&nocache=true&region=us&sources=netflix&spin_count=1"
            )

            # fetch
            request = requests.get(url)
            response = request.json()

            data: dict = {}
            title: str = response.get("title")
            rating: str = response.get("imdb_rating")
            description: str = response.get("overview")
            data["title"] = title
            data["rating"] = f"Rating: {rating}"
            data["description"] = description
            return data

        except Exception as e:
            # Handles the exception
            print(f"An error [getApiKey]: {e}")
