#!/usr/bin/python
# -*- coding: utf-8 -*-

#Sürüm: 1.3

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
    u"""ek([String]Sözcük, [Boolean]ÖzelIsim=False).fonksiyon() -> String
Çekim ekleri kütüphanesi.

Kullanım şekli: ek('Sözcük').den()
>>> 'Sözcükten'
Özel isimler için: ek('Ali',True).i()
>>> "Ali'yi"
"""
    sayilardaOtomatikOzelIsim = True  # Sayı girildiğinde otomatik olarak özel isim kabul edilecek,
    # örn: 'ek('5').den() büyük sayılar' >>> 5'ten büyük sayılar
    __sozcuk = ''  # Küçük harflere çevirilmiş sözcük
    __asilSozcuk = ''  # Orijinal sözcük
    __ek = ''
    __kaynastirma = ''  # Ünlü/Ünsüz kaynaştırma eki, __isle__() fonksiyonu otomatik karar verir
    __ozelIsim = False
    __sertler = ('p', u'ç', 't', 'k', 's', u'ş', 'h', 'f')
    __yumusama = {'p': 'b', u'ç': 'c', 't': 'd', 'k': u'ğ'}
    __benzesme = {'c': u'ç', 'd': 't', 'g': 'k'}
    __unluler = {u'tüm': ('a', 'e', u'ı', 'i', 'u', u'ü', 'o', u'ö'),
                 u'kalın': ('a', u'ı', 'u', 'o'),
                 'ince': ('e', 'i', u'ü', u'ö'),
                 u'düz': ('a', u'ı', 'e', 'i'),
                 'yuvarlak': ('o', 'u', u'ö', u'ü')}
    __sayilar = {
        2: {'1': 'on', '2': 'yirmi', '3': 'otuz', '4': u'kırk', '5': 'elli', '6': u'altmış', '7': u'yetmiş', '8': 'seksen',
            '9': 'doksan'},
        1: {'0': u'sıfır', '1': 'bir', '2': 'iki', '3': u'üç', '4': u'dört', '5': u'beş', '6': u'altı', '7': 'yedi',
            '8': 'sekiz', '9': 'dokuz'}}
    # Tamamlanacak
    _istisna = {u'kök': {u'şu': u'şun', 'bu': 'bun', 'o': 'on'}, # Ek aldıklarında kökü değişen sözcükler
                u'diğer': {'bene': 'bana', 'sene': 'sana'}, # Diğer istisnalar
                u'ünlü': {
                    'renk': 'reng', 'cenk': 'ceng', 'his': 'hiss', 'isim': 'ism', 'beyin': 'beyn', 'boyun': 'boyn',
                    u'karın': 'karn', 'af': 'aff', u'kısım': u'kısm', 'nesil': 'nesl', 'burun': 'burn',
                    u'zulüm': 'zulm', u'akıl': 'akl', u'asıl': 'asl', u'asır': 'asr', 'devir': 'devr', 'emir': 'emr',
                    'fikir': 'fikr', 'ilim': 'ilm', u'kayıt': 'kayd', u'keşif': u'keşf', 'keyif': 'keyf',
                    'nakil': 'nakl', 'nehir': 'nehr', u'sabır': 'sabr', 'seyir': 'seyr', u'şehir': u'şehr',
                    u'şekil': u'şekl', 'zehir': 'zehr', 'zihin': 'zihn', 'zan': 'zann', u'bağır': u'bağr',
                    u'ağız': u'ağz', u'alın': 'aln', 'beniz': 'benz', u'böğür': u'böğr', 'geniz': 'genz',
                    u'göğüs': u'göğs', u'gönül': u'gönl', u'oğul': u'oğl', 'resim': 'resm', u'kayın': 'kayn',
                    u'kayıp': 'kayb', u'nabız': 'nabz', 'ret': 'redd', 'kalp': 'kalb'},
                # Sadece ünlü ek aldıklarında kökü değişen sözcükler (ünlü düşmesi)
                u'büu': (
                    'kontrol', 'bandrol', 'banal', 'alpul', 'ametal', 'anormal', 'amiral', 'sadakat', 'santral',
                    u'şefkat', 'usul', 'normal', 'oryantal', 'hakikat', 'hayal', 'saat', 'kemal', 'gol', 'kalb', 'metal',
                    'faul', 'mineral', 'alkol', 'misal', 'meal', 'oramiral', u'tuğamiral', 'orjinal', 'orijinal',
                    'koramiral', 'general', u'tümgeneral', u'tuğgeneral', 'korgeneral', 'petrol', 'liberal', 'meral',
                    'metropol', u'ekümenapol', 'lokal', u'lügat', 'liyakat', 'legal', 'mentol', u'beşamol', u'meşgul',
                    u'meşekkat', 'oval', 'mahsul', 'makul', u'meraşal', 'metaryal', 'nasihat', 'radikal', 'moral',
                    'dikkat', 'rol', 'sinyal', 'sosyal', 'total', u'şevval', 'sual', 'spesiyal', 'tuval', 'turnusol',
                    'hol', 'tropikal', 'zeval', 'zelal', 'terminal', 'termal', 'resul', 'sadakat', 'resital', 'refakat',
                    'pastoral', 'hal', u'müzikal', u'müzikhol', 'menkul', 'mahmul', 'maktul', 'kolestrol', u'kıraat',
                    'ziraat', 'kapital', 'katedral', 'kabul', 'kanaat', 'jurnal', 'kefal', 'idrak', 'istiklal',
                    'integral', 'final', 'ekol', 'emsal', 'enternasyonal', 'nasyonal', u'enstrümantal', 'harf', 'cemal',
                    'cemaat', 'glikol', 'karambol', 'parabol', 'kemal', 'zulm', 'nakl')
                # Turkish-Suffix-Library'den alınmıştır. (https://github.com/miklagard/Turkish-Suffix-Library)
                # Büyük ünlü uyumu istisnaları #Cem Yıldız'a teşekkürler
    }

    def __repr__(self):
        return self.__sozcuk

    def __init__(self, Sozcuk, ozelIsim=False):
        if type(Sozcuk) == str:
            Sozcuk = Sozcuk.decode('cp1254')
        self.__sozcuk = Sozcuk.replace(u'İ', 'i').replace('I', u'ı').lower()  # Python Türkçe bug-fix
        self.__asilSozcuk = Sozcuk
        self.__ozelIsim = ozelIsim

    #Analiz fonksiyonları
    def _sertMi(self):
        return (True if self.__sozcuk.endswith(self.__sertler) else False)

    def _sonUnlu(self):
        liste = ['a', -1]
        for i in self.__unluler[u'tüm']:
            ara = self.__sozcuk.rfind(i)
            if ara > liste[1]:
                liste[0] = i
                liste[1] = ara
        return liste[0]

    def _inceMi(self):
        return (True if self.__unluler['ince'].count(self._sonUnlu()) > 0 else False)

    def _duzMu(self):
        return (True if self.__unluler[u'düz'].count(self._sonUnlu()) > 0 else False)

    #Ünlü saymak hatalara neden olabilir#
    def _kacHeceli(self):
        return sum(self.__sozcuk.count(x) for x in self.__unluler[u'tüm'])

    #Çoğul Eki    
    def ler(self):
        u"""Çoğul eki"""
        self.__ek = 'ler'
        self.__kaynastirma = ''
        return self.__isle__()

    #Durum (Hâl) Ekleri
    def i(self):
        """Belirtme durum eki"""
        self.__ek = 'i'
        self.__kaynastirma = 'y'
        return self.__isle__()

    def e(self):
        u"""Yönelme durum eki"""
        self.__ek = 'e'
        self.__kaynastirma = 'y'
        return self.__isle__()

    def de(self):
        """Bulunma durum eki"""
        self.__ek = 'de'
        self.__kaynastirma = ''
        return self.__isle__()

    def den(self):
        u"""Ayrılma durum eki"""
        self.__ek = 'den'
        self.__kaynastirma = ''
        return self.__isle__()

    #İyelik Ekleri
    def benim(self):
        u"""1. tekil şahıs iyelik eki"""
        self.__ek = 'm'
        self.__kaynastirma = 'i'
        return self.__isle__()

    def senin(self):
        u"""2. tekil şahıs iyelik eki"""
        self.__ek = 'n'
        self.__kaynastirma = 'i'
        return self.__isle__()

    def onun(self):
        u"""3. tekil şahıs iyelik eki"""
        self.__ek = 'i'
        self.__kaynastirma = 's'
        return self.__isle__()

    def bizim(self):
        u"""1. çoğul şahıs iyelik eki"""
        self.benim()
        self.__ek = 'z'
        self.__kaynastirma = 'i'
        return self.__isle__()

    def sizin(self):
        u"""2. çoğul şahıs iyelik eki"""
        self.senin()
        self.__ek = 'z'
        self.__kaynastirma = 'i'
        return self.__isle__()

    def onlarin(self):
        u"""3. çoğul şahıs iyelik eki"""
        self.__ek = 'leri'
        self.__kaynastirma = ''
        return self.__isle__()

    #Tamlayan Eki
    def nin(self):
        u"""İlgi eki (tamlayan)
    
Örnek: ek('Kapı').nin()+' '+ek('kol').i()"""
        self.__ek = 'in'
        self.__kaynastirma = 'n'
        return self.__isle__()

    #Eşitlik eki
    def ce(self):
        u"""Eşitlik eki"""
        self.__ek = 'ce'
        self.__kaynastirma = ''
        return self.__isle__()

    #Özel ek
    def ozel(self,ek,kaynastirma=''):
        self.__ek = ek
        self.__kaynastirma = kaynastirma
        return self.__isle__()

    def __isle__(self):
        #Ek aldıklarında kökü değişen sözcükler
        if self.__sozcuk in self._istisna[u'kök']:
            self.__sozcuk = self._istisna[u'kök'][self.__sozcuk]
        #Sayılar
        if self.__sozcuk.endswith(tuple(string.digits)):
            if self.sayilardaOtomatikOzelIsim:
                self.__ozelIsim = True
            sayi = ''
            # Sayıyı yalnız bırak
            self.__sozcuk = self.__sozcuk.replace(',', '').replace('.', '')
            for i in range(1, self.__sozcuk.__len__() + 1):
                if i == self.__sozcuk.__len__() or not self.__sozcuk[-i - 1].isdigit():
                    sayi = self.__sozcuk[(-i):]
                    break
            # Sayının sonunda kaç tane sıfır olduğunu say
            sifir = 0
            for i in range(sayi.__len__()):
                if sayi[-i - 1] != '0':
                    sifir = i
                    break
            if sifir >= 12:
                self.__sozcuk = 'trilyon'
		# 10^12 den sonra basamaklar 'ilyon' ile bittiği için ek getirirken farklılık oluşturmuyor
            elif sifir >= 9:
                self.__sozcuk = 'milyar'
            elif sifir >= 6:
                self.__sozcuk = 'milyon'
            elif sifir >= 3:
                self.__sozcuk = 'bin'
            elif sifir == 2:
                self.__sozcuk = u'yüz'
            elif sifir == 1:
                self.__sozcuk = self.__sayilar[2][sayi[-2]]
            else:
                self.__sozcuk = self.__sayilar[1][sayi[-1]]
            asilSozcuk = self.__sozcuk
            ret = self.__isle__()
            return self.__asilSozcuk[:-(sayi.__len__())] + ret.replace(asilSozcuk, sayi)
        #Ünsüz Sertleşmesi (Benzeşmesi)
        if self._sertMi() and self.__ek.startswith(tuple(self.__benzesme.keys())):
            self.__ek = self.__benzesme[self.__ek[0]] + self.__ek[1:]
        #Ünsüz Yumuşaması
        if not self.__ozelIsim and self._kacHeceli() > 1 and self.__sozcuk.endswith(tuple(self.__yumusama.keys())) \
                and self.__ek.startswith(self.__unluler[u'tüm']) and self.__sozcuk[-2] in self.__unluler[u'tüm']:
            self.__sozcuk = self.__sozcuk[:-1] + self.__yumusama[self.__sozcuk[-1]]
        #Kaynaştırma Ünlüsü
        if not self.__ek.startswith(self.__unluler[u'tüm']) and not self.__sozcuk.endswith(self.__unluler[u'tüm']):
            self.__ek = self.__kaynastirma + self.__ek
        #Düzlük-Yuvarlaklık (Küçük Ünlü) Uyumu
        if not self._duzMu():
            self.__ek = self.__ek.replace('i', u'ü')
        #Kalınlık-İncelik (Büyük Ünlü) Uyumu
        if not self._inceMi() and not self.__sozcuk in self._istisna[u'büu']:
            for i, j in zip(self.__unluler['ince'], self.__unluler[u'kalın']):
                self.__ek = self.__ek.replace(i, j)
        #Su, Ne sözcükleri istisnası
        if ('su', 'ne').count(self.__sozcuk) > 0:
            self.__kaynastirma = 'y'
        #Kaynaştırma Ünsüzü
        if self.__sozcuk.endswith(self.__unluler[u'tüm']) and self.__ek.startswith(self.__unluler[u'tüm']):
            self.__ek = self.__kaynastirma + self.__ek
        #Özel İsim
        if self.__ozelIsim:
            self.__ek = "'" + self.__ek
        #Ünlü Düşmesi (İstisna)
        if self.__sozcuk in self._istisna[u'ünlü'] and self.__ek.startswith(self.__unluler[u'tüm']):
            self.__sozcuk = self._istisna[u'ünlü'][self.__sozcuk]
        self.__sozcuk += self.__ek
        #Diğer İstisnalar
        if self.__sozcuk in self._istisna[u'diğer']:
            self.__sozcuk = self._istisna[u'diğer'][self.__sozcuk]
        #Return
        if self.__asilSozcuk.isupper():
            return self.__sozcuk.replace('i', u'İ').replace(u'ı', 'I').upper()  # Python Türkçe bug-fix
        elif self.__asilSozcuk.istitle():
            self.__sozcuk = self.__sozcuk[0].replace('i', u'İ').replace(u'ı', 'I') + self.__sozcuk[1:]
            return self.__sozcuk.title()
        else:
            return self.__sozcuk
