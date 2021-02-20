#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
	if len(string)%2 == 0:
		return True
	return False



def get_num_char(string, char):
	for i in string:
		return string.count(char)


def get_first_part_of_name(name):
	nom_separe = name.split("-")
	premier_nom = nom_separe[0]
	return"Bonjour " + (premier_nom).capitalize()


def get_random_sentence(animals, adjectives, fruits):
	random_animal = random.choice(animals)
	random_adjective = random.choice(adjectives)
	random_fruits = random.choice(fruits)
	return "Aujourd'hui, j'ai vu un " + random_animal + " s'emparer d'un panier " + random_adjective + " plein de " + random_fruits


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))

