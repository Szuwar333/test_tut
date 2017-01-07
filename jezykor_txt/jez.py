#! /usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os.path

@click.command()
@click.option('--plik_do_odczytu', help='Nazwa pliku z słowami', default="slowa.txt")
@click.option('--plik_do_zapisu', help='Nazwa pliku z słowami do zapisu', default="slowa_zapis.txt")



def main(plik_do_odczytu, plik_do_zapisu):
    click.echo("Słowa będa odczytywane  z : {0} ".format(plik_do_odczytu))
    click.echo("Słowa będa zapisywane do : {0} ".format(plik_do_zapisu))
    click.echo('Wprowadź słowo:')
    slownik = Slownik(plik_do_odczytu, plik_do_zapisu)
    sl = slownik.wczytaj_slownik()
    print("SLS ",sl)
    slownik.zapisz_slownik(sl)
    #print(sl)

class Slownik():
    def __init__(self, plik_odczyt, plik_zapis):
        self.plik_odczyt = plik_odczyt
        self.plik_zapis = plik_zapis


    def zapisz_slownik(self, lista_slow):
        print("zapisz ",lista_slow)
        f_plik = open(self.plik_zapis, "w")
        for slowo in lista_slow:
            linia = ""
            linia = "{0}:{1}".format(slowo, "|".join(lista_slow[slowo]) )
            print(linia)
            print(linia, end="\n", file=f_plik)
            f_plik.write(linia+"\n")


        f_plik.close()


      # # "sklejamy" znaczenia przecinkami w jeden napis
      #   znaczenia = ",".join(slownik[wobcy])
      #   # wyraz_obcy:znaczenie1,znaczenie2,...
      #   linia = ":".join([wobcy, znaczenia])
      #   print >>file1, linia  # zapisujemy w pliku kolejne linie
      #   file1.close()  # zamykamy plik

    def wczytaj_slownik(self):
        slownik={}
        if os.path.isfile( self.plik_odczyt ):  # czy istnieje plik słownika
            with open(self.plik_odczyt, "r") as f_plik:  # otwórz plik do odczytu
  
                for line in f_plik:  # przeglądamy kolejne linie

                    # rozbijamy linię na wyraz obcy i tłumaczenia
                    t = line.split(":")

                    slowo_pl = t[0]
                    slowa_ang = t[1].split("|")
                    slowa_ang[-1] = slowa_ang[-1].replace("\n", "")
                    slownik[slowo_pl]=slowa_ang

                    # # dodajemy do słownika wyrazy obce i ich znaczenia
                    # slownik[wobcy] = znaczenia
        else:
            komunikat = "Nie istnieje plik o nazwie : {0} ".format(self.plik_odczyt) 
            raise EnvironmentError(komunikat)
        return slownik  # zwracamy ilość elementów w słowniku



if __name__ == "__main__":
    main()