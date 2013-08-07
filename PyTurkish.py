#!/usr/bin/python
# -*- coding: cp1254 -*-

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
    """ek([String]Sözcük, [Boolean]ÖzelIsim=False).fonksiyon() -> String
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
    __sertler = ('p', 'ç', 't', 'k', 's', 'ş', 'h', 'f')
    __yumusama = {'p': 'b', 'ç': 'c', 't': 'd', 'k': 'ğ'}
    __benzesme = {'c': 'ç', 'd': 't', 'g': 'k'}
    __unluler = {'tüm': ('a', 'e', 'ı', 'i', 'u', 'ü', 'o', 'ö'),
                 'kalın': ('a', 'ı', 'u', 'o'),
                 'ince': ('e', 'i', 'ü', 'ö'),
                 'düz': ('a', 'ı', 'e', 'i'),
                 'yuvarlak': ('o', 'u', 'ö', 'ü')}
    __sayilar = {
        2: {'1': 'on', '2': 'yirmi', '3': 'otuz', '4': 'kırk', '5': 'elli', '6': 'altmış', '7': 'yetmiş', '8': 'seksen',
            '9': 'doksan'},
        1: {'0': 'sıfır', '1': 'bir', '2': 'iki', '3': 'üç', '4': 'dört', '5': 'beş', '6': 'altı', '7': 'yedi',
            '8': 'sekiz', '9': 'dokuz'}}
    # Tamamlanacak
    _istisna = {'kök': {'şu': 'şun', 'bu': 'bun', 'o': 'on'}, # Ek aldıklarında kökü değişen sözcükler
                'diğer': {'bene': 'bana', 'sene': 'sana'}, # Diğer istisnalar
                'ünlü': {
                    'renk': 'reng', 'cenk': 'ceng', 'his': 'hiss', 'isim': 'ism', 'beyin': 'beyn', 'boyun': 'boyn',
                    'karın': 'karn', 'af': 'aff', 'kısım': 'kısm', 'nesil': 'nesl', 'burun': 'burn',
                    'zulüm': 'zulm', 'akıl': 'akl', 'asıl': 'asl', 'asır': 'asr', 'devir': 'devr', 'emir': 'emr',
                    'fikir': 'fikr', 'ilim': 'ilm', 'kayıt': 'kayd', 'keşif': 'keşf', 'keyif': 'keyf',
                    'nakil': 'nakl', 'nehir': 'nehr', 'sabır': 'sabr', 'seyir': 'seyr', 'şehir': 'şehr',
                    'şekil': 'şekl', 'zehir': 'zehr', 'zihin': 'zihn', 'zan': 'zann', 'bağır': 'bağr',
                    'ağız': 'ağz', 'alın': 'aln', 'beniz': 'benz', 'böğür': 'böğr', 'geniz': 'genz',
                    'göğüs': 'göğs', 'gönül': 'gönl', 'oğul': 'oğl', 'resim': 'resm', 'kayın': 'kayn',
                    'kayıp': 'kayb', 'nabız': 'nabz', 'ret': 'redd', 'kalp': 'kalb'},
                # Sadece ünlü ek aldıklarında kökü değişen sözcükler (ünlü düşmesi)
                'büu': (
                    'kontrol', 'bandrol', 'banal', 'alpul', 'ametal', 'anormal', 'amiral', 'sadakat', 'santral',
                    'şefkat', 'usul', 'normal', 'oryantal', 'hakikat', 'hayal', 'saat', 'kemal', 'gol', 'kalb', 'metal',
                    'faul', 'mineral', 'alkol', 'misal', 'meal', 'oramiral', 'tuğamiral', 'orjinal', 'orijinal',
                    'koramiral', 'general', 'tümgeneral', 'tuğgeneral', 'korgeneral', 'petrol', 'liberal', 'meral',
                    'metropol', 'ekümenapol', 'lokal', 'lügat', 'liyakat', 'legal', 'mentol', 'beşamol', 'meşgul',
                    'meşekkat', 'oval', 'mahsul', 'makul', 'meraşal', 'metaryal', 'nasihat', 'radikal', 'moral',
                    'dikkat', 'rol', 'sinyal', 'sosyal', 'total', 'şevval', 'sual', 'spesiyal', 'tuval', 'turnusol',
                    'hol', 'tropikal', 'zeval', 'zelal', 'terminal', 'termal', 'resul', 'sadakat', 'resital', 'refakat',
                    'pastoral', 'hal', 'müzikal', 'müzikhol', 'menkul', 'mahmul', 'maktul', 'kolestrol', 'kıraat',
                    'ziraat', 'kapital', 'katedral', 'kabul', 'kanaat', 'jurnal', 'kefal', 'idrak', 'istiklal',
                    'integral', 'final', 'ekol', 'emsal', 'enternasyonal', 'nasyonal', 'enstrümantal', 'harf', 'cemal',
                    'cemaat', 'glikol', 'karambol', 'parabol', 'kemal', 'zulm', 'nakl')
                # Turkish-Suffix-Library'den alınmıştır. (https://github.com/miklagard/Turkish-Suffix-Library)
                # Büyük ünlü uyumu istisnaları #Cem Yıldız'a teşekkürler
    }

    def __repr__(self):
        return self.__sozcuk

    def __init__(self, Sozcuk, ozelIsim=False):
        self.__sozcuk = Sozcuk.replace('İ', 'i').replace('I', 'ı').lower()  # Python Türkçe bug-fix
        self.__asilSozcuk = Sozcuk
        self.__ozelIsim = ozelIsim

    #Analiz fonksiyonları
    def _sertMi(self):
        return (True if self.__sozcuk.endswith(self.__sertler) else False)

    def _sonUnlu(self):
        liste = ['a', -1]
        for i in self.__unluler['tüm']:
            ara = self.__sozcuk.rfind(i)
            if ara > liste[1]:
                liste[0] = i
                liste[1] = ara
        return liste[0]

    def _inceMi(self):
        return (True if self.__unluler['ince'].count(self._sonUnlu()) > 0 else False)

    def _duzMu(self):
        return (True if self.__unluler['düz'].count(self._sonUnlu()) > 0 else False)

    #Ünlü saymak hatalara neden olabilir#
    def _kacHeceli(self):
        return sum(self.__sozcuk.count(x) for x in self.__unluler['tüm'])

    #Çoğul Eki    
    def ler(self):
        """Çoğul eki"""
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
        """Yönelme durum eki"""
        self.__ek = 'e'
        self.__kaynastirma = 'y'
        return self.__isle__()

    def de(self):
        """Bulunma durum eki"""
        self.__ek = 'de'
        self.__kaynastirma = ''
        return self.__isle__()

    def den(self):
        """Ayrılma durum eki"""
        self.__ek = 'den'
        self.__kaynastirma = ''
        return self.__isle__()

    #İyelik Ekleri
    def benim(self):
        """1. tekil şahıs iyelik eki"""
        self.__ek = 'm'
        self.__kaynastirma = 'i'
        return self.__isle__()

    def senin(self):
        """2. tekil şahıs iyelik eki"""
        self.__ek = 'n'
        self.__kaynastirma = 'i'
        return self.__isle__()

    def onun(self):
        """3. tekil şahıs iyelik eki"""
        self.__ek = 'i'
        self.__kaynastirma = 's'
        return self.__isle__()

    def bizim(self):
        """1. çoğul şahıs iyelik eki"""
        self.benim()
        self.__ek = 'z'
        self.__kaynastirma = 'i'
        return self.__isle__()

    def sizin(self):
        """2. çoğul şahıs iyelik eki"""
        self.senin()
        self.__ek = 'z'
        self.__kaynastirma = 'i'
        return self.__isle__()

    def onlarin(self):
        """3. çoğul şahıs iyelik eki"""
        self.__ek = 'leri'
        self.__kaynastirma = ''
        return self.__isle__()

    #Tamlayan Eki
    def nin(self):
        """İlgi eki (tamlayan)
    
