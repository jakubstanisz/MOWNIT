**Sprawozdanie: Metody obliczeniowe w nauce i technice – Laboratorium 9**
**Temat:** Równania różniczkowe zwyczajne - część I
**Data:** 12.05.2026

---

### Cel ćwiczenia i opis metod
Celem niniejszego ćwiczenia laboratoryjnego jest zapoznanie się z metodami numerycznego rozwiązywania równań różniczkowych zwyczajnych (ODE). W ramach zadań dokonano przekształceń równań wyższych rzędów do równoważnych układów równań pierwszego rzędu oraz zbadano stabilność analityczną i numeryczną problemów. Główny nacisk położono na analizę metody Eulera w wariancie jawnym oraz niejawnym, badając jej zbieżność, obszar stabilności, a także zachowanie i rzędy zbieżności dla różnych wartości kroku całkowania $h$.

---

### Zadanie 1. Przekształcenia do układów pierwszego rzędu

Należy przedstawić każde z poniższych równań różniczkowych zwyczajnych jako równoważny układ równań pierwszego rzędu.

**(a) Równanie Van der Pol'a:**
$$y^{\prime\prime}=y^{\prime}(1-y^{2})-y$$

Wprowadzamy nową zmienną $t = \frac{dy}{dx}$.
Otrzymujemy:
$$\frac{dt}{dx}=\frac{d^{2}y}{dy^{2}}$$
$$\frac{dt}{dx}=t(1-y^{2})-y$$

Układ równań ma postać:
$$\begin{cases}\frac{dy}{dx}=t\\ \frac{dt}{dx}=t(1-y^{2})-y\end{cases}$$

**(b) Równanie Blasiusa:**
$$y^{\prime\prime\prime}=-yy^{\prime\prime}$$

Wprowadzamy zmienne pomocnicze $t = y^{\prime}$ oraz $z = t^{\prime} = y^{\prime\prime}$.
Układ równań przyjmuje postać:
$$\begin{cases}y^{\prime}=t\\ t^{\prime}=y^{\prime\prime}=z\\ z^{\prime}=-yt^{\prime}=-yz\end{cases}$$

**(c) II zasada dynamiki Newtona dla problemu dwóch ciał:**
$$y_{1}^{\prime\prime}=-\frac{GMy_{1}}{(y_{1}^{2}+y_{2}^{2})^{3/2}}$$
$$y_{2}^{\prime\prime}=-\frac{GMy_{2}}{(y_{1}^{2}+y_{2}^{2})^{3/2}}$$

Wprowadzamy zmienne $z_1 = y_1^{\prime}$ oraz $z_2 = y_2^{\prime}$. Równoważny układ równań to:
$$\begin{cases}y_{1}^{\prime}=z_{1}\\ y_{2}^{\prime}=z_{2}\\ z_{1}^{\prime}=-\frac{GMy_{1}}{(y_{1}^{2}+y_{2}^{2})^{3/2}}\\ z_{2}^{\prime}=-\frac{GMy_{2}}{(y_{1}^{2}+y_{2}^{2})^{3/2}}\end{cases}$$

---

### Zadanie 2. Przekształcenie do autonomicznego problemu początkowego

Dany jest problem początkowy:
$$y_{1}^{\prime}=\frac{y_{1}}{t}+y_{2}t$$
$$y_{2}^{\prime}=\frac{t(y_{2}^{2}-1)}{y_{1}}$$
$$y_{1}(1)=1$$
$$y_{2}(1)=0$$

Autonomiczny problem początkowy ma postać:
$$\begin{cases}y^{\prime}(t)=f(y)\\ y(t_{0})=y_{0}\end{cases}$$

Aby pozbyć się bezpośredniej zależności od zmiennej niezależnej $t$, wprowadzamy dodatkową zmienną $y_3 = t$. Z definicji wynika, że $y_3^{\prime} = 1$. 
Otrzymujemy autonomiczny problem:
$$\begin{cases}y_{1}^{\prime}=\frac{y_{1}}{y_{3}}+y_{2}y_{3}\\ y_{2}^{\prime}=\frac{y_{3}(y_{2}^{2}-1)}{y_{1}}\\ y_{3}^{\prime}=1\end{cases}$$
Z warunkami początkowymi: $y_1(1)=1$, $y_2(1)=0$, $y_3(1)=1$.

---

### Zadanie 3. Problem początkowy i dziedzina rozwiązania

