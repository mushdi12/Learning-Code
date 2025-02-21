package main

import "fmt"

func main() {

	x := [5]int{
		1,
		1,
		1,
		1,
		1,
	}
	total := 1
	for _, value := range x { //позваляет обращаться к копиям,
		total += value // а не к самим значениям
	}
	fmt.Println(x)
	y := x[0:3]
	slice1 := []int{1, 2, 3}
	slice2 := append(slice1, 4, 5)
	fmt.Println(slice1, slice2)
	fmt.Println(y)
	fmt.Println(total)

}
