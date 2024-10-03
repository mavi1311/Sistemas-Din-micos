## Sistemas dinámicos 

Los sistemas dinámicos son modelos que intentan resolver la trayectoria temporal de alguna cantidad física como función de algún generador dinámico.

En algunos casos se puede modelar la dinámica de un estado genérico y mediante la ecuación dinámica:

$$\frac{dy}{dt} =f(t,y)$$

Bajo la condición inicial:

$$ y(t_0) = y_0 $$

Siendo "t" la variable temporal y "y" un estado del sistema, este estado se puede representar mediante diferentes objetos matemáticos: desde cantidades escalares hasta matrices que representan cierto operador lineal.

El problema dinámico descrito anteriormente es usualmente conocido en el campo de las matemáticas aplicadas como problema de condición inicial.

En esta página vamos demostrar cómo utilizar el método Runge-Kutta de orden 4 o en forma breve RK4 para resolver problemas de valores iniciales de orden 4.


