from Guesser import PasswordGenerator, UserOptionGenerator

words = input("Entrez les mots (séparés par des espaces) : ").split()
date_format = "JJ-MM-AAAA"  # Format de date attendu
date = input(f"Entrez une date ({date_format}) : ")

options = UserOptionGenerator.get_user_options()

print("\nLes mots de passe générés :")
password_generator = PasswordGenerator(words, date, options)
password_generator.generate_passwords()
