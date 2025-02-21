package main

import "fmt"

func CountingSort(arr []int) []int {
	if len(arr) == 0 {
		return arr
	}

	max, min := arr[0], arr[0]
	for _, value := range arr {
		if value > max {
			max = value
		}
		if value < min {
			min = value
		}
	}

	count := make([]int, max-min+1)

	for _, value := range arr {
		count[value-min]++
	}

	index := 0
	for i, freq := range count {
		for freq > 0 {
			arr[index] = i + min
			index++
			freq--
		}
	}

	return arr
}

func main() {
	arr := []int{4, 2, 2, 8, 3, 3, 1, 5}
	fmt.Println("Исходный массив:", arr)

	sortedArr := CountingSort(arr)
	fmt.Println("Отсортированный массив:", sortedArr)
}
