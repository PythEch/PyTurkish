#!/usr/bin/env python
# -*- coding: cp1254 -*-
#
##################################################################
#
# Copyright (C) 2011-2014 PythEch
#
# This Source Code Form is subject to the terms of the Mozilla
# Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
##################################################################

# Private/Public simulasyonu i�in te�ekk�rler:
# http://en.literateprograms.org/Private_class_variables_%28Python%29?oldid=19190

from sys import version_info

__all__ = ['Ek', '__version__']
__version__ = '2.0'

# == Sabitler == #
# �ns�zler
SERT_UNSUZ = ('p', '�', 't', 'k', 's', '�', 'h', 'f')
YUMUSAMA = {'p': 'b', '�': 'c', 't': 'd', 'k': '�'}
BENZESME = {'c': '�', 'd': 't', 'g': 'k'}
# �nl�ler
UNLU = ('a', 'e', '�', 'i', 'u', '�', 'o', '�')
KALIN_UNLU = ('a', '�', 'u', 'o')
INCE_UNLU = ('e', 'i', '�', '�')
DUZ_UNLU = ('a', '�', 'e', 'i')
YUVARLAK_UNLU = ('o', 'u', '�', '�')

class Ek(object):
    def __init__(self, sozcuk, ozel_isim=False):
        if version_info[0] < 3 and isinstance(sozcuk, unicode):
            sozcuk = sozcuk.encode('cp1254', 'ignore')
        sozcuk = sozcuk.replace('�', 'i').replace('I', '�').lower()
        
        _sozcuk = sozcuk #isle() fonksiyonun g�rmesi i�in
        
        def __repr__(self):
            if not ozel_isim:
                return sozcuk
            else:
                return sozcuk[0].replace('i', '�').replace('�', 'I').upper() + sozcuk[1:]
        Ek.__repr__ = __repr__
        

        # == Analiz Fonksiyonlar� == #

        def unlu_sayisi(harfler):
            return len([x for x in harfler if x in UNLU])

        # ! Optimize edilebilir ! #
        def hecele():
            harf_sayisi=len(sozcuk)
            heceler=[]
            son_indeks=n=0
            while n < (harf_sayisi - 1):
                # 3 �ns�z yanyana
                if n+3 < harf_sayisi and unlu_sayisi(sozcuk[n:n+3]) == 0:
                    heceler.append(sozcuk[son_indeks:n+2])
                    son_indeks=n=n+2
                # 2 �nl� veya �ns�z yanyana
                elif n+2 < harf_sayisi and unlu_sayisi(sozcuk[n:n+2]) in (0,2):
                    heceler.append(sozcuk[son_indeks:n+1])
                    son_indeks=n=n+1
                # tek �ns�z
                elif not sozcuk[n] in UNLU and n != 0 and unlu_sayisi(sozcuk[n:]) != 0:
                    heceler.append(sozcuk[son_indeks:n])
                    son_indeks=n
                n+=1
            # son hece sanitasyonu
            if unlu_sayisi(sozcuk[-2:]) == 2: # 'video' gibi kelimeler i�in
                heceler.append(sozcuk[son_indeks:-1])
                heceler.append(sozcuk[-1])
            else:
                heceler.append(sozcuk[son_indeks:])
            return heceler
        self.hecele = hecele

        # == Ek Fonksiyonlar� == #

        #Durum (H�l) Ekleri
        def i():
            "Belirtme durum eki"
            return isle('i', 'y')
        self.i = i

        def e():
            u"Y�nelme durum eki"
            return isle('e', 'y')
        self.e = e

        def de():
            "Bulunma durum eki"
            return isle('de')
        self.de = de

        def den():
            u"Ayr�lma durum eki"
            return isle('den')
        self.den = den

        #�o�ul Eki
        def ler():
            u"�o�ul eki"
            return isle('ler')
        self.ler = ler

        #E�itlik eki
        def ce():
            u"E�itlik eki"
            return isle('ce')
        self.ce = ce

        #�yelik Ekleri
        def benim():
            u"1. tekil �ah�s iyelik eki"
            return isle('m', 'i')
        self.benim = benim

        def senin():
            u"2. tekil �ah�s iyelik eki"
            return isle('n', 'i')
        self.senin = senin

        def onun():
            u"3. tekil �ah�s iyelik eki"
            return isle('i', 's')
        self.onun = onun

        def bizim():
            u"1. �o�ul �ah�s iyelik eki"
            return isle('miz', 'i')
        self.bizim = bizim

        def sizin():
            u"2. �o�ul �ah�s iyelik eki"
            return isle('niz', 'i')
        self.sizin = sizin

        def onlarin():
            u"3. �o�ul �ah�s iyelik eki"
            return isle('leri')
        self.onlarin = onlarin

        #Tamlayan Eki
        def tamlayan():
            u"�lgi (tamlayan) eki"
            return isle('in', 'n')
        self.tamlayan = tamlayan

        #Tamlanan Eki (�yelik Eki)
        def tamlanan():
            u"Tamlanan eki, 3. tekil �ah�s iyelik ekiyle ayn�d�r"
            return onun()
        self.tamlanan = tamlanan
        
        def isle(ek, kaynastirma=''):
            sozcuk = _sozcuk

            try:
                son_unlu=next(x for x in reversed(sozcuk) if x in UNLU)
            except:
                raise ValueError("'%s' s�zc��� uygunsuz, hi� �nl� bulunamad�!" % sozcuk)

            #Kayna�t�rma �nl�s�
            if not (ek.startswith(UNLU) or sozcuk.endswith(UNLU)):
                ek = kaynastirma + ek

            #�ns�z Sertle�mesi (Benze�mesi)
            if sozcuk.endswith(SERT_UNSUZ) and ek[0] in BENZESME:
                ek = BENZESME[ek[0]] + ek[1:]

            #�ns�z Yumu�amas�
            if not ozel_isim and sozcuk[-1] in YUMUSAMA and sozcuk[-2] in UNLU \
                    and ek.startswith(UNLU) and unlu_sayisi(sozcuk) > 1: #and len(hecele()) > 1:
                sozcuk = sozcuk[:-1] + YUMUSAMA[sozcuk[-1]]

            #D�zl�k-Yuvarlakl�k (K���k �nl�) Uyumu
            if not son_unlu in DUZ_UNLU:
                ek = ek.replace('i', '�')

            #Kal�nl�k-�ncelik (B�y�k �nl�) Uyumu
            if not son_unlu in INCE_UNLU: #and not self.sozcuk in self._istisna['b�u']:
                for i, j in zip(INCE_UNLU, KALIN_UNLU):
                    ek = ek.replace(i, j)

            #Su, Ne s�zc�kleri istisnas�
            if sozcuk in ('su', 'ne'):
                kaynastirma = 'y'

            #Kayna�t�rma �ns�z�
            if sozcuk.endswith(UNLU) and ek.startswith(UNLU):
                ek = kaynastirma + ek

            #�zel �sim
            if ozel_isim and not "'" in sozcuk:
                ek = "'" + ek
            
            return Ek(sozcuk + ek, ozel_isim)


