package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	data, _ := reader.ReadString('\n')

	lines := strings.Fields(data)

	for i, w := range lines {
		runes := []rune(w)

		if len(runes) > 0 {
			// Первую букву делаем заглавной
			runes[0] = unicode.ToUpper(runes[0])

			// Остальные буквы делаем строчными
			for j := 1; j < len(runes); j++ {
				runes[j] = unicode.ToLower(runes[j])
			}
		}

		lines[i] = string(runes)
	}

	result := strings.Join(lines, " ")

	fmt.Println(result)
}