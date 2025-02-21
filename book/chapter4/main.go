package main

import "fmt"

func findMin() {
	x := []int{48, 96, 86, 68,
		57, 82, 63, 70,
		37, 34, 83, 27,
		19, 97, 9, 17}
	minimum := 1000

	for _, element := range x {
		if minimum > element {
			minimum = element
		}
	}
	fmt.Println(minimum)
}

func main() {
	findMin()
	var i = 0
	for i < 10 {
		fmt.Print(i)
		fmt.Print(" ")
		i++
	}
	for i := 0; i < 10; i++ {
	}
}
