"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

!Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

!Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

!Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""

import datetime


name = input("What's your name? ").strip().capitalize()   # removes extra spaces
age = input("How old are you? ").strip()
city = input("Which city do you live in? ").strip().capitalize()
profession = input("What is your profession? ").strip().capitalize()
fav_hobby = input("what's your favourite hobby? ").strip().capitalize()

intro_message = (
    f"Hello! my name is {name}, i'm {age} years old and live in {city}. "
    f"I work as a {profession} and i absolutely enjoy {fav_hobby} in my free time. "
    f"Nice to meet you!\n"
)

# getting date of current day (to put current login date)
current_date = datetime.date.today().isoformat()

intro_message += f"\n Logged On: {current_date}"

boarder = "*" * 80
final_output = f"{boarder}\n{intro_message}\n{boarder}"

print(final_output)
