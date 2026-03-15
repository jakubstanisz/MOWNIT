## Zadanie 4
Celem ćwiczenia było Porównanie pięciu metod sumowania $n$ liczb typu float32 względem wyniku wzorcowego z math.fsum()

Metody:
- (a) Sumowanie losowe z akumulatorem float64
- (b) Sumowanie losowe z akumulatorem float32
- (c) Algorytm Kahana (kompensacja błędu), float32
- (d) Sumowanie po posortowaniu rosnąco, float32
- (e) Sumowanie po posortowaniu malejąco, float32

![image](zadanie4_graph.png)

Wnioski:
- Algorytm Kahana (c) za każdym razem daje najdokładniejszy wynik
- Zastosowanie akumulatora float64 (a) znacząco redukuje błąd względem metod 32-bitowych
- Standardowe metody (b, d, e) wykazują zbliżony poziom błędów przy niskiej precyzji obliczeń