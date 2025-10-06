import numpy as np
from matplotlib import pyplot as plt

def Euler_Method(f, x0, y0, h, xfinal):
    n_steps = int((xfinal - x0) / h)
    xs = np.zeros(n_steps + 1)
    ys = np.zeros(n_steps + 1)

    # condiciones iniciales
    xs[0] = x0
    ys[0] = y0

    # iteración de Euler
    for i in range(1, n_steps + 1):
        xs[i] = xs[i-1] + h
        ys[i] = ys[i-1] + h * f(xs[i-1], ys[i-1])

    return xs, ys

def Improved_Euler_Method(f, x0, y0, h, xfinal):
    # Calculate number of steps
    n_steps = int((xfinal - x0) / h)
    
    # Initialize arrays for x and y values
    xs = np.zeros(n_steps + 1)
    ys = np.zeros(n_steps + 1)
    
    # Set initial conditions
    xs[0] = x0
    ys[0] = y0
    
    # Improved Euler Method iteration (Heun's Method)
    for i in range(1, n_steps + 1):
        # Update x value
        xs[i] = xs[i-1] + h
        
        # Calculate slope at current point
        k1 = f(xs[i-1], ys[i-1])
        
        # Calculate estimated y value using Euler step
        y_pred = ys[i-1] + h * k1
        
        # Calculate slope at predicted point
        k2 = f(xs[i], y_pred)
        
        # Calculate final y value using average slope
        ys[i] = ys[i-1] + (h/2) * (k1 + k2)
        
    return xs, ys

def RK4_Method(f, x0, y0, h, xfinal):
    n_steps = int((xfinal - x0) / h)
    xs = np.zeros(n_steps + 1)
    ys = np.zeros(n_steps + 1)

    # condiciones iniciales
    xs[0] = x0
    ys[0] = y0

    # iteración de RK4
    for i in range(1, n_steps + 1):
        x = xs[i-1]
        y = ys[i-1]

        k1 = f(x, y)
        k2 = f(x + h/2, y + h/2 * k1)
        k3 = f(x + h/2, y + h/2 * k2)
        k4 = f(x + h, y + h * k3)
        xs[i] = x + h
        ys[i] = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    return xs, ys


def Bisection_Method(f, a, b, tol_f=1e-6, tol_x=1e-6, max_iter=100):
    """
    Método de bisección con criterios de parada mejorados.
    Retorna valor , hisorial , mensaje
    """
    if f(a) * f(b) >= 0:
        return None,None, "Error: f(a) y f(b) deben tener signos opuestos"
    
    iter_count = 0
    history = []  # Para tracking de convergencia
    
    while iter_count < max_iter:
        c = (a + b) / 2
        f_c = f(c)
        
        # Criterio 1: Tolerancia en función
        if abs(f_c) < tol_f:
            return c,history, f"Convergencia por |f(x)| < {tol_f} en {iter_count} iteraciones"
        
        # Criterio 2: Tolerancia en argumento (ancho del intervalo)
        if (b - a) / 2 < tol_x:
            return c, history, f"Convergencia por ancho de intervalo < {tol_x} en {iter_count} iteraciones" 
        
        # Continuar bisección
        if f(a) * f_c < 0:
            b = c
        else:
            a = c
            
        history.append((c, f_c, b-a))
        iter_count += 1
    
    return (a + b) / 2,history, f"Máximo de iteraciones ({max_iter}) alcanzado"

def Newton_Raphson_Method(f, df, x0, tol_f=1e-6, tol_x=1e-6, tol_rel=1e-6, max_iter=100):
    """
    Método de Newton-Raphson con criterios de parada mejorados
    """
    x = x0
    iter_count = 0
    history = []
    
    while iter_count < max_iter:
        f_x = f(x)
        df_x = df(x)
        
        # Criterio de falla: derivada cero
        if abs(df_x) < 1e-14:
            return x, f"Falla: derivada aproximadamente cero en x = {x}"
        
        # Criterio 1: Tolerancia en función
        if abs(f_x) < tol_f:
            return x, f"Convergencia por |f(x)| < {tol_f} en {iter_count} iteraciones"
        
        # Calcular nuevo punto
        dx = f_x / df_x
        x_new = x - dx
        
        # Criterio 2: Tolerancia absoluta en argumento
        if abs(dx) < tol_x:
            return x_new, f"Convergencia por |dx| < {tol_x} en {iter_count} iteraciones"
        
        # Criterio 3: Tolerancia relativa
        if abs(x_new) > 1e-10:  # Evitar división por números muy pequeños
            if abs(dx) / abs(x_new) < tol_rel:
                return x_new, f"Convergencia relativa |dx/x| < {tol_rel} en {iter_count} iteraciones"
        
        history.append((x, f_x, dx))
        x = x_new
        iter_count += 1
    
    return x, f"Máximo de iteraciones ({max_iter}) alcanzado"

