#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import json

class Main:
    def __init__(self):
        self.STATEMODE = "state_info"

        # Init the mygamemaster
        try:
            with open('mygamemaster.json') as data_file:
                self.GAMEMASTER = json.load(data_file)
        except:
            pass

        # Init the french version
        try:
            with open('txt_french.json') as data_file:
                self.TRAD = json.load(data_file)
        except:
            pass

    def changeMode(self, mode):
        self.STATEMODE = mode
        return self.TRAD["sentences"]["state"] + self.TRAD["sentences"][mode]

    def sayListe(self, array):
        if len(array) == 1:
            return array[0]
        elif len(array) == 2:
            return " et ".join(array)
        else:
            last = array.pop()
            return ", ".join(array) + " et " + last

    def sayForces(self, pokemon_id):
        pokemon_types = self.GAMEMASTER["pokemons"][pokemon_id]["types"]
        trad_pokemon_types = []
        for pokemon_type in pokemon_types:
            trad_pokemon_types.append(self.TRAD["types"][pokemon_type])  
        forces = self.GAMEMASTER["pokemons"][pokemon_id]["forces"]
        trad_forces = []
        for force in forces:
            trad_forces.append(self.TRAD["types"][force])
        return self.TRAD["sentences"]["forces"].format(self.TRAD["pokemons"][pokemon_id], self.sayListe(trad_pokemon_types)) + self.sayListe(trad_forces)

    def sayWeaknesses(self, pokemon_id):
        weaknesses = self.GAMEMASTER["pokemons"][pokemon_id]["weaknesses"]
        trad_weaknesses = []
        for weakness in weaknesses:
            trad_weaknesses.append(self.TRAD["types"][weakness])
        return self.TRAD["sentences"]["weaknesses"].format(self.TRAD["pokemons"][pokemon_id]) + self.sayListe(trad_weaknesses)

    def advise(self, speech):
        if speech in self.TRAD["sentences"]["show_info"]:
                return self.changeMode("state_info")
        elif speech in self.TRAD["sentences"]["show_fight"]:
                return self.changeMode("state_fight")
        elif speech.capitalize() in self.TRAD["pokemons"].values():
                pokemon_id = self.TRAD["pokemons_reverse_id"][speech.capitalize()]
                print ("pokemon_id : " + pokemon_id)
                print self.STATEMODE
                if self.STATEMODE == "state_info":
                        return self.sayForces(pokemon_id)
                elif self.STATEMODE == "state_fight":
                        return self.sayWeaknesses(pokemon_id)
                else:
                    return "ERROR WITH STATE UNKNOWN"
        else:
            print "Nothing understood"


speech = "go"

main = Main()

while speech != "fin":
    speech = raw_input("Say something: ")
    print main.advise(speech)
