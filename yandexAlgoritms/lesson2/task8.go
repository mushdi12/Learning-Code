package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func findMax3Composition(ms []int) (int, int, int) {
	sort.Ints(ms)
	var result []int

	if len(ms) == 3 {
		result = append(result, ms[0], ms[1], ms[2])

	} else {
		if ms[0]*ms[1]*ms[len(ms)-1] > ms[len(ms)-1]*ms[len(ms)-2]*ms[len(ms)-3] {
			result = append(result, ms[0], ms[1], ms[len(ms)-1])
		} else {
			result = append(result, ms[len(ms)-1], ms[len(ms)-2], ms[len(ms)-3])
		}
	}

	sort.Ints(result)
	return result[0], result[1], result[2]
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
	fmt.Print(findMax3Composition(a))

}
