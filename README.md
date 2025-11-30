# 📘 **“Una misión de Eric, Miguel y Alfonso”**

Era una tarde nublada en MATCOM cuando **Eric**, **Miguel** y **Alfonso** recibieron un mensaje inesperado de la profesora de ecuaciones diferenciales:

> *"Equipo: su misión de hoy es resolver la dinámica completa de un automóvil diesel, desde su aceleración hasta su comportamiento oscilatorio. Ah, y háganlo antes de que cierre la cafetería."*

Los tres se miraron.
La presión era real: **si no terminaban, se quedaban sin empanadas**.

---

## 🚗 **Parte A — Cinemática directa: El arranque del auto**

> "Ok, empezamos suave"

dijo **Miguel**, siempre optimista.

El auto tenía la aceleración:

$
\frac{dv}{dt} = 0.12 t^2 + 0.6 t,
$

y partía del reposo:
$
t_0 = 0, \quad v_0 = 0.
$

>"¡Esto es integrable!" 

gritó **Eric**, emocionado como si hubiera descubierto oro.

(Miguel y Alfonso sospechan que Eric no sabe integrar)

Integraron la aceleración (sin Eric):

$
v(t) = \int(0.12 t^2 + 0.6 t)\,dt
= 0.04 t^3 + 0.3 t^2 + C.
$

Como $v(0)=0$, entonces $C=0$.

En los primeros 10 segundos:

$
v(10) = 0.04(1000) + 0.3(100) = 40 + 30 = 70 \text{ m/s}.
$

> "70 metros por segundo... ese carro anda más duro que el wifi del laboratorio"
bromeó **Alfonso**.

Después integraron la velocidad para encontrar la distancia:

$
x(t)=\int (0.04 t^3 + 0.3 t^2)\,dt
=0.01 t^4 + 0.1 t^3.
$

Entonces:

$
x(10)=0.01(10^4)+0.1(1000)=100+100=200 \text{ m}.
$

> "En 10 segundos recorrió **200 metros**. Ese carro sí es diesel premium"

dijo Miguel.

> "Todo gracias a mi! 

dijo Eric sin entender mucho que habia pasado

Luego dibujaron el campo de isoclinas para ver cómo la velocidad aumentaba suavemente con el tiempo.

---

## 🔱 **Parte B — La bifurcación pitchfork**

Cuando comenzaron con:

$
\frac{dv}{dt}=rv - v^3,
$

Alfonso preguntó:

> "¿Qué tiene que ver esto con el carro?"

Eric respondió:

> "Es como el punto en el que el motor decide si se apaga, arranca o gira estable. ¡Esto es física de verdad!"

Encontraron los equilibrios:

$
v_0 = 0, \qquad v_{\pm} = \pm\sqrt{r}.
$

Eric notó:

* Si $r<0$: solo existe $v=0$, estable → *motor apagado*.
* Si $r>0$: aparecen $\pm\sqrt{r}$ estables → *motor encendido*.

Miguel dibujó el clásico "tenedor" del *pitchfork* y dijo:

> "Entonces el motor pasa de dormido a prendido al cruzar $r=0$... ¡igual que yo cuando me dan café!"

Todos rieron.

---

## 🌀 **Parte C — El resorte amortiguado**

Ya faltaban 10 minutos para que cerrara la cafetería.

El sistema era:

$
\dot x = v, \qquad
\dot v = -\alpha v - \beta x.
$

> "Esto es un sistema lineal de primer orden"

dijo Eric.

> "Como cuando el auto queda pegado a un resorte... literal física I."

Hallaron el punto crítico:

$
(x^*,v^*)=(0,0).
$

El análisis del Jacobiano les mostró que, según los parámetros $\alpha,\beta>0$, el origen es un:

* **Nodo estable** si la amortiguación es fuerte.
* **Foco espiral estable** si la amortiguación es débil.

Miguel interpretó el plano de fase:

> "El carro oscila si hay poco amortiguamiento, como un resorte suave... pero si hay mucho, vuelve al equilibrio sin oscilar."

Alfonso añadió:

> "O sea, si el auto está amarrado a un resorte gigante... ¡normal!"

(Eric seguia sin entender mucho)

---

## 🎉 **Final**
A las **11:57 am**, tres minutos antes del cierre, terminaron todo el análisis:

* Cinemática del auto
* Plano de fase resorte–amortiguador

El profesor les escribió:

> *"Excelente trabajo, equipo. Las empanadas están ganadas."*

Y así, **Eric**, **Miguel** y **Alfonso** salvaron la tarde...
y la merienda.

---
