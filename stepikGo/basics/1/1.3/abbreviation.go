package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

func main() {
	phrase := readString()
	phrase_msv := strings.Fields(phrase)
	var abbr string
	for _, dig := range phrase_msv {
		runes := []rune(dig) // нужно сделать именно так а не просто dig[0] - так оно берет первый байт, а не символ
		firstLetter := runes[0]
		if unicode.IsLetter(firstLetter) {
			abbr += string(unicode.ToUpper(firstLetter))
		}

	}

	fmt.Println(abbr)
}

func readString() string {
	rdr := bufio.NewReader(os.Stdin)
	str, _ := rdr.ReadString('\n')
	return str
}
