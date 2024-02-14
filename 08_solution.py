def user(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}", end=", ")


user(name="Prantik", age=25, city="Kolkata")
user(name="Prantik", age=25)
