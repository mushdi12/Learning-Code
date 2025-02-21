package main

import (
	"fmt"
)

func createPrefSum(msv []int) []int {
	result := make([]int, len(msv))

	for i := 1; i < len(msv); i++ {
		result[i] = msv[i-1] + result[i-1]
	}

	return result
}

func getIntervalSum(prefix_sum []int, l, r int) int { // если индексы с 0, то сумма [l;r) если с 1 то (l;r]
	return prefix_sum[r] - prefix_sum[l]
}

func getCoupleCnt(msv []int, k int) int { //метод 2 указателей
	right := 0
	result := 0
	for left := 0; left < len(msv); left++ {
		for right < len(msv) && msv[right]-msv[left] <= k {
			right++
		}
		result += len(msv) - right
	}
	return result
}

func main() {
	num := []int{1, 3, 6, 8, 5, 4, 9, 4, 5}

	prefix_sum := createPrefSum(num)

	left := 2

	right := 4

	interval := getIntervalSum(prefix_sum, left, right)

	fmt.Println("Numbers: ", num)
	fmt.Println("Prefix sum: ", prefix_sum)
	fmt.Println("Sum numbers [2,4) :", interval)

	// Дана отсортированная последовательность чисел длиной N и число K
	// нужно найти количество пар чисел таких что их ранзность > K

	data := []int{1, 3, 7, 8}

	k := 4

	fmt.Println("Data: ", data)
	fmt.Println("Couple's count: ", getCoupleCnt(data, k))

}
