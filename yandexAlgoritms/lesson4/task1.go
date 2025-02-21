package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func foundChar(dict map[string]string, word string) string {
	var value string
	var exist bool
	if value, exist = dict[word]; !exist {
		for keys, words := range dict {
			if word == words {
				value = keys
			}
		}
	}

	return value
}

func main() {

	var count int
	var word string
	fmt.Scan(&count)

	reader := bufio.NewReader(os.Stdin)

	dict := make(map[string]string)

	i := 0
	for i < count {
		input, _ := reader.ReadString('\n')
		input = strings.TrimSpace(input)
		strings_msv := strings.Fields(input)
		dict[strings_msv[0]] = strings_msv[1]
		i++
	}

	fmt.Scan(&word)

	fmt.Print(foundChar(dict, word))
}
