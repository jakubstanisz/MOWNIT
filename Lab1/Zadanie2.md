## Zadanie 2

Poniżej przedstawiono przekształcenia mające na celu zmniejszenie błędu numerycznego dla wskazanych argumentów.

- $\sqrt{x+1}-1$, $x \approx 0$
  $$\frac{(\sqrt{x+1}-1)(\sqrt{x+1}+1)}{\sqrt{x+1}+1} = \frac{x+1-1}{\sqrt{x+1}+1} = \mathbf{\frac{x}{\sqrt{x+1}+1}}$$

- $x^{2}-y^{2}$, $x \approx y$
  $$\mathbf{(x-y)(x+y)}$$

- $\frac{1-\cos x}{\sin x}$, $x \approx 0$
  $$\frac{2\sin^{2}(x/2)}{2\sin(x/2)\cos(x/2)} = \frac{\sin(x/2)}{\cos(x/2)} = \mathbf{\tan\left(\frac{x}{2}\right)}$$

- $\sin x - \sin y$, $x \approx y$
  $$\mathbf{2\sin\left(\frac{x-y}{2}\right)\cos\left(\frac{x+y}{2}\right)}$$

- $\frac{a+b}{2}$ (bisekcja odcinka $[a, b]$)
  $$\mathbf{a + \frac{b-a}{2}}$$

- $\text{softmax}(x)_{i} = \frac{\exp(x_{i})}{\sum_{j}\exp(x_{j})}$
  $M = \max(x)$ $$\mathbf{\frac{\exp(x_{i} - M)}{\sum_{j}\exp(x_{j} - M)}}$$

Różnice w wartościach oryginalnej i stabilnej wersji wyrażeń na przykładzie dwóch podpunktów, precyzja wynosi 10 cyfr znaczących.

| Oryginalna | Stabilna | Argumenty | Wartość_og | Wartość_st |
|:----------:|:--------:|:---------:|:----------:|:-------------:|
|$\mathbf{\sqrt{x+1}-1}$|$\mathbf{\frac{x}{\sqrt{x+1}+1}}$| $\mathbf{x = 10^{-11}}$ | $\mathbf{0.00000}$ | $\mathbf{5E-12}$ | 
| $\mathbf{x^2 - y^2}$ | $\mathbf{(x-y)(x+y)}$ | $\mathbf{x = 1.0000000001}$ $\mathbf{y = 1.0000000000}$ | $\mathbf{0E-9}$ | $\mathbf{2E-13}$ |

Wnioski:
- Nawet poprawna matematycznie metoda może produkować błędne wyniki w arytmetyce komputerowej, dlatego postać wzoru jest kluczowa dla stabilności.

- Błąd kancelacji można skutecznie wyeliminować poprzez przekształcenia algebraiczne, takie jak mnożenie przez sprzężenie lub faktoryzacja.

- Otrzymanie wyniku 0.00000 lub 0E-9 w wersji oryginalnej przy niezerowym wyniku wersji stabilnej dowodzi utraty informacji o wyniku na skutek zaokrągleń.

