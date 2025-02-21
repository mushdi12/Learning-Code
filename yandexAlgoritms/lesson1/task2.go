package main

import "fmt"

var a, b, c int

func readSide() {
	_, err := fmt.Scan(&a, &b, &c)

	if err != nil {
		fmt.Print(err)
		return
	}
}

func main() {
	readSide()

	if (a+b > c) && (a+c > b) && (b+c > a) {
		fmt.Print("YES")
	} else {
		fmt.Print("NO")
	}

}
