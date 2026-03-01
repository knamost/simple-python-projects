"""
 Challenge:  Personal Movie Tracker with JSON

Create a Python CLI tool that lets users maintain their own personal movie database, like a mini IMDb.

Your program should:
1. Store all movie data in a `movies.json` file.
2. Each movie should have:
   - Title
   - Genre
   - Rating (out of 10)
3. Allow the user to:
   - Add a movie
   - View all movies
   - Search movies by title or genre
   - Exit the app

Bonus:
- Prevent duplicate titles from being added
- Format output in a clean table
- Use JSON for reading/writing structured data
"""

import os
import json

FILENAME = "movies.json"

# Load movies from JSON file
def load_movies():
   if not os.path.exists(FILENAME):
      return []
   with open(FILENAME, "r", encoding="utf-8") as file:
      return json.load(file)
   
# Save movies to JSON file
def save_movies(movies):
   with open(FILENAME, "w", encoding="utf-8") as file:
      json.dump(movies, file, indent=2)
      
# Add a movies
def add_movies(movies):
   title = input("Enter movie title: ").strip().lower()
   
   if any(movie["title"].lower() == title for movie in movies):
      print("Movie already exists")
      return
   
   genre = input("Genre: ").strip().lower()
   
   try:
      rating = float(input("Rating: "))
      if not (0 <= rating <= 10):
         raise ValueError
   except ValueError:
      print("Please enter valid number")
      return
   
   movies.append({
      "title":title, 
      "genre":genre, 
      "rating":rating
      })
   
   save_movies(movies)
   print("Movie added ✅")
   
# Search Movies
def search_movies(movies):
   term = input("Enter the title or genre: ").strip().lower()
   
   results = [
      movie for movie in movies
     if term in movie["title"].lower() or term in movie["genre"].lower()
   ]
   
   if not results:
      print("No matching result")
      return
   
   print(f"\nFound {len(results)} result(s)")
   
   for movie in results:
      print(f"{movie['title']} -- {movie['genre']} -- {movie['rating']}")
      

# View all Movies
def view_movies(movies):
   if not movies:
      print("No movies in Database")
      return
   
   print("-"*50)
   for movie in movies:
      print(f"{movie["title"]} -- {movie["genre"]} -- {movie["rating"]}")
   print("-"*50)

# Main Program Loop
def run_movie_db():
   movies = load_movies()
   
   while True:
      print("\n🍿 MyMoviesDB")
      print("1. Add Movie")
      print("2. View all Movies")
      print("3. Search Movie")
      print("4. Exit")
      
      choice = input("Choose an option (1-4): ").strip()
      
      match choice:
         case "1":
            add_movies(movies)
         case "2":
            view_movies(movies)
         case "3":
            search_movies(movies)
         case "4":
            print("Thanks for using MyMovieDB")
            break
         case _:
            print("Enter valid choice")
            
if __name__ == "__main__":
   run_movie_db()
   
   