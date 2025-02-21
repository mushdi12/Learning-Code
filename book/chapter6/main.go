package main

import (
	"fmt"
)

func swap(x *int, y *int) {
	a := *x
	*x = *y
	*y = a

}

func main() {
	x := 1
	y := 2
	fmt.Println("Изначальное значение x:", x, "y:", y)
	swap(&x, &y)
	fmt.Println("Полученное значение x:", x, "y:", y)
}
