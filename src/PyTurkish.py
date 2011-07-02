#!/usr/bin/python
# -*- coding: utf-8 -*-

##################################################################
#
# Bu yazılım PythEch tarafından yazılmış olup, geliştirme süreci
# devam etmektedir.
#
# Programın amacı değişkenlere gelen eklerin dilbilgisine uygun
# bir şekilde yazılmasını otomatikleştirmektir. Özellikle
# internet sitelerinde karşılaşılan bu sıkıntıdan benim gibi
# rahatsız olduysanız bu yazılımı kullaniblir ve geliştirebilir-
# siniz.
#
# Script/Betik dosyasını Python 3.x kök dizinine attıktan sonra
# ister kabuk ister betik kısmında şu kodu ekleyerek kullanmaya
# başlayabilirsiniz:
#
# import PyTurkish
#
# Kullanım örneği:
# >>> ek("Deneme").i()
# 'Denemeyi'
#
# NOT: -in iyelik eki Python'da yerleşik bir deyim olması nede-
# niyle (kaynaştırma eki ile birlikte) "nin()" olarak isimlen-
# dirilmiştir.
#
# Hata ve görüş bildirileri için:
# E-posta : pythech.tr@gmail.com
#     Msn : physic_tr@hotmail.com
#   Xfire : physictr
#   Steam : pythech
#
# Copyright (C) 2011 PythEch
#
# Bu yazılımın, GNU Özgür Belgeleme Lisansı, Sürüm 2 veya Özgür
# Yazılım Vakfı tarafından yayımlanmış daha yeni sürümlerindeki
# koşullara uygun şekilde; değişmeyen bölümler, ön kapak ve
# arka kapak metni olmaksızın, kopyalanması, dağıtılması ve/veya
# değiştirilmesine izin verilmiştir.
#
# Ayrıntılar için "GNU Genel Kamu Lisansı"na bakınız.
# Lisansın bir kopyası belge ile birlikte dağıtılmış olmalıdır.
# Dağıtılmadıysa, "http://www.gnu.org/licenses/" bağlantısına
# göz atın.
#
##################################################################

class ek():
    __author__ = 'PythEch'
    __kelime=""
    __klm=""
    __ek=""
    __kaynastirma=""
    __unlu=""
    __sertler=('p', 'ç', 't', 'k', 's', 'ş', 'h', 'f')
    __yumusama={'p':'b','ç':'c','t':'d','k':'ğ'}
    __benzesme={'c':'ç','d':'t','g':'k'}
    __unluler={"tüm":('a','e','ı','i','u','ü','o','ö'),
             "kalın":('a','ı','u','o'),
             "ince":('e','i','ü','ö'),
             "düz":('a','ı','e','i'),
             "yuvarlak":('o','u','ö','ü')}

    def __init__(self,kelime):
        self.__kelime=kelime
        self.__klm=self.__kelime.lower()

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
            self.__unlu="i"
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
        #Ünsüz Sertleşmesi (Benzeşmesi)
        if self._sertMi() and self.__ek.startswith(tuple(self.__benzesme.keys())):
            self.__ek=self.__benzesme[self.__ek[0]]+self.__ek[1:]
        #Ünsüz Yumuşaması
        if self.__kelime.endswith(tuple(self.__yumusama.keys()))\
            and self.__ek.startswith(self.__unluler["tüm"]):
                k=self.__yumusama[self.__kelime[-1]]
                if self.__kelime[-2] == 'n' and k=='k':
                    self.__kelime=self.__kelime[:-1]+'g'
                elif k=='k':
                    pass
                else:
                    self.__kelime=self.__kelime[:-1]+k
        #Ara Ünlüsü
        if not self.__ek.startswith(self.__unluler["tüm"]) and \
           not self.__kelime.endswith(self.__unluler["tüm"]):
            self.__ek=self.__unlu+self.__ek
        #Düzlük-Yuvarlaklık (Küçük Ünlü) Uyumu
        if not self._duzMu():
            self.__ek=self.__ek.replace('i','ü')
        #Kalınlık-İncelik (Büyük Ünlü) Uyumu
        if not self._inceMi():
            #ls={x:ünlüler["kalın"][ünlüler["ince"].index(x)] for x in ünlüler["ince"]}
            n=0
            for i in self.__unluler["ince"]:
                self.__ek=self.__ek.replace(i,self.__unluler["kalın"][n])
                n+=1
        #Kaynaştırma
        if ("su","ne").count(self.__klm) > 0:
            self.__kaynastirma='y'
        if self.__kelime.endswith(self.__unluler["tüm"])\
            and self.__ek.startswith(self.__unluler["tüm"]):
                self.__ek=self.__kaynastirma+self.__ek
        self.__kelime+=self.__ek
        return self.__kelime

