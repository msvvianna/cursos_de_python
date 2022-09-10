# variaveis
name = "ada lovelace"
print(name.title())  # coloca a primeira letra de cada palavra em maiuscula
print(name.lower())  # coloca as palavra em letra minuscula
print(name.upper())  # coloca as palavra em letra minuscula
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name  # concatena
message = "Hello, " + full_name.title() + "!\n\n"
print(message)

# espaços e tabulações
print("Languages:\n\t- Python\n\t- C\n\t- Java")

# removendo espaços em brancos
favorite_language = ' python '
print(favorite_language)
favorite_language = favorite_language.rstrip()  # ' python'
print(favorite_language)
favorite_language = favorite_language.lstrip()  # 'python '
print(favorite_language)
favorite_language = favorite_language.strip()  # 'python'
print(favorite_language)
