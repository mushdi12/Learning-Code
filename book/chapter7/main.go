package main

import "fmt"

type Triangle struct {
	a float64
	b float64
	c float64
}

type Square struct {
	a float64
	b float64
}

type Shape interface {
	perimeter() float64
}

func (t Triangle) perimeter() float64 {
	return t.a + t.b + t.c
}

func (s Square) perimeter() float64 {
	return s.a*2 + s.b*2
}

func totalPerimeter(shapes ...Shape) float64 {
	var total float64
	for _, shape := range shapes {
		total += shape.perimeter()
	}
	return total
}

func (t Triangle) toString() {
	fmt.Println("Triangle - a:", t.a, "b:", t.b, "c:", t.c)
}

func (s Square) toString() {
	fmt.Println("Square - a:", s.a, "b:", s.b)
}

func main() {
	triangle := Triangle{1, 2, 3}
	square := Square{4, 5}
	triangle.toString()
	square.toString()
	fmt.Println("Triangle sum:", triangle.perimeter())
	fmt.Println("Square sum:", square.perimeter())
	fmt.Println("Sum :", totalPerimeter(triangle, square))

}
