package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func readNumber() string {
	reader := bufio.NewReader(os.Stdin)

	input_number, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println(err)
		return ""
	}

	input_number = strings.TrimSpace(input_number)
	answer := strings.NewReplacer("+", "", "-", "", "(", "", ")", "").Replace(input_number)
	if string(answer[0]) != "7" && string(answer[0]) != "8" {
		answer = "495" + answer
		return answer
	}
	return answer[1:]
}

func main() {

	writer := bufio.NewWriter(os.Stdout)

	var book_number, result string
	added_number := readNumber()
	//fmt.Print(added_number)

	for i := 1; i <= 3; i++ {
		book_number = readNumber()
		if book_number == added_number {
			result += "YES\n"
		} else {
			result += "NO\n"
		}
	}
	_, err := writer.WriteString(result)

	err = writer.Flush()
	if err != nil {
		panic(err)
	}

}
