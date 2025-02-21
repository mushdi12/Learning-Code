package main

import "fmt"

func main() {
	var text, result string
	var len_text int

	fmt.Scan(&text, &len_text)

	if len_text >= len(text) {
		result = text
	} else {
		result = text[:len_text] + "..."
	}

	fmt.Println(result)
}