def isocline(dy_dx , exact_solution, x_interval , y_interval , step_size , h):

    # CONFIGURACIÓN DEL DOMINIO DE VISUALIZACIÓN
    x_min, x_max = x_interval    # Rango en x de -5 a 2
    y_min, y_max = y_interval    # Rango en y de -3 a 8

    # 1. GENERACIÓN DEL CAMPO DE PENDIENTES
    # Crea una malla de puntos para visualizar las pendientes
    x_field = np.linspace(x_min, x_max, h)  # Puntos en x cada 0.5 unidades
    y_field = np.linspace(y_min, y_max, h)  # Puntos en y cada 0.5 unidades
    X_field, Y_field = np.meshgrid(x_field, y_field)  # Malla 2D

    # Calcula las componentes del campo vectorial
    DX = np.ones_like(X_field)      # Componente x siempre 1 (dirección horizontal)
    DY = dy_dx(X_field, Y_field)    # Componente y según la ecuación diferencial

    # Normalización para que todas las flechas tengan la misma longitud
    M = np.sqrt(DX**2 + DY**2)      # Magnitud del vector
    DX_norm = DX / M                # Componente x normalizada
    DY_norm = DY / M                # Componente y normalizada

    # VISUALIZACIÓN DEL CAMPO DE PENDIENTES
    fig, (ax1) = plt.subplots(1, 1, figsize=(10, 8))
    ax1.quiver(X_field, Y_field, DX_norm, DY_norm, 
            M, scale=30, alpha=0.7, cmap='viridis', width=0.003)
    # - quiver: dibuja flechas en cada punto de la malla
    # - M: colorea las flechas según la magnitud de la pendiente
    # - scale=30: controla el tamaño de las flechas
    # - alpha=0.7: transparencia del 70%

    # 2. MÉTODO DE LAS ISOCLINAS CORREGIDO
    # Las isoclinas son curvas donde la pendiente es constante
    # Para y' = 0.12x² + 0.6x, las isoclinas son: 0.12x² + 0.6x = k
    # Esta es independiente de y, así que son líneas horizontales y = constante

    # 3. TRAZADO DE SOLUCIÓN USANDO ISOCLINAS
    def isocline_method(x0, y0, x_target, step_size=0.5):
        """
        Método gráfico que sigue las pendientes del campo para trazar una solución
        Es esencialmente un método de Euler con pasos constantes
        """
        x_values = [x0]
        y_values = [y0]
        
        x_current = x0
        y_current = y0
        
        # Determina si avanzar hacia adelante o atrás en x
        direction = 1 if x_target > x0 else -1
        step = step_size * direction
        
        # Itera hasta llegar cerca del objetivo
        while (direction == 1 and x_current < x_target) or (direction == -1 and x_current > x_target):
            # Calcula la pendiente en el punto actual
            slope = dy_dx(x_current, y_current)
            
            # Avanza un paso usando la pendiente actual
            x_next = x_current + step
            y_next = y_current + slope * step  # Fórmula de Euler: y_{n+1} = y_n + h*f(x_n, y_n)
            
            x_values.append(x_next)
            y_values.append(y_next)
            
            x_current = x_next
            y_current = y_next
            
            # Protección contra bucles infinitos
            if len(x_values) > 1000:
                break
        
        return np.array(x_values), np.array(y_values)

    # EJECUCIÓN DEL MÉTODO
    x_iso_sol, y_iso_sol = isocline_method(0, 0, 10, step_size)

    # Encuentra y(-4) por interpolación lineal
    y_at_neg4_isocline = np.interp(10, x_iso_sol, y_iso_sol)

    # Agregar la solución exacta al gráfico
    x_exact = np.linspace(x_min, x_max, 100)
    y_exact = exact_solution(x_exact)
    ax1.plot(x_exact, y_exact, 'g-', linewidth=3, label='Solución exacta', alpha=0.8)

    # Valor exacto en x = 10
    y_exact_at_neg4 = exact_solution(10)

    # VISUALIZACIÓN FINAL
    ax1.plot(x_iso_sol, y_iso_sol, 'ro-', linewidth=3, markersize=4, 
            label='Solución por Isoclinas', alpha=0.8)
    ax1.plot(0, 0, 'go', markersize=10, label='Punto inicial (0, 0)')
    ax1.plot(10, y_at_neg4_isocline, 'ro', markersize=10, 
            label=f'y(10) ≈ {y_at_neg4_isocline:.3f} (Isoclinas)')
    ax1.plot(10, y_exact_at_neg4, 'gs', markersize=10, 
            label=f'y(10) = {y_exact_at_neg4:.3f} (Exacta)')

    ax1.set_xlim(x_min, x_max)
    ax1.set_ylim(y_min, y_max)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Campo de Pendientes y Soluciones para y\' = 0.12x² + 0.6x')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    print(f"Solución exacta en x = 10: y = {y_exact_at_neg4:.6f}")
    print(f"Solución por isoclinas en x = 10: y ≈ {y_at_neg4_isocline:.6f}")
    print(f"Error absoluto: {abs(y_exact_at_neg4 - y_at_neg4_isocline):.6f}")
