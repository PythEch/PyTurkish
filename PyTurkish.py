#!/usr/bin/python
# -*- coding: cp1254 -*-

#S�r�m: 1.2

##################################################################
#
# Copyright (C) 2011-2013 PythEch
#
# This Source Code Form is subject to the terms of the Mozilla 
# Public License, v. 2.0. If a copy of the MPL was not distributed 
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
##################################################################

import string
class ek():
    """ek([String]S�zc�k, [Boolean]�zelIsim=False).fonksiyon() -> String
�ekim ekleri k�t�phanesi.

Kullan�m �ekli: ek("S�zc�k").den() veya ek("S�zc�k").cekim().den()
>>> "S�zc�kten"
�zel isimler i�in: ek("Ali",True).i()
>>> "Ali'yi"
"""
    sayilardaOtomatikOzelIsim=True #Say� girildi�inde otomatik olarak �zel isim kabul edilecek, �rn: 'ek("5").den() b�y�k say�lar' >>> 5'ten b�y�k say�lar 
    __sozcuk="" #K���k harflere �evirilmi� s�zc�k
    __asilSozcuk = "" #Orijinal s�zc�k
    __ek=""
    __kaynastirma="" # �nl�/�ns�z kayna�t�rma eki, __isle__() fonksiyonu otomatik karar verir
    __ozelIsim = False
    __sertler=('p', '�', 't', 'k', 's', '�', 'h', 'f')
    __yumusama={'p':'b','�':'c','t':'d','k':'�'}
    __benzesme={'c':'�','d':'t','g':'k'}
    __unluler={"t�m":('a','e','�','i','u','�','o','�'),
             "kal�n":('a','�','u','o'),
             "ince":('e','i','�','�'),
             "d�z":('a','�','e','i'),
             "yuvarlak":('o','u','�','�')}
    __sayilar={2: {'1':'on', '2':'yirmi', '3':'otuz', 
                      '4':'k�rk', '5':'elli', '6':'altm��',
                      '7':'yetmi�', '8':'seksen', '9':'doksan'},
               1: {'0':'s�f�r', '1':'bir', '2':'iki', '3':'��',
                       '4':'d�rt', '5':'be�', '6':'alt�', '7':'yedi', 
                       '8':'sekiz', '9':'dokuz'}}
    #Tamamlanacak
    _istisna={"k�k":{"�u":"�un", "bu":"bun", "o":"on"},#Ek ald�klar�nda k�k� de�i�en s�zc�kler
              "s�zc�k":{"bene":"bana", "sene":"sana"}, #Di�er istisnalar
              "�nl�":{"renk":"reng", "cenk":"ceng", "his":"hiss", "isim":"ism", "beyin":"beyn", "boyun":"boyn", "kar�n":"karn", "af":"aff",
                    "k�s�m":"k�sm", "nesil":"nesl", "burun":"burn", "zul�m":"zulm", "ak�l":"akl", "as�l":"asl" ,"as�r":"asr", "devir":"devr", 
                    "emir":"emr", "fikir":"fikr", "ilim":"ilm", "kay�t":"kayd", "ke�if":"ke�f", "keyif":"keyf", "nakil":"nakl", "nehir":"nehr",
                    "sab�r":"sabr", "seyir":"seyr", "�ehir":"�ehr", "�ekil":"�ekl", "zehir":"zehr", "zihin":"zihn", "zan":"zann","ba��r":"ba�r",
                    "a��z":"a�z", "al�n":"aln", "beniz":"benz", "b���r":"b��r", "geniz":"genz", "g���s":"g��s", "g�n�l":"g�nl", "o�ul":"o�l",
                    "resim":"resm", "kay�n":"kayn", "kay�p":"kayb", "nab�z":"nabz", "ret":"redd"}, #Sadece �nl� ek ald�klar�nda k�k� de�i�en s�zc�kler (�nl� d��mesi)
              #B�y�k �nl� uyumu istisnalar� #Cem Y�ld�z'a te�ekk�rler
              "b�u": ("kontrol", "bandrol", "banal", "alpul", "ametal", "anormal", "amiral"
                       , "sadakat", "santral", "�efkat", "usul", "normal", "oryantal", "hakikat"
                       , "hayal", "saat", "kemal", "gol", "kalp", "metal", "faul", "mineral", "alkol"
                       , "misal", "meal", "oramiral", "tu�amiral", "orjinal","orijinal", "koramiral", "general"
                       , "t�mgeneral", "tu�general", "korgeneral", "petrol", "liberal", "meral"
                       , "metropol", "ek�menapol", "lokal", "l�gat", "liyakat", "legal", "mentol"
                       , "be�amol", "me�gul", "me�ekkat", "oval", "mahsul", "makul", "mera�al"
                       , "metaryal", "nasihat", "radikal", "moral", "dikkat", "rol", "sinyal"
                       , "sosyal", "total", "�evval", "sual", "spesiyal", "tuval", "turnusol", "hol"
                       , "tropikal", "zeval", "zelal", "terminal", "termal", "resul", "sadakat", "resital"
                       , "refakat", "pastoral", "hal", "m�zikal", "m�zikhol", "menkul", "mahmul", "maktul"
                       , "kolestrol", "k�raat", "ziraaat", "kapital", "katedral", "kabul", "kanaat", "jurnal"
                       , "kefal", "idrak", "istiklal", "integral", "final", "ekol", "emsal", "enternasyonal"
                       , "nasyonal", "enstr�mantal", "harf", "cemal", "cemaat", "glikol", "karambol", "parabol"
                       , "kemal", "zulm", "nakl") #Turkish-Suffix-Library'den al�nm��t�r. (https://github.com/miklagard/Turkish-Suffix-Library)
    }

    def __repr__(self):
        return self.__sozcuk
    
    def __init__(self,Sozcuk,ozelIsim=False):
        self.__sozcuk = Sozcuk.replace("�","i").replace("I","�").lower() #Python T�rk�e bug-fix
        self.__asilSozcuk = Sozcuk
        self.__ozelIsim = ozelIsim

    #Analiz fonksiyonlar�
    def _sertMi(self):
        return (True if self.__sozcuk.endswith(self.__sertler) else False)

    def _sonUnlu(self):
        liste=['a',-1]
        for i in self.__unluler["t�m"]:
            ara=self.__sozcuk.rfind(i)
            if ara > liste[1]:
                liste[0]=i
                liste[1]=ara
        return liste[0]
    
    def _inceMi(self):
        return (True if self.__unluler["ince"].count(self._sonUnlu()) > 0 else False)

    def _duzMu(self):
        return (True if self.__unluler["d�z"].count(self._sonUnlu()) > 0 else False)

    #�nl� saymak hatalara neden olabilir#
    def _kacHeceli(self):
        n=0
        for i in self.__unluler["t�m"]:
            n+=self.__sozcuk.count(i)
        return n

    #�o�ul Eki    
    def ler(self):
        """�o�ul eki"""
        self.__ek="ler"
        return self.__isle__()
        
    #Durum (H�l) Ekleri
    def i(self):
        """Belirtme durum eki"""
        self.__ek="i"
        self.__kaynastirma="y"
        return self.__isle__()
        
    def e(self):
        """Y�nelme durum eki"""
        self.__ek="e"
        self.__kaynastirma="y"
        return self.__isle__()
        
    def de(self):
        """Bulunma durum eki"""
        self.__ek="de"
        return self.__isle__()

    def den(self):
        """Ayr�lma durum eki"""
        self.__ek="den"
        return self.__isle__()
    
    #�yelik Ekleri
    def benim(self):
        """�yelik eki (ben)"""
        self.__ek="m"
        self.__kaynastirma="i"
        return self.__isle__()
        
    def senin(self):
        """�yelik eki (sen)"""
        self.__ek="n"
        self.__kaynastirma="i"
        return self.__isle__()
    
    def onun(self):
        """�yelik eki (o)"""
        self.__ek="i"
        self.__kaynastirma="s"
        return self.__isle__()

    #Tamlayan Eki
    def nin(self):
        """�lgi eki (tamlayan)
    
�rnek: ek("Kap�").nin()+' '+ek("kol").i()"""
        self.__ek="in"
        self.__kaynastirma="n"
        return self.__isle__()

    #E�itlik eki
    def ce(self):
        """E�itlik eki"""
        self.__ek="ce"
        return self.__isle__()

    def __isle__(self):
        #�stisna 1
        if self.__sozcuk in self._istisna["k�k"]:
            self.__sozcuk = self._istisna["k�k"][self.__sozcuk]
        #Say�lar
        if self.__sozcuk.endswith(tuple(string.digits)):
            if self.sayilardaOtomatikOzelIsim:
                self.__ozelIsim=True
            sayi = ""
            # Say�y� yaln�z b�rak
            self.__sozcuk = self.__sozcuk.replace(",","").replace(".","")
            for i in range(1, self.__sozcuk.__len__()+1):
                if i == self.__sozcuk.__len__() or not self.__sozcuk[-i-1].isdigit():
                        sayi = self.__sozcuk[(-i):]
                        break
            # Say�n�n sonunda ka� tane s�f�r oldu�unu say
            sifir = 0
            for i in range(sayi.__len__()):
                if sayi[-i-1] != "0":
                    sifir = i
                    break
            if sifir >= 12:
                self.__sozcuk = 'trilyon'
                #10^12 den sonra basamaklar 'ilyon' ile bitti�i i�in ek getirirken farkl�l�k olu�turmuyor
            elif sifir >= 9:
                self.__sozcuk = 'milyar'
            elif sifir >= 6:
                self.__sozcuk = 'milyon'
            elif sifir >= 3:
                self.__sozcuk = 'bin'
            elif sifir == 2:
                self.__sozcuk = 'y�z'
            elif sifir == 1:
                self.__sozcuk = self.__sayilar[2][sayi[-2]]
            else:
                self.__sozcuk = self.__sayilar[1][sayi[-1]]
            asilSozcuk=self.__sozcuk
            ret=self.__isle__()
            return self.__asilSozcuk[:-(sayi.__len__())] + ret.replace(asilSozcuk, sayi)
        #�ns�z Sertle�mesi (Benze�mesi)
        if self._sertMi() and self.__ek.startswith(tuple(self.__benzesme.keys())):
            self.__ek=self.__benzesme[self.__ek[0]]+self.__ek[1:]
        #�ns�z Yumu�amas�
        if not self.__ozelIsim and self._kacHeceli() > 1 and self.__sozcuk.endswith(tuple(self.__yumusama.keys())) and self.__ek.startswith(self.__unluler["t�m"]):
                k=self.__yumusama[self.__sozcuk[-1]]
                if self.__sozcuk[-2] == 'n' and k=='�':
                    self.__sozcuk = self.__sozcuk[:-1]+'g'
                elif k!="�" or self.__sozcuk[-2] in self.__unluler["t�m"]:
                    self.__sozcuk = self.__sozcuk[:-1]+k
        #Kayna�t�rma �nl�s�
        if not self.__ek.startswith(self.__unluler["t�m"]) and not self.__sozcuk.endswith(self.__unluler["t�m"]):
            self.__ek=self.__kaynastirma+self.__ek
        #D�zl�k-Yuvarlakl�k (K���k �nl�) Uyumu
        if not self._duzMu():
            self.__ek=self.__ek.replace('i','�')
        #Kal�nl�k-�ncelik (B�y�k �nl�) Uyumu
        if not self._inceMi() and not self.__sozcuk in self._istisna["b�u"]:
            n=0
            for i in self.__unluler["ince"]:
                self.__ek=self.__ek.replace(i,self.__unluler["kal�n"][n])
                n+=1
        #Kayna�t�rma �ns�z�
        if ("su","ne").count(self.__sozcuk) > 0: #Su, Ne s�zc�kleri istisnas�
            self.__kaynastirma='y'
        if self.__sozcuk.endswith(self.__unluler["t�m"]) and self.__ek.startswith(self.__unluler["t�m"]):
                self.__ek=self.__kaynastirma+self.__ek
        if self.__ozelIsim:
            self.__ek="'"+self.__ek
        #�stisna 2
        if self.__sozcuk in self._istisna["�nl�"] and self.__ek.startswith(self.__unluler["t�m"]):
            self.__sozcuk = self._istisna["�nl�"][self.__sozcuk]
        self.__sozcuk += self.__ek
        #�stisna 3
        if self.__sozcuk in self._istisna["s�zc�k"]:
            self.__sozcuk = self._istisna["s�zc�k"][self.__sozcuk]
        #Return
        if self.__asilSozcuk.isupper():
            return self.__sozcuk.replace("i","�").replace("�","I").upper() #Python T�rk�e bug-fix
        elif self.__asilSozcuk.istitle():
            self.__sozcuk = self.__sozcuk[0].replace("i","�").replace("�","I") + self.__sozcuk[1:] #Python T�rk�e bug-fix
            return self.__sozcuk.title()
        else:
            return self.__sozcuk
