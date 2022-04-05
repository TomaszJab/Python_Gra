# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 14:26:20 2022

@author: Mr. Tomasz
"""
import numpy as np
import random
import pandas as pd

def wprowadzLiczbePunktowDlaKtorychGraMaSieSkonczyc():
   
    while True:
        liczbaPunktowDlaKtorychGraSieZakonczy = input("Wpisz liczbe punktow dla ktorych gra ma sie skonczyc\n")
        try:
            liczbaPunktowDlaKtorychGraSieZakonczy = int(liczbaPunktowDlaKtorychGraSieZakonczy)
            print("Wpisano:",liczbaPunktowDlaKtorychGraSieZakonczy)
        except:
            print("Podana wartosc nie jest liczba")
            continue
        if (liczbaPunktowDlaKtorychGraSieZakonczy<=0):
            print("Podana wartosc nie powinna być mniejsza rowna od zera")
        else:
            return liczbaPunktowDlaKtorychGraSieZakonczy;
        

def wprowadzRuchGracza():
    global ruchGracza;
    while True:
        ruchGracza = input("===Wybierz kamien, papier lub nozyce: ===\n")
        if(ruchGracza=='k' or ruchGracza=='p' or ruchGracza =='n'):
            if(ruchGracza =='k'):
                ruchGracza = "Kamien"
            elif (ruchGracza =='p'):
                ruchGracza = "Papier"
            else:
                ruchGracza = "Nozyce"
            break;
        else:
            print("Napisz litere k jesli chcesz użyć kamienia")
            print("p jesli chcesz użyć papieru \nn jesli chcesz użyć nozyc")
            
    return ruchGracza;

def losujRuchKomputera():
    return random.choice( ["Kamien", "Papier", "Nozyce"] )

def wypiszNaKonsoliWyboryGraczy(ruchGracza,ruchKomputera):
    print("Wybrano: {ruchGracza}".format(ruchGracza=ruchGracza))
    print("Komputer wybral: {ruchKomputera}".format(ruchKomputera=ruchKomputera))


def obliczPunkty(ruchGracza,ruchKomputera):
    global punktyGracza, punktyKomputera

    if(ruchGracza =='Kamien' and ruchKomputera =='Nozyce') or (ruchGracza =='Papier' and ruchKomputera =='Kamien') or(ruchGracza =='Nozyce' and ruchKomputera =='Papier'):
        punktyGracza +=1
        punktyKomputera -=1
    elif ruchGracza!=ruchKomputera:
        punktyGracza -=1
        punktyKomputera +=1
    print(f"Punkty gracza {punktyGracza}, \nPunkty komputera: {punktyKomputera}")

def przeprowadzUczenieMaszynowe():

    global ruchKomputera, ruchGracza,macierz
    
    while liczbaPunktowDlaKtorychGraSieZakonczy!= punktyGracza and liczbaPunktowDlaKtorychGraSieZakonczy!= punktyKomputera and  punktyGracza >=0:
        
        ruchGracza = wprowadzRuchGracza()
        ruchKomputera = przewidzRuchGracza()
        
        wypiszNaKonsoliWyboryGraczy(ruchGracza,ruchKomputera)
        obliczPunkty(ruchGracza,ruchKomputera)
        aktualizujLancuchMarkowa()
        
def aktualizujLancuchMarkowa():
    global poprzedniRuchKomputeraIGracza
    nowyRuchKomputeraIGracza=skrocNazwe(ruchKomputera)+"_"+skrocNazwe(ruchGracza)
    macierz[table.index(poprzedniRuchKomputeraIGracza)][table.index(nowyRuchKomputeraIGracza)]=macierz[table.index(poprzedniRuchKomputeraIGracza)][table.index(nowyRuchKomputeraIGracza)]+1
   
    print(poprzedniRuchKomputeraIGracza+" ->"+nowyRuchKomputeraIGracza)
    print(pd.DataFrame(macierz,index=table,columns=table))
    poprzedniRuchKomputeraIGracza = nowyRuchKomputeraIGracza
    
def sprawdzKtoWygral():
    print("Koniec gry")
    if (punktyGracza<0):
        print("Przykro mi, wygral komputer")
    else:
        print("Graturacje !! Wygrales")

def przewidzRuchGracza():
    global ruchKomputera, poprzedniRuchKomputeraIGracza
    poprzedniRuchKomputeraIGracza=skrocNazwe(ruchKomputera)+"_"+skrocNazwe(ruchGracza)

    przewidywanyRuchGracza = np.random.choice( table,p=np.divide(macierz[table.index(poprzedniRuchKomputeraIGracza)],sum(macierz[table.index(poprzedniRuchKomputeraIGracza)])) )
    przewidywanyRuchGracza = przewidywanyRuchGracza.split('_')[1]
    if (przewidywanyRuchGracza=='k'):
        ruchKomputera = "Papier"
    elif przewidywanyRuchGracza=='p':
        ruchKomputera = "Nozyce"
    else:
        ruchKomputera = "Kamien"
    return ruchKomputera

def skrocNazwe(nazwaRuchu):
    if(nazwaRuchu =='Kamien'):
        nazwaRuchu = "k"
    elif (nazwaRuchu =='Papier'):
        nazwaRuchu = "p"
    else:
        nazwaRuchu = "n"
    return nazwaRuchu

def wyswietlZasadyGry():
    print("===Gra kamien, papier, nozyce===")
    print("Gracz, który chce użyć kamienia musi wpisac na konsoli litere k,")
    print("papieru litere p")
    print("nozyc litere n")
    
#https://machinelearningmastery.com/how-to-save-a-numpy-array-to-file-for-machine-learning/
def odczytModeluZPliku():
    try:
        macierz = np.load('s20128_markov_model.npy')
    except:
        macierz = np.ones((9, 9), dtype=np.int)
    #print(macierz)
    return macierz

def zapiszModeluDoPliku():
    data = np.asarray(macierz)
    # save to npy file
    np.save('s20128_markov_model.npy', data)

if __name__ == "__main__":
    macierz = odczytModeluZPliku()
    table = ["k_p", "k_n", "k_k","p_p", "p_n", "p_k","n_p", "n_n", "n_k"]
    punktyGracza = 0
    punktyKomputera = 0
    przewidywanyRuchGracza =""
    
    wyswietlZasadyGry()
    
    liczbaPunktowDlaKtorychGraSieZakonczy = wprowadzLiczbePunktowDlaKtorychGraMaSieSkonczyc()
    
    ruchKomputera = losujRuchKomputera()
    ruchGracza = wprowadzRuchGracza()
    
    wypiszNaKonsoliWyboryGraczy(ruchGracza,ruchKomputera)
    obliczPunkty(ruchGracza,ruchKomputera)
    
    przeprowadzUczenieMaszynowe()
    
    sprawdzKtoWygral()
    
    zapiszModeluDoPliku()











