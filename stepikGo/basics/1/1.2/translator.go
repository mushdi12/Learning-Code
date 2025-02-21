package main

import "fmt"

func main() {
	var input string
	fmt.Scan(&input)

	switch input {
	case "en":
		fmt.Println("English")
	case "fr":
		fmt.Println("French")
	case "rus", "ru":
		fmt.Println("Russian")
	default:
		fmt.Println("Unknown")

	}
}
