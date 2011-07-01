
##################################################################
#
# Bu yazılım Test_12 tarafından yazılmış olup, geliştirme süreci
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
# import türkçe
#
# Kullanım örneği:
# >>> ek("Deneme").i()
# 'Denemeyi'
#
# NOT: -in iyelik eki Python'da yerleşik bir deyim olması nede-
# niyle "inn()" olarak isim verilmiştir.
#
# Hata ve görüş bildirileri için:
# E-posta : pythech.tr@gmail.com
#     Msn : physic_tr@hotmail.com
#   Xfire : physictr
#   Steam : pythech
#
# Copyright (C) 2011 Test_12.
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
    __author__ = 'Test_12'
    __kelime=""
    __ek=""
    __kaynaştırma=""
    __sertler=('p', 'ç', 't', 'k', 's', 'ş', 'h', 'f')
    __yumuşama={'p':'b','ç':'c','t':'d','k':'ğ'}
    __benzeşme={'c':'ç','d':'t','g':'k'}
    __ünlüler={"tüm":('a','e','ı','i','u','ü','o','ö'),
             "kalın":('a','ı','u','o'),
             "ince":('e','i','ü','ö'),
             "düz":('a','ı','e','i'),
             "yuvarlak":('o','u','ö','ü')}

    def __init__(self,kelime):
        self.__kelime=kelime

    def _sertMi(self):
        if self.__kelime.endswith(self.__sertler):
            return True
        else:
            return False

    def _inceMi(self):
        liste=['a',-1]
        for i in self.__ünlüler["tüm"]:
            ara=self.__kelime.rfind(i)
            if ara > liste[1]:
                liste[0]=i
                liste[1]=ara
        if self.__ünlüler["ince"].count(liste[0]) > 0:
            return True
        else:
            return False

    def _düzMü(self):
        liste=['a',-1]
        for i in self.__ünlüler["tüm"]:
            ara=self.__kelime.rfind(i)
            if ara > liste[1]:
                liste[0]=i
                liste[1]=ara
        if self.__ünlüler["düz"].count(liste[0]) > 0:
            return True
        else:
            return False

    def de(self):
        self.__ek="de"
        return self.__işle__()

    def den(self):
        self.__ek="den"
        return self.__işle__()

    def ler(self):
        self.__ek="ler"
        return self.__işle__()

    def i(self):
        self.__ek="i"
        self.__kaynaştırma="y"
        return self.__işle__()

    def inn(self):
        self.__ek="in"
        klm=self.__kelime.lower()
        if ("su","ne").count(klm) > 0:
            self.__kaynaştırma='y'
        else:
            self.__kaynaştırma="n"
        return self.__işle__()

    def e(self):
        self.__ek="e"
        self.__kaynaştırma="y"
        return self.__işle__()

    def ce(self):
        self.__ek="ce"
        return self.__işle__()


    def __işle__(self):
        #Ünsüz Sertleşmesi (Benzeşmesi)
        if self._sertMi() and self.__ek.startswith(tuple(self.__benzeşme.keys())):
            self.__ek=self.__benzeşme[self.__ek[0]]+self.__ek[1:]
        #Ünsüz Yumuşaması
        if self.__kelime.endswith(tuple(self.__yumuşama.keys()))\
            and self.__ek.startswith(self.__ünlüler["tüm"]):
                k=self.__yumuşama[self.__kelime[-1]]
                if self.__kelime[-2] == 'n' and k=='k':
                    self.__kelime=self.__kelime[:-1]+'g'
                elif k=='k':
                    pass
                else:
                    self.__kelime=self.__kelime[:-1]+k
        #Düzlük-Yuvarlaklık (Küçük Ünlü) Uyumu
        if not self._düzMü():
            self.__ek=self.__ek.replace('i','ü')
        #Kalınlık-İncelik (Büyük Ünlü) Uyumu
        if not self._inceMi():
            #ls={x:ünlüler["kalın"][ünlüler["ince"].index(x)] for x in ünlüler["ince"]}
            n=0
            for i in self.__ünlüler["ince"]:
                self.__ek=self.__ek.replace(i,self.__ünlüler["kalın"][n])
                n+=1
        #Kaynaştırma
        if self.__kelime.endswith(self.__ünlüler["tüm"])\
            and self.__ek.startswith(self.__ünlüler["tüm"]):
                self.__ek=self.__kaynaştırma+self.__ek
        self.__kelime+=self.__ek
        return self.__kelime
