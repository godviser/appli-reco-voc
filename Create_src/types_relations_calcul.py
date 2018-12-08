#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

TYPES_FORCES = {
	'POKEMON_TYPE_ICE': ['POKEMON_TYPE_DRAGON', 'POKEMON_TYPE_FLYING', 'POKEMON_TYPE_GRASS', 'POKEMON_TYPE_GROUND'], 
	'POKEMON_TYPE_POISON': ['POKEMON_TYPE_GRASS', 'POKEMON_TYPE_FAIRY'], 
	'POKEMON_TYPE_DRAGON': ['POKEMON_TYPE_DRAGON'], 
	'POKEMON_TYPE_PSYCHIC': ['POKEMON_TYPE_FIGHTING', 'POKEMON_TYPE_POISON'], 
	'POKEMON_TYPE_ROCK': ['POKEMON_TYPE_FIRE', 'POKEMON_TYPE_ICE', 'POKEMON_TYPE_FLYING', 'POKEMON_TYPE_BUG'], 
	'POKEMON_TYPE_BUG': ['POKEMON_TYPE_GRASS', 'POKEMON_TYPE_PSYCHIC', 'POKEMON_TYPE_DARK'], 
	'POKEMON_TYPE_FIRE': ['POKEMON_TYPE_STEEL', 'POKEMON_TYPE_ICE', 'POKEMON_TYPE_BUG', 'POKEMON_TYPE_GRASS'], 
	'POKEMON_TYPE_GHOST': ['POKEMON_TYPE_PSYCHIC', 'POKEMON_TYPE_GHOST'], 
	'POKEMON_TYPE_NORMAL': [], 
	'POKEMON_TYPE_FAIRY': ['POKEMON_TYPE_FIGHTING', 'POKEMON_TYPE_DARK', 'POKEMON_TYPE_DRAGON'], 
	'POKEMON_TYPE_FLYING': ['POKEMON_TYPE_FIGHTING', 'POKEMON_TYPE_BUG', 'POKEMON_TYPE_GRASS'], 
	'POKEMON_TYPE_STEEL': ['POKEMON_TYPE_ICE', 'POKEMON_TYPE_FAIRY', 'POKEMON_TYPE_ROCK'], 
	'POKEMON_TYPE_ELECTRIC': ['POKEMON_TYPE_WATER', 'POKEMON_TYPE_FLYING'], 
	'POKEMON_TYPE_WATER': ['POKEMON_TYPE_GROUND', 'POKEMON_TYPE_ROCK', 'POKEMON_TYPE_FIRE'], 
	'POKEMON_TYPE_GROUND': ['POKEMON_TYPE_ROCK', 'POKEMON_TYPE_FIRE', 'POKEMON_TYPE_ELECTRIC', 'POKEMON_TYPE_STEEL', 'POKEMON_TYPE_POISON'], 
	'POKEMON_TYPE_FIGHTING': ['POKEMON_TYPE_NORMAL', 'POKEMON_TYPE_ICE', 'POKEMON_TYPE_STEEL', 'POKEMON_TYPE_ROCK', 'POKEMON_TYPE_DARK'], 
	'POKEMON_TYPE_GRASS': ['POKEMON_TYPE_WATER', 'POKEMON_TYPE_GROUND', 'POKEMON_TYPE_ROCK'], 
	'POKEMON_TYPE_DARK': ['POKEMON_TYPE_PSYCHIC', 'POKEMON_TYPE_GHOST']}
TYPES_WEAKNESSES = {
	'POKEMON_TYPE_ICE': ['POKEMON_TYPE_FIGHTING', 'POKEMON_TYPE_FIRE', 'POKEMON_TYPE_STEEL', 'POKEMON_TYPE_ROCK'], 
	'POKEMON_TYPE_POISON': ['POKEMON_TYPE_GROUND', 'POKEMON_TYPE_PSYCHIC'], 
	'POKEMON_TYPE_ROCK': ['POKEMON_TYPE_GROUND', 'POKEMON_TYPE_FIGHTING', 'POKEMON_TYPE_STEEL', 'POKEMON_TYPE_GRASS', 'POKEMON_TYPE_WATER'], 
	'POKEMON_TYPE_PSYCHIC': ['POKEMON_TYPE_DARK', 'POKEMON_TYPE_GHOST', 'POKEMON_TYPE_BUG'], 
	'POKEMON_TYPE_DRAGON': ['POKEMON_TYPE_FAIRY', 'POKEMON_TYPE_DRAGON', 'POKEMON_TYPE_ICE'], 
	'POKEMON_TYPE_BUG': ['POKEMON_TYPE_FLYING', 'POKEMON_TYPE_FIRE', 'POKEMON_TYPE_ROCK'], 
	'POKEMON_TYPE_FIRE': ['POKEMON_TYPE_GROUND', 'POKEMON_TYPE_ROCK', 'POKEMON_TYPE_WATER'], 
	'POKEMON_TYPE_GHOST': ['POKEMON_TYPE_DARK', 'POKEMON_TYPE_GHOST'], 
	'POKEMON_TYPE_NORMAL': ['POKEMON_TYPE_FIGHTING'], 
	'POKEMON_TYPE_FAIRY': ['POKEMON_TYPE_STEEL', 'POKEMON_TYPE_POISON'], 
	'POKEMON_TYPE_FLYING': ['POKEMON_TYPE_ELECTRIC', 'POKEMON_TYPE_ROCK', 'POKEMON_TYPE_ICE'], 
	'POKEMON_TYPE_STEEL': ['POKEMON_TYPE_GROUND', 'POKEMON_TYPE_FIGHTING', 'POKEMON_TYPE_FIRE'], 
	'POKEMON_TYPE_ELECTRIC': ['POKEMON_TYPE_GROUND'], 
	'POKEMON_TYPE_WATER': ['POKEMON_TYPE_ELECTRIC', 'POKEMON_TYPE_GRASS'], 
	'POKEMON_TYPE_GROUND': ['POKEMON_TYPE_GRASS', 'POKEMON_TYPE_ICE', 'POKEMON_TYPE_WATER'], 
	'POKEMON_TYPE_FIGHTING': ['POKEMON_TYPE_FAIRY', 'POKEMON_TYPE_FLYING', 'POKEMON_TYPE_PSYCHIC'], 
	'POKEMON_TYPE_GRASS': ['POKEMON_TYPE_FLYING', 'POKEMON_TYPE_FIRE', 'POKEMON_TYPE_POISON', 'POKEMON_TYPE_ICE', 'POKEMON_TYPE_BUG'], 
	'POKEMON_TYPE_DARK': ['POKEMON_TYPE_FAIRY', 'POKEMON_TYPE_FIGHTING', 'POKEMON_TYPE_BUG']}

	
