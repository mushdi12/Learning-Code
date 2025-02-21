package main

import (
	"fmt"
)
import m "education/math"

func main() {
	xs := []float64{2, 4}
	avg := m.Average(xs)
	min := m.Min(xs)
	max := m.Max(xs)
	fmt.Println("Max:", max)
	fmt.Println("Min:", min)
	fmt.Println("Average:", avg)
}