if __name__ == '__main__':
    import requests, re, random
    get=requests.get('http://www.birsozluk.com/')
    get.encoding='cp1254'
    s=re.search('</th></tr><tr><td align=center>(.*)</td></tr></table><br>', get.text).groups()[0]
    if version_info[0] < 3:
        s=s.encode('cp1254', 'ignore')
    s=re.findall(r'href="([^\'">]+)', s)
    for sozcuk in s:
        rand = random.randint(0,13)
        sozcuk = sozcuk.strip()
        if rand == 0:
            ekli='-'.join(Ek(sozcuk).hecele()), "hecele"
        elif rand == 1:
            ekli=Ek(sozcuk).i(), "i"
        elif rand == 2:
            ekli=Ek(sozcuk).e(), "e"
        elif rand == 3:
            ekli=Ek(sozcuk).de(), "de"
        elif rand == 4:
            ekli=Ek(sozcuk).den(), "den"
        elif rand == 5:
            ekli=Ek(sozcuk).ler(), "ler"
        elif rand == 6:
            ekli=Ek(sozcuk).ce(), "ce"
        elif rand == 7:
            ekli=Ek(sozcuk).benim(), "benim"
        elif rand == 8:
            ekli=Ek(sozcuk).senin(), "senin"
        elif rand == 9:
            ekli=Ek(sozcuk).onun(), "onun"
        elif rand == 10:
            ekli=Ek(sozcuk).bizim(), "bizim"
        elif rand == 11:
            ekli=Ek(sozcuk).sizin(), "sizin"
        elif rand == 12:
            ekli=Ek(sozcuk).onlarin(), "onlarin"
        else:
            ekli=Ek(sozcuk).tamlayan(), "tamlayan"
        print('%15s: %30s (%s)' % (sozcuk, ekli[0], ekli[1]))
