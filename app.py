from user import User

user = User.load_from_file("Jovani.txt")

print(user.movies)