Dany jest problem:
$$y^{\prime}=\sqrt{1-y}$$
$$y(0)=0$$

Sprawdzamy, czy funkcja $y(t)=\frac{t(4-t)}{4}$ spełnia powyższe równanie.
Obliczamy pochodną:
$$y^{\prime}(t)=\frac{4-2t}{4}=1-\frac{t}{2}$$
Podstawiamy do prawej strony równania:
$$\sqrt{1-y(t)} = \sqrt{1-\frac{4t-t^{2}}{4}}=\sqrt{\frac{4-4t+t^{2}}{4}}=\sqrt{\left(1-\frac{t}{2}\right)^{2}}=1-\frac{t}{2}$$
Ponadto warunek początkowy jest spełniony: $y(0)=\frac{0(4-0)}{4}=0$.

**Wyznaczenie dziedziny:**
Wyrażenie pod pierwiastkiem musi być nieujemne, zatem $y(t) \le 1$.
$$\frac{t(4-t)}{4}\le1 \implies \frac{4t-t^{2}-4}{4}\le0 \implies -\frac{(t-2)^{2}}{4}\le0$$
Powyższy warunek jest spełniony dla każdego $t \in (-\infty,\infty)$.

Dodatkowo wyrażenie $1-\frac{t}{2}$ (z uwagi na to, że jest wynikiem pierwiastkowania) musi być nieujemne:
$$1-\frac{t}{2}\ge0 \implies t\le2$$

Łącznie dziedzina to: $t\in(-\infty,2]$.

---

### Zadanie 4. Metoda Eulera dla równania liniowego

Dano równanie:
$$y^{\prime}=-5y, \quad y(0)=1$$
Krok całkowania $h=0.5$.

**(a) Analityczna stabilność**
Analityczne rozwiązanie równania to $y(t)=e^{-5t}$.
Granica w nieskończoności: $\lim_{t\rightarrow\infty}e^{-5t}=0$.
Funkcja maleje do zera bez osobliwości, rozwiązanie jest asymptotycznie stabilne.

**(b) Dowód zbieżności jawnej metody Eulera**
Z definicji metody Eulera: $y_{n+1}=y_{n}+hf(t_{n},y_{n})$.
$$y_{n+1}=y_{n}+h(-5y_{n}) = y_{n}(1-5h)$$
Z warunku początkowego: $y_{n}=y_{0}(1-5h)^{n} = (1-5h)^{n}$.
Korzystając z faktu, że $nh = t$:
$$\lim_{h\rightarrow0, n\rightarrow\infty}y_{n} = \lim_{h\rightarrow0, n\rightarrow\infty}(1-5h)^{n} = \lim_{h\rightarrow0}\left((1-5h)^{\frac{1}{-5h}}\right)^{-5nh} = e^{-5t} = y(t)$$
Dowodzi to zbieżności metody.

**(c) Numeryczna stabilność (metoda jawna)**
Warunek stabilności dla metody jawnej: $|1+h\lambda| \le 1$.
Podstawiając: $|1+0.5 \cdot (-5)| = |-1.5| = 1.5 > 1$.
Metoda jawna nie jest stabilna numerycznie dla tego kroku.

**(d) Obliczenia numeryczne dla $t=0.5$ (metoda jawna)**
Wykonujemy 1 krok ($h=0.5$):
$$y_{1} = 1 \cdot (1 - 5 \cdot 0.5) = -1.5$$
Wartość rzeczywista to $y(0.5) = e^{-2.5} \approx 0.08208$.

**(e) Numeryczna stabilność (metoda niejawna)**
Metoda niejawna jest bezwarunkowo stabilna dla $h>0$ przy ujemnej lambdzie, ponieważ $\left|\frac{1}{1-h\lambda}\right| \le 1$.

**(f) Obliczenia numeryczne dla $t=0.5$ (metoda niejawna)**
Dla 1 kroku:
$$y_{1} = y_{0} + h(-5y_{1}) \implies y_{1} = \frac{y_{0}}{1+5h} = \frac{1}{1 + 2.5} = \frac{1}{3.5} \approx 0.2857$$

**(g) Maksymalny krok $h$ przy żądanej tolerancji $0.001$**
Wymagamy $|y_{n}-y(t_{n})| < 0.001$ w punkcie $t_{n}=0.5$.
$$|(1-5h)^{\frac{0.5}{h}}-e^{-2.5}| < 0.001$$
Rozwiązanie przybliżono metodą numeryczną (kod w załączonym pliku `lab9_kody.ipynb`).
Wynik to: $h \approx 0.0019484$, co odpowiada $n=257$ krokom.

