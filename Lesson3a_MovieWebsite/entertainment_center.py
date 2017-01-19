import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "http://vignette4.wikia.nocookie.net/jack-millers-webpage-of-disney/images/7/75/Toy_Story_DVD_cover.jpg",
                        "https://www.youtube.com/watch?v=ZXre34PxgTc")


avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                     "http://www.new-video.de/co/avatar09.jpg",
                     "https://www.youtube.com/watch?v=8TNlvM4cN6U")

lammbock = media.Movie("Lambock",
                        "Stefan and Kai have good going business, self-grown cannabis screened as pizza delivering service. For now they only have to deal with aphids.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BM2VhZjMwNDMtZmQ5Zi00YWVjLWJhZGItYzUwYThjYzk3OTM2L2ltYWdlXkEyXkFqcGdeQXVyMzA3Njg4MzY@._V1_SY1000_CR0,0,707,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=9aSjKzNzc8I")

school_of_rock = media.Movie("School of Rock", 
                        "Storyline",
                        "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", 
                        "Storyline",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", 
                        "Storyline",
                        "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=5nOF93SzX6s")

hunger_games = media.Movie("Hunger Games", 
                        "Storyline",
                        "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                        "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, lammbock, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
