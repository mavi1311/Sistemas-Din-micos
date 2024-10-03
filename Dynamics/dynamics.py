# Dynamics/dynamics.py

"""Proporciona funciones para resolver sistemas dinámicos.

ESte módulo permite al usiario realizar simulaciones de sistemas dinamicos mediantes métodos matemáticos, utilizando operadores y estados iniciales.

Este módulo contiene las siguientes funciones:

- `dyn_generator(oper, state)` - Genera la función del estado inicial.
- `rk4(func, oper, state, h)` - Genera el resultado al problema del valor inicial por el metodo RK4.
"""
def dyn_generator(oper, state):
    """ Genera una función  del problema del valor inicial.

    Examples:
        >>> import numpy as np
        >>> operador = np.array([[0,1],[1,0]])
        >>> print(operador)
        [[0 1]
         [1 0]]
        >>> yinicial = np.array([[1,0],[0,0]])
        >>> print(yinicial)
        [[1 0]
         [0 0]]
        >>> prueba = dyn_generator(operador, yinicial)
        >>> print(test)
        [[0.-0j 0.+1j]
         [0.-1j 0.-0j]]
    
    Args:
        oper (tuple): El operador de la función.
        state (tuple): El estado inicial de la función.

    Returns:
        (tuple): El resultado de la función: (-1.0j)*(np.dot(oper,state)-np.dot(state,oper))
   """
    return (-1.0j)*(np.dot(oper,state)-np.dot(state,oper))

def rk4(func, oper, state, h):
    """ Genera la función del metodo RK4

    Examples:
        >>> import numpy as np
        >>> times = np.linspace(0.0,10.0,30)
        print(times)
        [ 0.          0.34482759  0.68965517  1.03448276  1.37931034  1.72413793 ... 8.27586207  8.62068966  8.96551724  9.31034483  9.65517241 10.        ]
        >>> h = times[1] - times [0]
        >>> operador = np.array([[0,1],[1,0]])
        >>> yinicial = np.array([[1,0],[0,0]])
        >>> resultado = rk4(dyn_generator, operador, yinicial, h)
        print(resultado)
        [[0.88580682+0.j         0.        +0.31749286j] [0.        -0.31749286j 0.11419318+0.j        ]][[0.59609037+0.j         0.        +0.48996364j] ....  [[0.38519955+0.j         0.        +0.47591116j]  [0.        -0.47591116j 0.61480045+0.j        ]]
    
    Args:
        func (tuple):  Función del problema de valor inicial. 
        oper (tuple): El operador de la función de valor inicial.
        state (tuple): El estado inicial de la función.
        h (float): Es el incremento temporal entre cada tiempo.

    Returns:
        (tuple): Nos da una tupla con los resultados de todos los valores del sistema dinámico

    """
    return state + 1/(6) * (k_1 + 2 * k_2 + 2* k_3 + k_4)



