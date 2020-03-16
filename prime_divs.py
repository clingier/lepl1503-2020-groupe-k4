#!/usr/bin/env python3

"""Factorise la liste des diviseurs premiers de nombres entiers.

Ce script lit dans un fichier d'entrée une liste d'entiers (tous naturels plus grand ou égal à 2).
Pour chaque entier dans cette liste, il calcule la liste de ses diviseurs premiers.
Ensuite, il écrit dans un fichier de sortie une ligne pour chaque entier avec sa liste de diviseurs premiers.

Par exemple pour un fichier d'entrée :

	20414363521583006011
	13
	100

Le fichier de sortie sera :

	20414363521583006011 283 72135560146936417
	13
	100 2 5

Ce script s'utilise comme :
	$ python3 prime_divs.py input_filename output_filename
Pour plus d'information, lancez :
	$ python3 prime_divs.py -h

Pour tester le script, lancez :
	$ python3 -m pytest
Si vous avez une erreur, installez d'abord pytest :
	$ pip3 install -U pytest
"""


import argparse
import logging
import os
import sys

logger = logging.getLogger()


def is_div(number, i):
	"""Vérifie si i est un diviseur de number."""
	return number % i == 0

def is_prime(number):
	"""Vérifie si number est un nombre premier."""
	for i in range(2, number):
		if is_div(number, i):
			return False
	return True

def prime_divs(number):
	"""Calcule la liste des diviseurs premiers de number."""
	prime_dividers = []
	for i in range(2, number):
		if is_prime(i) and is_div(number, i):
			prime_dividers.append(i)
	return prime_dividers


def main(input, output):
	"""Lit chaque entier en entrée, trouve ses disviseurs premiers et écrit en sortie."""
	logger.info("Début de la boucle principale")
	for line in input:

		try:
			number = int(line)
		except ValueError:
			logger.warning("Entier mal formatté : %s", line[:-1])
			continue
		if number < 2:
			logger.warning("Entier plus petit que 2 : %s", line[:-1])
			continue

		prime_dividers = prime_divs(number)
		res = str(number) + " " + " ".join(str(div) for div in prime_dividers)

		output.write(res + "\n")
		logger.debug(res)


def parse_args(args=sys.argv[1:]):
	"""Analyse les arguments."""
	parser = argparse.ArgumentParser(description=sys.modules[__name__].__doc__,
	                                 formatter_class=argparse.RawDescriptionHelpFormatter)

	parser.add_argument("input_file", type=argparse.FileType('r'), help="Nom du fichier d'entrée")
	parser.add_argument("output_file", type=argparse.FileType('w'), help="Nom du fichier de sortie")

	group = parser.add_mutually_exclusive_group()
	group.add_argument("-v", "--verbose", default=False, action="store_true", help="Active les informations de débug")
	group.add_argument("-q", "--quiet", default=False, action="store_true", help="Désactive toutes les informations")

	arguments = parser.parse_args(args)

	logging.basicConfig(level=logging.INFO, stream=sys.stderr, format="%(levelname)s: %(message)s")
	if arguments.quiet:
		logger.setLevel(logging.WARNING)
	if arguments.verbose:
		logger.setLevel(logging.DEBUG)

	return arguments.input_file, arguments.output_file


if __name__ == '__main__':
	input_file, output_file = parse_args()
	logger.info("Fichiers ouverts")
	main(input_file, output_file)
	logger.info("Fermeture des fichiers")
	input_file.close()
	output_file.close()
