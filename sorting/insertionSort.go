package main

import "fmt"

//сортировка вставками работает через O(n^2) - худший случай

func insertionSort(arr []int) {
	for i := 1; i < len(arr); i++ { //начинаем с 1 элемента, а не с 0-ого
		key := arr[i] // <-текущий элемент
		j := i - 1    // индекс предыдущего элемента

		for j >= 0 && key < arr[j] { // т.е если у нас предыдущий элемент > текущего
			arr[j+1] = arr[j]
			j--
		}
		arr[j+1] = key
	}
}
func countTransposition(ms []int) int {
	k := 0
	for i := 1; i < len(ms); i++ {
		key := ms[i]
		j := i - 1
		for j >= 0 && ms[j] > key {
			k += 1 // <-тут
			ms[j+1] = ms[j]
			j--
		}
		ms[j+1] = key // здесь не считаем k+=1 так как мы уже учитываем эту перестановку для 1 см (тут)
	}
	return k
}

func main() {
	array := []int{7, 2, 5, 1, 67, 0}
	fmt.Println("Array before sorting:", array)
	insertionSort(array)
	fmt.Println("Array after sorting:", array)
	count := countTransposition(array)
	fmt.Println("Count array's transposition:", count)
}
