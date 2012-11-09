#!/usr/bin/python
# -*- coding: utf-8 -*-

##################################################################
#
# Copyright (C) 2011-2012 PythEch
#
# This Source Code Form is subject to the terms of the Mozilla 
# Public License, v. 2.0. If a copy of the MPL was not distributed 
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
##################################################################

# bobince'e Teþekkürler: http://stackoverflow.com/a/722175/180343
import weakref, new
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
    __kelime=""
    __ek=""
    __kaynastirma=""
    __ozelIsim=""
    __sertler=('p', 'ç', 't', 'k', 's', 'þ', 'h', 'f')
    __yumusama={'p':'b','ç':'c','t':'d','k':'ð'}
    __benzesme={'c':'ç','d':'t','g':'k'}
    __unluler={"tüm":('a','e','ý','i','u','ü','o','ö'),
             "kalýn":('a','ý','u','o'),
             "ince":('e','i','ü','ö'),
             "düz":('a','ý','e','i'),
             "yuvarlak":('o','u','ö','ü')}
    #Tamamlanacak
    _istisna={"kök":{"þu":"þun", "bu":"bun", "o":"on"}, #Ek aldýklarýnda kökü deðiþen kelimeler
              "kelime":{"bene":"bana", "sene":"sana"} #Diðer istisnalar
    }

    def __repr__(self):
        return self.__kelime
    
    def __init__(self,Kelime,ozelIsim=False):
        self.__kelime=Kelime.lower()
        self.__ozelIsim = ozelIsim

    def _sertMi(self):
        if self.__kelime.endswith(self.__sertler):
            return True
        else:
            return False

    def _inceMi(self):
        liste=['a',-1]
        for i in self.__unluler["tüm"]:
            ara=self.__kelime.rfind(i)
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
            ara=self.__kelime.rfind(i)
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
            n+=self.__kelime.count(i)
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
        if self._kacHeceli() == 1:
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
        #Ünsüz Sertleþmesi (Benzeþmesi)
        if self._sertMi() and self.__ek.startswith(tuple(self.__benzesme.keys())):
            self.__ek=self.__benzesme[self.__ek[0]]+self.__ek[1:]
        #Ünsüz Yumuþamasý
        if self.__kelime.endswith(tuple(self.__yumusama.keys()))\
            and self.__ek.startswith(self.__unluler["tüm"]):
                k=self.__yumusama[self.__kelime[-1]]
                if self.__kelime[-2] == 'n' and k=='k':
                    self.__kelime=self.__kelime[:-1]+'g'
                elif k=='k':
                    pass
                else:
                    self.__kelime=self.__kelime[:-1]+k
        #Kaynaþtýrma Ünlüsü
        if not self.__ek.startswith(self.__unluler["tüm"]) and \
           not self.__kelime.endswith(self.__unluler["tüm"]):
            self.__ek=self.__kaynastirma+self.__ek
        #Düzlük-Yuvarlaklýk (Küçük Ünlü) Uyumu
        if not self._duzMu():
            self.__ek=self.__ek.replace('i','ü')
        #Kalýnlýk-Ýncelik (Büyük Ünlü) Uyumu
        if not self._inceMi():
            n=0
            for i in self.__unluler["ince"]:
                self.__ek=self.__ek.replace(i,self.__unluler["kalýn"][n])
                n+=1
        #Kaynaþtýrma Ünsüzü
        if ("su","ne").count(self.__kelime) > 0:
            self.__kaynastirma='y'
        if self.__kelime.endswith(self.__unluler["tüm"])\
            and self.__ek.startswith(self.__unluler["tüm"]):
                self.__ek=self.__kaynastirma+self.__ek
        if self.__ozelIsim:
            self.__ek="'"+self.__ek
        #Ýstisna
        if self.__ek in self._istisna["kök"]:
            self.__ek = self._istisna["kök"][self.__ek]
        self.__kelime+=self.__ek
        if self.__kelime in self._istisna["kelime"].keys():
            self.__kelime = self._istisna["kelime"][self.__kelime]
        return self.__kelime