movies_count = int(input())

high_rating_movie = None
high_rating = float('-inf')
low_rating = float('inf')
low_rating_movie = None
total_rating = 0

for i in range(movies_count):
    movie_name = input()
    rating = float(input())
    total_rating += rating
    if rating < low_rating:
        low_rating = rating
        low_rating_movie = movie_name
    if rating > high_rating:
        high_rating = rating
        high_rating_movie = movie_name

print(f"{high_rating_movie} is with highest rating: {high_rating:.1f}")
print(f"{low_rating_movie} is with lowest rating: {low_rating:.1f}")
print(f"Average rating: {total_rating / movies_count:.1f}")

