PyTurkish
=======

PyTurkish, adından da anlaşılacağı üzere Python ile yazılmış bir çekim ekleri kütüphanesidir. Örnek kullanım:
```python
from PyTurkish import *

print "%s mesaj at." % Ek("Hakan", True).e()
print "%s selam söyle..." % Ek("Mustafa", True).benim().e()
```

Şu anda kısıtlı bir Hâl Ekleri, Çoğul ve Eşitlik Eki, İyelik Ekleri, Tamlayan ve Tamlayan Ekleri desteği var.

Github varsayılan ANSI versiyonu görüntülerken encoding sorunları yaşıyor, bunun için raw olarak indirmeniz gerek.

Değişiklikler
--------------
- 2.0
+ Sıfırdan yazıldı, kod kalabalığı kaldırıldı, okunabilirlik arttırıldı.
+ Heceleme fonksiyonu eklendi.
+ Artık 'string' yerine Ek 'class'ı döndürülüyor, yani zincirleme eklemeler tek satırda mümkün.
+ Bazı gereksiz şeyler kaldırıldı.
+ Python 3.x desteği.
+ Timeit testlerine göre bilgisayarımda bu sürüm 5 kat daha hızlı.

Yapılacaklar
--------------
+ İstisnalar ve sayılar tekrar eklenecek
+ Tamlama kaynaştırma ekleri desteği
+ Bağlaç desteği