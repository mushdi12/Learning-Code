package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func findNearNumber(orig_number int, ms []int) int {

	dif := math.Abs(float64(orig_number) - float64(ms[0]))
	result := ms[0]

	for i := 1; i < len(ms); i++ {
		if math.Abs(float64(orig_number)-float64(ms[i])) < dif {
			result = ms[i]
			dif = math.Abs(float64(orig_number) - float64(ms[i]))
		}
	}

	return result
}

func main() {
	var n, orig_number int

	fmt.Scan(&n)

	var a []int
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')

	input = strings.TrimSpace(input)
	strNumbers := strings.Fields(input)

	for i := 0; i < len(strNumbers); i++ {
		num, _ := strconv.Atoi(string(strNumbers[i]))
		a = append(a, num)
	}

	fmt.Scan(&orig_number)

	fmt.Println(findNearNumber(orig_number, a))
}
