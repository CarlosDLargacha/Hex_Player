Implementación del juador HEX

- **Algoritmo principal**: Usa Minimax con poda alfa-beta para explorar el árbol de juego, limitado por un tiempo máximo de ejecución (`time_limit`). Implementa Iterative Deepening para incrementar progresivamente la profundidad de búsqueda.

- **Optimizaciones clave**:
  - *Ordenamiento de movimientos*: Prioriza movimientos estratégicos usando heurísticas de conexión de lados, bloqueo de oponentes y control del centro.
  - *Libro de aperturas*: Contiene movimientos predefinidos para tamaños comunes de tablero (7x7 y 11x11) que se usan en las primeras jugadas.
  - *Evaluación adaptativa*: Combina múltiples factores estratégicos en la función de evaluación: distancia potencial a la victoria, conteo de puentes, y control posicional.

- **Mecanismos de evaluación**:
  1. Calcula distancias mínimas de conexión usando BFS optimizado
  2. Evalúa puentes potenciales (posiciones vacías que conectan múltiples piezas)
  3. Mide control estratégico con ponderación por posición central y conexiones adyacentes

- **Gestión de recursos**:
  - Sistema de timeout con margen de seguridad del 15%
  - Límite máximo de profundidad dinámico (`max_depth = size * 2`)
  - Estadísticas de seguimiento de nodos evaluados y podas realizadas

- **Estructuras de datos**:
  - Clonado de tableros para simulación de jugadas
  - Historial de movimientos y caché de parámetros de optimización
  - Cola de doble extremo (deque) para implementación eficiente de BFS
