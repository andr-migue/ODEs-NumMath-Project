# Propuesta de Proyecto Interactivo en Unity para el Tema 1

---

## Concepto General del Proyecto en Unity

Crearás una aplicación con una interfaz principal que permita al usuario seleccionar y explorar tres escenas diferentes, cada una correspondiente a una de las partes del Tema 1:

1. **Escena A(completada):** Cinemática y Métodos Numéricos
2. **Escena B:** Análisis de Bifurcación
3. **Escena C(completada):** Oscilador Amortiguado y Plano de Fase

Cada escena tendrá una simulación 3D de un automóvil y una interfaz de usuario (UI) que mostrará los gráficos y datos relevantes, cumpliendo con todos los requisitos del "Enfoque".

---

## Escena A: Cinemática Directa (Parte A)

**Objetivo:** Simular el movimiento del coche bajo una aceleración variable y analizar el rendimiento de diferentes métodos numéricos.

#### 1. Simulación 3D

* Un modelo 3D de un automóvil sobre una pista recta.
* Al presionar "Iniciar", el coche se moverá desde el reposo (`t=0`, `x=0`, `v=0`).
* El movimiento se calculará en cada frame resolviendo la EDO: `dv/dt = 0.12t² + 0.6t`.

#### 2. Implementación del "Enfoque" (UI)

* **Panel de Modelación:**
  * Mostrar la EDO: `dv/dt = 0.12t² + 0.6t`.
  * Mostrar las condiciones iniciales: `v(0)=0`, `x(0)=0`.

* **Panel de Análisis Numérico (Interactivo):**
  * **Menú de Algoritmo:** Un desplegable para que el usuario elija el método numérico:
        1. Euler
        2. Runge-Kutta 2 (RK2)
        3. Runge-Kutta 4 (RK4)
  * **Panel de Comparación y Error:**
    * Calcula y almacena la solución analítica (real):
      * `v(t) = 0.04t³ + 0.3t²`
      * `x(t) = 0.01t⁴ + 0.1t³`
    * La UI mostrará en tiempo real:
      * Tiempo (`t`)
      * Posición Numérica (del coche simulado)
      * Posición Analítica (el valor real)
      * Error Relativo %
  * Al final de los 10s, mostrar un resumen con los valores finales y el error total, demostrando la superioridad de RK4.

* **Panel de Visualización (Campo de Isoclinas):**
  * Una ventana 2D en la UI mostrará el campo de isoclinas pre-calculado en el plano `(t, v)`.
  * Mientras el coche 3D se mueve, un punto rojo en este gráfico 2D seguirá la trayectoria `(t, v(t))` del coche, mostrando cómo la solución sigue las pendientes del campo.

---

## Escena B: Bifurcación (Parte B)

**Objetivo:** Mostrar cómo un parámetro `r` cambia cualitativamente el comportamiento del sistema.

#### 1. Visualización 3D

* Un modelo 3D del coche.
* Un **slider** en la UI para controlar el valor del parámetro `r`.
* El coche puede cambiar su estado visualmente:
  * Si `r < 0`: Se muestra detenido en una posición estable.
  * Si `r > 0`: Se muestra vibrando o con un aura que indique inestabilidad.

#### 2. Implementación del "Enfoque" (UI)

* **Panel de Modelación:**
  * Mostrar la EDO: `dv/dt = rv - v³`.

* **Panel de Análisis y Visualización (Diagrama de Bifurcación):**
  * La parte central. Un gráfico 2D con:
    * Eje horizontal: Parámetro `r`.
    * Eje vertical: Puntos de equilibrio `v`.
  * Dibujar el diagrama de bifurcación tipo "horquilla":
    * Línea `v=0` para `r < 0` (**estable**, color verde).
    * Línea `v=0` para `r > 0` (**inestable**, color rojo).
    * Ramas `v = √r` y `v = -√r` para `r > 0` (**estables**, color verde).
  * **Interactividad:** Al mover el slider de `r`, una línea vertical se moverá sobre el diagrama, mostrando los equilibrios para ese valor de `r`. El coche 3D cambiará su estado en `r=0`.

---

## Escena C: Plano de Fase (Parte C)

**Objetivo:** Modelar el coche como un oscilador amortiguado y visualizar su comportamiento en el plano de fase.

#### 1. Simulación 3D

* Modelo 3D del coche, opcionalmente con un resorte visible que se estire/comprima.
* El usuario puede establecer las condiciones iniciales:
  * Haciendo clic y arrastrando el coche a una posición inicial `x₀`.
  * Introduciendo una velocidad inicial `v₀` en la UI.
* Al simular, el coche oscilará hasta detenerse.

#### 2. Implementación del "Enfoque" (UI)

* **Panel de Modelación:**
  * Mostrar el sistema de EDOs: `dx/dt = v`, `dv/dt = -αv - βx`.
  * **Sliders** para que el usuario modifique `α` (amortiguamiento) y `β` (constante del resorte).

* **Panel de Análisis y Plano de Fase (UI 2D):**
  * **Clasificación Automática:** Un texto mostrará la clasificación del punto crítico `(0,0)` según los valores de `α` y `β`:
    * Si `α² - 4β > 0`: "Nodo Estable (Sobre-amortiguado)"
    * Si `α² - 4β = 0`: "Nodo Degenerado (Críticamente Amortiguado)"
    * Si `α² - 4β < 0`: "Foco Estable (Sub-amortiguado)"
  * **Visualización del Plano de Fase:**
    * Un gran gráfico 2D del plano de fase (eje X: posición, eje Y: velocidad).
    * Dibujar el campo de direcciones del sistema en el fondo.
    * Durante la simulación 3D, dibujar en tiempo real la trayectoria correspondiente en el plano de fase. El usuario verá espirales (Foco) o curvas directas (Nodo).

* **Panel de Validación (Benchmarks):**
  * Un botón de "Caso de Prueba" puede fijar `α=0` (oscilador simple) para comparar la simulación con la solución analítica conocida y verificar la precisión.

---

### Resumen del Flujo de Trabajo en Unity

1. **Configuración del Proyecto:** Crea las tres escenas y la navegación entre ellas.
2. **Creación de Assets:** Consigue un modelo de coche 3D. Diseña la UI con paneles para gráficos, sliders y botones.
3. **Implementación de Solvers:** Crea scripts en C# para los métodos de Euler y Runge-Kutta.
4. **Desarrollo por Escena:**
    * **Escena A:** Enfócate en la simulación de movimiento y la comparación de errores.
    * **Escena B:** Enfócate en la interactividad del slider y el dibujo del diagrama de bifurcación.
    * **Escena C:** Enfócate en el dibujo dinámico del plano de fase y la clasificación automática del sistema.
