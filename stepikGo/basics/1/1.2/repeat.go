package main

import "fmt"

func main() {
	var line, result string
	var cnt int
	fmt.Scan(&line, &cnt)

	for cnt > 0 {
		result += line
		cnt--
	}

	fmt.Println(result)
}
