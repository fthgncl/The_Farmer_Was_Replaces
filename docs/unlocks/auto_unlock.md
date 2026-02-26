# Otomatik Kilit Açma
Oyunu tamamen otomatikleştirmek için, özellikleri otomatik olarak açmak üzere `unlock()` fonksiyonunu kullanabilirsiniz.
Örneğin, hız ve genişletme özelliklerinin kilidini açmak için `unlock(Unlocks.Speed)` ve `unlock(Unlocks.Expand)` kullanabilirsiniz.

Bir kilidin maliyetini belirlemek için, tıpkı bir bitki veya eşya için yaptığınız gibi `get_cost()` fonksiyonunu kullanın.
Örnek:
`get_cost(Unlocks.Loops)`
`{Items.Hay:5}` döndürür