Örnek: ek('Kapı').nin()+' '+ek('kol').i()"""
        self.__ek = 'in'
        self.__kaynastirma = 'n'
        return self.__isle__()

    #Eşitlik eki
    def ce(self):
        """Eşitlik eki"""
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
        if self.__sozcuk in self._istisna['kök']:
            self.__sozcuk = self._istisna['kök'][self.__sozcuk]
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
                self.__sozcuk = 'yüz'
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
                and self.__ek.startswith(self.__unluler['tüm']) and self.__sozcuk[-2] in self.__unluler['tüm']:
            self.__sozcuk = self.__sozcuk[:-1] + self.__yumusama[self.__sozcuk[-1]]
        #Kaynaştırma Ünlüsü
        if not self.__ek.startswith(self.__unluler['tüm']) and not self.__sozcuk.endswith(self.__unluler['tüm']):
            self.__ek = self.__kaynastirma + self.__ek
        #Düzlük-Yuvarlaklık (Küçük Ünlü) Uyumu
        if not self._duzMu():
            self.__ek = self.__ek.replace('i', 'ü')
        #Kalınlık-İncelik (Büyük Ünlü) Uyumu
        if not self._inceMi() and not self.__sozcuk in self._istisna['büu']:
            for i, j in zip(self.__unluler['ince'], self.__unluler['kalın']):
                self.__ek = self.__ek.replace(i, j)
        #Su, Ne sözcükleri istisnası
        if ('su', 'ne').count(self.__sozcuk) > 0:
            self.__kaynastirma = 'y'
        #Kaynaştırma Ünsüzü
        if self.__sozcuk.endswith(self.__unluler['tüm']) and self.__ek.startswith(self.__unluler['tüm']):
            self.__ek = self.__kaynastirma + self.__ek
        #Özel İsim
        if self.__ozelIsim:
            self.__ek = "'" + self.__ek
        #Ünlü Düşmesi (İstisna)
        if self.__sozcuk in self._istisna['ünlü'] and self.__ek.startswith(self.__unluler['tüm']):
            self.__sozcuk = self._istisna['ünlü'][self.__sozcuk]
        self.__sozcuk += self.__ek
        #Diğer İstisnalar
        if self.__sozcuk in self._istisna['diğer']:
            self.__sozcuk = self._istisna['diğer'][self.__sozcuk]
        #Return
        if self.__asilSozcuk.isupper():
            return self.__sozcuk.replace('i', 'İ').replace('ı', 'I').upper()  # Python Türkçe bug-fix
        elif self.__asilSozcuk.istitle():
            self.__sozcuk = self.__sozcuk[0].replace('i', 'İ').replace('ı', 'I') + self.__sozcuk[1:]
            return self.__sozcuk.title()
        else:
            return self.__sozcuk
