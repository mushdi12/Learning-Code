package main

import "fmt"

func main() {
	var a, b, c int
	fmt.Scan(&a, &b, &c)
	//fmt.Print(a, b, c)

	if c < 0 {
		fmt.Print("NO SOLUTION")
		return
	}

	if a == 0 {
		if b == c*c {
			fmt.Println("MANY SOLUTIONS")
		} else {
			fmt.Println("NO SOLUTION")
		}
		return
	}

	if (c*c-b)%a != 0 {
		fmt.Println("NO SOLUTION")
		return
	}

	x := (c*c - b) / a

	if a*x+b < 0 {
		fmt.Print("NO SOLUTION")
		return
	} else {
		fmt.Print(x)
	}

}