**(h) Bezpośrednia iteracja i metoda Newtona w metodzie niejawnej**
Wzór na metodę niejawną:
$$y_{n+1}=y_{n}+h(-5)y_{n+1}$$
Stosując bezpośrednią iterację, funkcja iterująca to: $\varphi(y)=y_{n}-5hy$.
Warunek zbieżności:
$$|\varphi^{\prime}(y)| < 1 \implies |-5h| < 1 \implies 5h < 1 \implies h < \frac{1}{5}$$
Użycie metody Newtona jest tutaj optymalne (uzasadnione), ponieważ funkcja $\varphi(y)$ jest liniowa i algorytm znajdzie pierwiastek w zaledwie pierwszej iteracji.

---

### Zadanie 5. Stabilność dla układu równań

Dany jest układ:
$$y_{1}^{\prime}=-2y_{1}+y_{2}$$
$$y_{2}^{\prime}=-y_{1}-2y_{2}$$

Wyznaczamy wartości własne macierzy układu:
$$A-\lambda I=\begin{pmatrix}-2-\lambda&1\\ -1&-2-\lambda\end{pmatrix}$$
$$\det(A-\lambda I)=(-2-\lambda)^{2}-(-1) \cdot 1 = \lambda^{2}+4\lambda+5=0$$
Pierwiastki równania to: $\lambda_{1}=-2+i$, $\lambda_{2}=-2-i$.

Dla metody jawnej Eulera warunek stabilności nakazuje, by dla każdej wartości własnej $\lambda$:
$$|1+\lambda h| < 1$$
Analizujemy dla $\lambda = -2+i$:
$$|1+(-2+i)h| < 1 \implies |(1-2h)+ih| < 1$$
$$\sqrt{(1-2h)^{2}+h^{2}} < 1 \implies 1-4h+4h^{2}+h^{2} < 1$$
$$5h^{2}-4h < 0 \implies h(5h-4) < 0$$
Warunek stabilności określa zbiór: $h \in \left(0,\frac{4}{5}\right)$.
Obliczenia dla $\lambda = -2-i$ prowadzą do identycznego warunku.

---

### Zadanie 6. Empiryczny rząd zbieżności

Dany jest problem:
$$y^{\prime}=\alpha t^{\alpha-1}, \quad y(0)=0$$
Gdzie $\alpha \in \{2.5, 1.5, 1.1\}$, krok $h \in \{0.2, 0.1, 0.05\}$. Rozwiązaniem jest funkcja $y(t)=t^{\alpha}$.
Wyniki błędów względnych obliczono skryptem i na ich podstawie wyznaczono empiryczny rząd zbieżności $r$ ze wzoru na spadek błędu ze zmianą siatki (kod w załączonym notesie Jupyter). 

Uzyskane empiryczne rzędy zbieżności:
$$r_{\alpha_{1}} \approx 0.905347$$
$$r_{\alpha_{2}} \approx 1.289960$$
$$r_{\alpha_{3}} \approx 1.865001$$

**Analiza:**
Kształt wykresów błędu jest bardzo podobny dla różnych wartości $h$, przy czym im mniejsze $h$, tym mniejszy błąd numeryczny. Znaczną różnicę obserwuje się manipulując rzędem wielomianu $\alpha$. Dla małego $\alpha=1.1$ błąd względny maleje szybciej w relacji do $t$ niż dla $\alpha=1.5$. Metoda jest niestabilna w punkcie 0 dla pochodnych o zerowej wartości startowej bez odpowiedniego formowania różnic.

---

### Wnioski

Przeprowadzone laboratorium poszerzyło wiedzę dotyczącą numerycznego rozwiązywania równań różniczkowych. Początkowe zadania przypomniały techniki analitycznego przekształcania równań do standardowej postaci autonomicznej, co jest kluczowe przy modelowaniu przed podaniem układu na wejście dowolnej procedury numerycznej. Analiza metody Eulera w wariantach niejawnym i jawnym wskazała na jej fizyczne ograniczenia – jaskrawo widoczne, kiedy parametry przestają zapewnić stabilność numeryczną. Otrzymane wykresy oraz błędy względne dały czytelny obraz tego, jak kształtuje się dokładność badanej metody dla problemów nieliniowych i jak zmienia się wraz z redukcją parametrów całkowania.

---