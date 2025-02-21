package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

func mostCountWord(input []string) string {
	dict := make(map[string]int)

	for _, value := range input {
		dict[value] += 1
	}

	max := 0
	var max_word string
	var a []string
	for key, value := range dict {
		if value > max {
			max = value
			max_word = key
		} else if value == max {
			a = append(a, key)
		}
	}
	a = append(a, max_word)

	sort.Strings(a)

	return a[0]
}

func main() {

	reader := bufio.NewReader(os.Stdin)

	input, _ := reader.ReadString('\n')
	input = strings.TrimSpace(input)
	strings_msv := strings.Fields(input)

	fmt.Print(mostCountWord(strings_msv))
}
