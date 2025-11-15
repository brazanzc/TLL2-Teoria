# 🧪 Comparación de Algoritmos de Ordenamiento  
### Análisis Empírico de Complejidad Temporal (Bubble Sort, Merge Sort y Quick Sort)

Este proyecto implementa y compara tres algoritmos clásicos de ordenamiento —**Bubble Sort**, **Merge Sort** y **Quick Sort**— mediante un benchmark experimental que evalúa su rendimiento sobre listas de distintos tamaños. Finalmente, los resultados se visualizan en un gráfico generado con `matplotlib`.

---

## 📌 Objetivos del Proyecto

- Implementar algoritmos de ordenamiento desde cero.
- Medir su rendimiento real usando listas aleatorias.
- Comparar el comportamiento empírico frente a su complejidad teórica.
- Generar un gráfico visual que contraste las diferencias de desempeño.

---

## 🛠️ Tecnologías utilizadas

- Python 3
- matplotlib
- random
- time
- copy

---

## 📚 Algoritmos Implementados

### 🔴 Bubble Sort — *O(n²)*
Método iterativo simple basado en intercambios consecutivos.

### 🔵 Merge Sort — *O(n log n)*
Estrategia de división y conquista, implementada de forma recursiva.

### 🟢 Quick Sort — *O(n log n) promedio*
Divide la lista según un pivote y ordena recursivamente cada partición.

---

## 🚀 Ejecución del Experimento

El programa:

1. Genera listas aleatorias de distintos tamaños.  
2. Ejecuta cada algoritmo sobre la misma lista base.  
3. Mide tiempos de ejecución.  
4. Genera un gráfico comparativo (`comparacion_algoritmos.png`).  

### Para ejecutar:

```bash
python main.py
