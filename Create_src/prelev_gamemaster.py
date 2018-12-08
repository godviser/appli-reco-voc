#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

import os
import json
import codecs
from types_relations import TYPES_FORCES, TYPES_WEAKNESSES


def find_forces(types):
	forces = []
	for type in types:
		forces += TYPES_FORCES[type]
	return list(set(forces))

def find_weaknesses(types):
	weaknesses = []
	for type in types:
		weaknesses += TYPES_WEAKNESSES[type]
	return list(set(weaknesses))


data={}
try:
    with open('gamemaster.json') as data_file:
        data = json.load(data_file)
except:
    pass

new_json = {}
new_json["pokemons"] = {}
new_json["moves"] = {}

print data["itemTemplates"][0]["templateId"][0: 2]

for element in data["itemTemplates"]:
    if element["templateId"][0: 2] == "V0":
                if element["templateId"][6: 13] == "POKEMON":
                        fiche_pkm = {}
                        fiche_pkm["id"] = element["templateId"][2: 5]
                        if "form" in element["pokemonSettings"].keys():
                            fiche_pkm["EN_name"] = element["pokemonSettings"]["form"]
                        else:
                            fiche_pkm["EN_name"] = element["pokemonSettings"]["pokemonId"]
                        fiche_pkm["types"] = [element["pokemonSettings"]["type"]]
                        if "type2" in element["pokemonSettings"].keys():
                                fiche_pkm["types"].append(element["pokemonSettings"]["type2"])
                        fiche_pkm["stamina"] = element["pokemonSettings"]["stats"]["baseStamina"]
                        fiche_pkm["attack"]  = element["pokemonSettings"]["stats"]["baseAttack"]
                        fiche_pkm["defense"] = element["pokemonSettings"]["stats"]["baseDefense"]
                        fiche_pkm["quickMoves"] = element["pokemonSettings"]["quickMoves"]
                        fiche_pkm["cinematicMoves"] = element["pokemonSettings"]["cinematicMoves"]                     
                        fiche_pkm["forces"] = find_forces(fiche_pkm["types"])
                        fiche_pkm["weaknesses"] = find_weaknesses(fiche_pkm["types"])

                        new_json["pokemons"][fiche_pkm["EN_name"]] = fiche_pkm
                        
                elif element["templateId"][6: 10] == "MOVE":
                        fiche_attack = {}
                        fiche_attack["id"] = element["templateId"][2: 5]
                        fiche_attack["EN_name"] = element["moveSettings"]["movementId"]
                        fiche_attack["type"] = element["moveSettings"]["pokemonType"]

                        new_json["moves"][fiche_attack["EN_name"]] = fiche_attack

print new_json["pokemons"]["001"]
with open('mygamemaster.json', 'w') as outfile:
    json.dump(new_json, outfile, sort_keys = True, indent = 4,
               ensure_ascii = False)
