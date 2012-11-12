#!/usr/bin/python
# -*- coding: cp1254 -*-

# Sürüm 1.1

##################################################################
#
# Copyright (C) 2011-2012 PythEch
#
# This Source Code Form is subject to the terms of the Mozilla 
# Public License, v. 2.0. If a copy of the MPL was not distributed 
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
##################################################################

# bobince'e Teşekkürler: http://stackoverflow.com/a/722175/180343
import weakref, new
import string
class innerclass(object):
    """Descriptor for making inner classes.

    Adds a property 'owner' to the inner class, pointing to the outer
    owner instance.
    """

    # Use a weakref dict to memoise previous results so that
    # instance.Inner() always returns the same inner classobj.
    #
    def __init__(self, inner):
        self.inner= inner
        self.instances= weakref.WeakKeyDictionary()

    # Not thread-safe - consider adding a lock.
    #
    def __get__(self, instance, _):
        if instance is None:
            return self.inner
        if instance not in self.instances:
            self.instances[instance]= new.classobj(
                self.inner.__name__, (self.inner,), {'owner': instance}
            )
        return self.instances[instance]

class ek():
    __sozcuk=""
    __asilSozcuk = ""
    __ek=""
    __kaynastirma=""
    __ozelIsim = False
    __sertler=('p', 'ç', 't', 'k', 's', 'ş', 'h', 'f')
    __yumusama={'p':'b','ç':'c','t':'d','k':'ğ'}
    __benzesme={'c':'ç','d':'t','g':'k'}
    __unluler={"tüm":('a','e','ı','i','u','ü','o','ö'),
             "kalın":('a','ı','u','o'),
             "ince":('e','i','ü','ö'),
             "düz":('a','ı','e','i'),
             "yuvarlak":('o','u','ö','ü')}
    __sayilar={"on": {'1':'on', '2':'yirmi', '3':'otuz', 
                      '4':'kırk', '5':'elli', '6':'altmış',
                      '7':'yetmiş', '8':'seksen', '9':'doksan'},
               "bir": {'0':'sıfır', '1':'bir', '2':'iki', '3':'üç',
                       '4':'dört', '5':'beş', '6':'altı', '7':'yedi', 
                       '8':'sekiz', '9':'dokuz'}}
    #Tamamlanacak
    _istisna={"kök":{"şu":"şun", "bu":"bun", "o":"on"}, #Ek aldıklarında kökü değişen sozcukler
              "sozcük":{"bene":"bana", "sene":"sana"} #Diğer istisnalar
    }

    def __repr__(self):
        return self.__sozcuk
    
    def __init__(self,Sozcuk,ozelIsim=False):
        self.__sozcuk = Sozcuk.lower()
        self.__asilSozcuk = Sozcuk
        self.__ozelIsim = ozelIsim

    # 3 gereksiz fonksiyon, ileride belki kaldırırım
    def __saveCase(self):
        caseList=[]
        for i in self.__asilSozcuk:
            caseList.append(True if i.isupper() else False)
        return caseList

    def __loadCase(self, caseList):
        for n in range(len(caseList)):
            self.__asilSozcuk = self.__asilSozcuk[:n] + (self.__asilSozcuk[n].upper() if caseList[n] else self.__asilSozcuk[n].lower()) + self.__asilSozcuk[n+1:]
            
	# Case Insensitive Change, Case Insensitive'i çeviremediğimden 
	# dolayı yarı İngilizce yarı Türkçe yapmak istemedim
	# Makul bir karşılığı varsa lütfen bildirin
    def __ciChange(self,to):
        caseList = self.__saveCase()
        self.__asilSozcuk = to
        self.__loadCase(caseList)

    def _sertMi(self):
        if self.__sozcuk.endswith(self.__sertler):
            return True
        else:
            return False

    def _inceMi(self):
        liste=['a',-1]
        for i in self.__unluler["tüm"]:
            ara=self.__sozcuk.rfind(i)
            if ara > liste[1]:
                liste[0]=i
                liste[1]=ara
        if self.__unluler["ince"].count(liste[0]) > 0:
            return True
        else:
            return False

    def _duzMu(self):
        liste=['a',-1]
        for i in self.__unluler["tüm"]:
            ara=self.__sozcuk.rfind(i)
            if ara > liste[1]:
                liste[0]=i
                liste[1]=ara
        if self.__unluler["düz"].count(liste[0]) > 0:
            return True
        else:
            return False

    def _kacHeceli(self):
        n=0
        for i in self.__unluler["tüm"]:
            n+=self.__sozcuk.count(i)
        return n
    
    @innerclass
    class cekim():
        def de(self):
            return self.owner.de()
        def den(self):
            return self.owner.den()
        def ler(self):
            return self.owner.ler()
        def i(self):
            return self.owner.i()
        def nin(self):
            return self.owner.nin()
        def n(self):
            return self.owner.n()
        def e(self):
            return self.owner.e()
        def ce(self):
            return self.owner.ce()
        
    def de(self):
        self.__ek="de"
        return self.__isle__()

    def den(self):
        self.__ek="den"
        return self.__isle__()

    def ler(self):
        self.__ek="ler"
        return self.__isle__()

    def i(self):
        self.__ek="i"
        self.__kaynastirma="y"
        return self.__isle__()
    
    def nin(self):
        self.__ek="in"
        self.__kaynastirma="n"
        return self.__isle__()

    def n(self):
        if self._kacHeceli() <= 1:
            return self.nin()
        else:
            self.__ek="n"
            self.__kaynastirma="i"
        return self.__isle__()

    def senin(self):
        return self.n()

    def e(self):
        self.__ek="e"
        self.__kaynastirma="y"
        return self.__isle__()

    def ce(self):
        self.__ek="ce"
        return self.__isle__()

    def __isle__(self):
        #İstisna 1
        if self.__sozcuk in self._istisna["kök"]:
            self.__ciChange(self._istisna["kök"][self.__sozcuk])
            self.__sozcuk = self.__asilSozcuk.lower()
        #Sayılar
        if self.__sozcuk.endswith(tuple(string.digits)):
            sayi = ""
            # Sayıyı yalnız bırak
            self.__sozcuk = self.__sozcuk.replace(",","").replace(".","")
            for i in range(self.__sozcuk.__len__()):
                if not self.__sozcuk[-i].isdigit():
                        sayi = self.__sozcuk[(-i)+1:]
                        break
            # Sayının sonunda kaç tane sıfır olduğunu say
            sifir = 0
            for i in range(sayi.__len__()):
                if sayi[-i-1] != "0":
                    sifir = i
                    break
            if sifir >= 12:
                self.__sozcuk = 'trilyon'
                #10^12 den sonra basamaklar 'ilyon' ile bittiği için ek getirirken farklılık oluşturmuyor
            elif sifir >= 9:
                self.__sozcuk = 'milyar'
            elif sifir >= 6:
                self.__sozcuk = 'milyon'
            elif sifir >= 3:
                self.__sozcuk = 'bin'
            elif sifir == 2:
                self.__sozcuk = 'yüz'
            elif sifir == 1:
                self.__sozcuk = self.__sayilar["on"][sayi[-2]]
            else:
                self.__sozcuk = self.__sayilar["bir"][sayi[-1]]
        #Ünsüz Sertleşmesi (Benzeşmesi)
        if self._sertMi() and self.__ek.startswith(tuple(self.__benzesme.keys())):
            self.__ek=self.__benzesme[self.__ek[0]]+self.__ek[1:]
        #Ünsüz Yumuşaması
        if not self.__ozelIsim and self._kacHeceli() > 1 and self.__sozcuk.endswith(tuple(self.__yumusama.keys())) and self.__ek.startswith(self.__unluler["tüm"]):
                k=self.__yumusama[self.__sozcuk[-1]]
                if self.__sozcuk[-2] == 'n' and k=='ğ':
                    self.__ciChange(self.__sozcuk[:-1]+'g')
                elif k!="ğ" or self.__sozcuk[-2] in self.__unluler["tüm"]:
                    self.__ciChange(self.__sozcuk[:-1]+k)
        #Kaynaştırma Ünlüsü
        if not self.__ek.startswith(self.__unluler["tüm"]) and \
           not self.__sozcuk.endswith(self.__unluler["tüm"]):
            self.__ek=self.__kaynastirma+self.__ek
        #Düzlük-Yuvarlaklık (Küçük Ünlü) Uyumu
        if not self._duzMu():
            self.__ek=self.__ek.replace('i','ü')
        #Kalınlık-İncelik (Büyük Ünlü) Uyumu
        if not self._inceMi():
            n=0
            for i in self.__unluler["ince"]:
                self.__ek=self.__ek.replace(i,self.__unluler["kalın"][n])
                n+=1
        #Kaynaştırma Ünsüzü
        if ("su","ne").count(self.__sozcuk) > 0:
            self.__kaynastirma='y'
        if self.__sozcuk.endswith(self.__unluler["tüm"])\
            and self.__ek.startswith(self.__unluler["tüm"]):
                self.__ek=self.__kaynastirma+self.__ek
        if self.__ozelIsim:
            self.__ek="'"+self.__ek
        #İstisna 2
        self.__asilSozcuk+=self.__ek
        if self.__asilSozcuk.lower() in self._istisna["sozcük"]:
            self.__ciChange(self._istisna["sozcük"][self.__asilSozcuk.lower()])
        return self.__asilSozcuk