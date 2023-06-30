import random
import itertools
from leet_mapping import L33T_MAPPING
from special_characters import COMMON_SPECIAL_CHARACTERS, ALL_SPECIAL_CHARACTERS

class PasswordGenerator:
    def __init__(self, words, date, options):
        self.words = words
        self.date = date
        self.options = options

    def generate_passwords(self):
        count = 0

        for length in range(len(self.words) + 1, len(self.words) + len(self.options) + 1):
            for combination in itertools.permutations([self.date] + self.options, length):
                password = ""

                for option in combination:
                    generated_option = OptionGenerator.generate_option(option)
                    if generated_option:
                        password += generated_option

                if password:
                    count += 1
                    print(password)

class OptionGenerator:
    @staticmethod
    def generate_option(option):
        if option == "minuscule":
            return LowercaseOptionGenerator.generate_option()
        elif option == "majuscule":
            return UppercaseOptionGenerator.generate_option()
        elif option == "premiere_majuscule":
            return FirstUppercaseOptionGenerator.generate_option()
        elif option == "sans_accents":
            return WithoutAccentsOptionGenerator.generate_option()
        elif option == "l33t":
            return LeetOptionGenerator.generate_option()
        elif option == "nombres_dates":
            return DateNumbersOptionGenerator.generate_option()
        elif option == "annee_2_chiffres":
            return TwoDigitYearOptionGenerator.generate_option()
        elif option == "annee_4_chiffres":
            return FourDigitYearOptionGenerator.generate_option()
        elif option == "caracteres_speciaux_communs":
            return CommonSpecialCharactersOptionGenerator.generate_option()
        elif option == "caracteres_speciaux_tous":
            return AllSpecialCharactersOptionGenerator.generate_option()
        else:
            return ""

class LowercaseOptionGenerator:
    @staticmethod
    def generate_option():
        return random.choice("abcdefghijklmnopqrstuvwxyz")

class UppercaseOptionGenerator:
    @staticmethod
    def generate_option():
        return random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

class FirstUppercaseOptionGenerator:
    @staticmethod
    def generate_option():
        return random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

class WithoutAccentsOptionGenerator:
    @staticmethod
    def generate_option():
        return random.choice("aeiou")

class LeetOptionGenerator:
    @staticmethod
    def generate_option():
        return random.choice(list(L33T_MAPPING.keys()))

class DateNumbersOptionGenerator:
    @staticmethod
    def generate_option():
        return random.choice("0123456789")

class TwoDigitYearOptionGenerator:
    @staticmethod
    def generate_option():
        return random.choice([str(i).zfill(2) for i in range(0, 100)])

class FourDigitYearOptionGenerator:
    @staticmethod
    def generate_option():
        return random.choice([str(i) for i in range(1900, 2100)])

class CommonSpecialCharactersOptionGenerator:
    @staticmethod
    def generate_option():
        return random.choice(COMMON_SPECIAL_CHARACTERS)

class AllSpecialCharactersOptionGenerator:
    @staticmethod
    def generate_option():
        return random.choice(ALL_SPECIAL_CHARACTERS)

class UserOptionGenerator:
    @staticmethod
    def get_user_options():
        print("Choisissez les options pour la génération des mots de passe :")
        options = []

        print("\nOptions pour les mots :")
        if input("Basculer toutes les lettres en minuscule ? (Oui/Non) ").lower() in ["oui", "o"]:
            options.append("minuscule")
        if input("Basculer toutes les lettres en majuscule ? (Oui/Non) ").lower() in ["oui", "o"]:
            options.append("majuscule")
        if input("Basculer la première lettre en majuscule ? (Oui/Non) ").lower() in ["oui", "o"]:
            options.append("premiere_majuscule")
        if input("Retirer les accents ? (Oui/Non) ").lower() in ["oui", "o"]:
            options.append("sans_accents")
        if input("Utiliser le L33T ? (Oui/Non) ").lower() in ["oui", "o"]:
            options.append("l33t")

        print("\nOptions pour la date :")
        if input("Utiliser les nombres de la date ? (Oui/Non) ").lower() in ["oui", "o"]:
            options.append("nombres_dates")
        if input("Utiliser l'année sur 2 chiffres ? (Oui/Non) ").lower() in ["oui", "o"]:
            options.append("annee_2_chiffres")
        if input("Utiliser l'année sur 4 chiffres ? (Oui/Non) ").lower() in ["oui", "o"]:
            options.append("annee_4_chiffres")

        print("\nOptions caractères spéciaux :")
        if input("Ajouter les caractères spéciaux les plus communs ? (Oui/Non) ").lower() in ["oui", "o"]:
            options.append("caracteres_speciaux_communs")
        if input("Ajouter tous les caractères spéciaux ? (Oui/Non) ").lower() in ["oui", "o"]:
            options.append("caracteres_speciaux_tous")

        return options
