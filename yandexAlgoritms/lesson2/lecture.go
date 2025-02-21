package main

import "fmt"

func findMax(ms []int) int {
	max_index := 0
	for i := 1; i < len(ms); i++ {
		if ms[max_index] < ms[i] {
			max_index = i
		}
	}
	return ms[max_index]
}

func find2Max(ms []int) (int, int) {
	first_max := max(ms[0], ms[1])
	second_max := min(ms[0], ms[1])
	for i := 2; i < len(ms); i++ {
		if ms[i] > first_max {
			second_max = first_max
			first_max = ms[i]
		} else if ms[i] > second_max {
			second_max = ms[i]
		}
	}

	return first_max, second_max
}

func findMinEven(ms []int) int {
	// flag := false
	min := -1
	for i := 0; i < len(ms); i++ {
		if ms[i]%2 == 0 && (min == -1 || ms[i] < min) { // (!flag || ms[i] < min)  <-- для универсальности
			min = ms[i]
			// flag := true
		}
	}
	return min
}

func findMinWords(ms []string) []string {
	min_word := len(ms[0])
	for i := 1; i < len(ms); i++ {
		if len(ms[i]) < min_word {
			min_word = len(ms[i])
		}
	}
	min_words := []string{}

	for i := 0; i < len(ms); i++ {
		if len(ms[i]) == min_word {
			min_words = append(min_words, ms[i])
		}
	}
	return min_words
}

func findWaterCount(ms []int) int {
	heap := 0
	for i := 1; i < len(ms); i++ {
		if ms[i] > ms[heap] {
			heap = i
		}
	}
	water_sum := 0
	now_heap := 0
	for i := 0; i < heap; i++ {
		if ms[i] > now_heap {
			now_heap = ms[i]
		}
		water_sum += now_heap - ms[i]
	}

	now_heap = 0
	for i := len(ms) - 1; i > heap; i-- {
		if ms[i] > now_heap {
			now_heap = ms[i]
		}
		water_sum += now_heap - ms[i]
	}
	return water_sum
}

func main() {
	a := []int{6, 1, 2, 3, 4, 3, 54, 7, 43, 2, 55, 7}
	b := []string{"123", "321", "2", "32", "3"}
	c := []int{3, 1, 4, 3, 5, 1, 1, 7, 3, 1}

	fmt.Println("=====First Task=====")
	fmt.Println("Maximum: ", findMax(a))

	fmt.Println("  ")

	fmt.Println("=====Second Task====")
	first_max, second_max := find2Max(a)
	fmt.Println("First Maximum: ", first_max)
	fmt.Println("Second Maximum: ", second_max)

	fmt.Println("  ")

	fmt.Println("=====Third Task=====")
	fmt.Println("Minimum: ", findMinEven(a))

	fmt.Println("  ")

	fmt.Println("=====Fourth Task=====")
	fmt.Println("Minimum words: ", findMinWords(b))

	fmt.Println("  ")

	fmt.Println("=====Fourth Task=====")
	fmt.Println("Count of water blocks: ", findWaterCount(c))

}
