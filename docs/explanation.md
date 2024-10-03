# Explicación

Los métodos de Runge-Kutta son métodos genéricos iterativos, explicitos e implicitos, para la aproximación de soluciones de ecuaciones diferenciales ordinarias, concretamente, del problema de valor inicial.

El método de Runge-Kutta de cuarto orden o también conocido como RK4, así como lo dice el nombre, es un método para la resolución de ecuaciones diferenciales de orden 4.

Si tenemos un problema de valor inicial como:

$$ y' = f(x,y)  con   y(x_0) = y_0 $$

Entonces el método RK4 para este problema está dado por la siguiente ecuación:

$$  y_{i+1} = y_i + frac{1}{6}h (k_1 + 2k_2 + 2k_3 + k_4) $$

Donde:

$$
\left\{
    \begin{aligned}
        & k_1 = f(x_i, y_i) \\
        & k_2 = f(x_i + \frac{1}{2}h, y_i + \frac{1}{2}k_1h)\\
        & k_3 = f(x_i + \frac{1}{2}h, y_i + \frac{1}{2}k_2h)\\
        & k_4 = f(x_i + h, y_i + k_3h)
    \end{aligned}
\right.
$$

Esta forma del método de Runge-Kutta, es un método de cuarto orden lo cual significa que el error por paso es del orden de O(H⁵), mientras que el error acumulado tiene el orden O(h⁴). Por lo tanto, la convergencia es de orden O(h⁴), razón por la cual es usado en los métodos computacionales.

