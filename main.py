import random
import time
import sys
import matplotlib.pyplot as plt
import copy

# ==========================================
# PARTE 1: IMPLEMENTACIÓN DE ALGORITMOS
# ==========================================

def bubble_sort(arr):
    """
    Algoritmo 1: Bubble Sort
    Complejidad Teórica: O(n^2)
    Enfoque: Iterativo simple.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):
    """
    Algoritmo 2: Merge Sort
    Complejidad Teórica: O(n log n)
    Enfoque: División y Conquista (Recursivo).
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Proceso de mezcla (Merge)
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    """
    Algoritmo 3: Quick Sort
    Complejidad Teórica: O(n log n) promedio.
    Enfoque: División y Conquista (Pivote).
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# ==========================================
# PARTE 2: MOTOR DE PRUEBAS (BENCHMARK)
# ==========================================

def run_experiment():
    # Aumentamos el límite de recursión para listas grandes en Quick/Merge Sort
    sys.setrecursionlimit(20000)
    
    # Tamaños de lista a probar (N)
    # Nota: Bubble Sort es muy lento, mantenemos N razonable (< 5000)
    sizes = [100, 500, 1000, 1500, 2000, 2500, 3000]
    
    times_bubble = []
    times_merge = []
    times_quick = []

    print(f"{'N':<10} | {'Bubble (s)':<12} | {'Merge (s)':<12} | {'Quick (s)':<12}")
    print("-" * 55)

    for n in sizes:
        # Generar lista aleatoria base para este tamaño
        base_arr = [random.randint(0, 10000) for _ in range(n)]
        
        # Copias para que cada algoritmo ordene la misma lista desordenada
        arr1 = copy.deepcopy(base_arr)
        arr2 = copy.deepcopy(base_arr)
        arr3 = copy.deepcopy(base_arr)

        # 1. Medir Bubble Sort
        start = time.time()
        bubble_sort(arr1)
        end = time.time()
        t_bubble = end - start
        times_bubble.append(t_bubble)

        # 2. Medir Merge Sort
        start = time.time()
        merge_sort(arr2)
        end = time.time()
        t_merge = end - start
        times_merge.append(t_merge)

        # 3. Medir Quick Sort
        start = time.time()
        quick_sort(arr3)
        end = time.time()
        t_quick = end - start
        times_quick.append(t_quick)

        print(f"{n:<10} | {t_bubble:.6f}     | {t_merge:.6f}     | {t_quick:.6f}")

    return sizes, times_bubble, times_merge, times_quick

# ==========================================
# PARTE 3: GENERACIÓN DE GRÁFICOS
# ==========================================

def plot_results(sizes, t_bubble, t_merge, t_quick):
    plt.figure(figsize=(10, 6))
    
    plt.plot(sizes, t_bubble, marker='o', label='Bubble Sort O(n^2)', color='red')
    plt.plot(sizes, t_merge, marker='s', label='Merge Sort O(n log n)', color='blue')
    plt.plot(sizes, t_quick, marker='^', label='Quick Sort O(n log n)', color='green')

    plt.title('Comparación de Complejidad Temporal: Algoritmos de Ordenamiento')
    plt.xlabel('Tamaño de la entrada (N)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.legend()
    plt.grid(True)
    
    # Guardar gráfico para el informe
    plt.savefig('comparacion_algoritmos.png')
    print("\n[Info] Gráfico guardado como 'comparacion_algoritmos.png'")
    plt.show()

if __name__ == "__main__":
    print("Iniciando investigación aplicada de algoritmos...\n")
    sizes, t_b, t_m, t_q = run_experiment()
    plot_results(sizes, t_b, t_m, t_q)