TYPES_FORCES_FRENCH = {
	"plante": ["eau", "sol", "roche"],
	"roche": ["feu", "glace", "vol", "insecte"],
	"glace": ["dragon", "vol", "plante", "sol"],
	"dragon": ["dragon"],
	"tenebre": ["psy", "spectre"],
	"psy": ["combat", "poison"],
	"insecte": ["plante", "psy", "tenebre"],
	"vol": ["combat", "insecte", "plante"],
	"acier": ["glace", "fee", "roche"],
	"feu": ["acier", "glace", "insecte", "plante"],
	"combat": ["normal", "glace", "acier", "roche", "tenebre"],
	"sol": ["roche", "feu", "electrique", "acier", "poison"],
	"spectre": ["psy", "spectre"],
	"poison": ["plante", "fee"],
	"eau": ["sol", "roche", "feu"],
	"fee": ["combat", "tenebre", "dragon"],
	"electrique": ["eau", "vol"],
	"normal": []
}


TYPES_WEAKNESSES_FRENCH = {'spectre': ['tenebre', 'spectre'],
                    'roche': ['sol', 'combat', 'acier', 'plante', 'eau'],
                    'fee': ['acier', 'poison'],
                    'combat': ['fee', 'vol', 'psy'],
                    'normal': ['combat'],
                    'vol': ['electrique', 'roche', 'glace'],
                    'glace': ['combat', 'feu', 'acier', 'roche'],
                    'sol': ['plante', 'glace', 'eau'],
                    'poison': ['sol', 'psy'],
                    'acier': ['sol', 'combat', 'feu'],
                    'tenebre': ['fee', 'combat', 'insecte'],
                    'psy': ['tenebre', 'spectre', 'insecte'],
                    'feu': ['sol', 'roche', 'eau'],
                    'plante': ['vol', 'feu', 'poison', 'glace', 'insecte'],
                    'electrique': ['sol'],
                    'dragon': ['fee', 'dragon', 'glace'],
                    'eau': ['electrique', 'plante'],
                    'insecte': ['vol', 'feu', 'roche']
                    }

new_TYPES_WEAKNESSES_FRENCH = {}

for type_pkm, forces in TYPES_FORCES_FRENCH.iteritems():
	new_TYPES_WEAKNESSES_FRENCH[type_pkm] = []

for type_pkm, forces in TYPES_FORCES_FRENCH.iteritems():
	for force in forces:
		new_TYPES_WEAKNESSES_FRENCH[force].append(type_pkm)

print new_TYPES_WEAKNESSES_FRENCH



ID_TYPES = {
        "plante": "POKEMON_TYPE_GRASS",
	"roche": "POKEMON_TYPE_ROCK",
	"glace": "POKEMON_TYPE_ICE",
	"dragon": "POKEMON_TYPE_DRAGON",
	"tenebre": "POKEMON_TYPE_DARK",
	"psy": "POKEMON_TYPE_PSYCHIC",
	"insecte": "POKEMON_TYPE_BUG",
	"vol": "POKEMON_TYPE_FLYING",
	"acier": "POKEMON_TYPE_STEEL",
	"feu": "POKEMON_TYPE_FIRE",
	"combat": "POKEMON_TYPE_FIGHTING",
	"sol": "POKEMON_TYPE_GROUND",
	"spectre": "POKEMON_TYPE_GHOST",
	"poison": "POKEMON_TYPE_POISON",
	"eau": "POKEMON_TYPE_WATER",
	"fee": "POKEMON_TYPE_FAIRY",
	"electrique": "POKEMON_TYPE_ELECTRIC",
	"normal": "POKEMON_TYPE_NORMAL"
        }

def convert_in_POKEMON_TYPE(dico):
        new_dico = {}
        for type_pkm, forces in dico.iteritems():
                new_dico[ID_TYPES[type_pkm]] = []
                for force in forces:
                        new_dico[ID_TYPES[type_pkm]].append(ID_TYPES[force])
        return new_dico

print "TYPES_FORCES = "
print convert_in_POKEMON_TYPE(TYPES_FORCES_FRENCH)
print "TYPES_WEAKNESSES = "
print convert_in_POKEMON_TYPE(TYPES_WEAKNESSES_FRENCH)

	
