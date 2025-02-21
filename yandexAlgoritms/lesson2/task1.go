package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func isIncreasing(ms []int) string {
	for i := 0; i < len(ms)-1; i++ {
		if ms[i] >= ms[i+1] {
			return "NO"
		}
	}
	return "YES"
}

func main() {
	a := []int{}

	reader := bufio.NewReader(os.Stdin)
	input, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println(err)
	}

	input = strings.TrimSpace(input)

	strNumbers := strings.Fields(input)

	for i := 0; i < len(strNumbers); i++ {
		num, _ := strconv.Atoi(string(strNumbers[i]))
		a = append(a, num)
	}
	fmt.Print(isIncreasing(a))
}
