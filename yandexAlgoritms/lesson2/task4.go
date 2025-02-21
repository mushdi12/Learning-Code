package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func findBiggerNeigh(ms []int) int {
	count := 0
	for i := 1; i < len(ms)-1; i++ {
		if ms[i] > ms[i-1] && ms[i] > ms[i+1] {
			count += 1
		}
	}
	return count
}

func main() {
	var a []int
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')

	input = strings.TrimSpace(input)
	input_msv := strings.Fields(input)

	for i := 0; i < len(input_msv); i++ {
		num, _ := strconv.Atoi(input_msv[i])
		a = append(a, num)
	}

	fmt.Println(findBiggerNeigh(a))
}
