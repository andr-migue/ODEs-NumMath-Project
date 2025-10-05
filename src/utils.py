import numpy as np
from matplotlib import pyplot as pyplot

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
