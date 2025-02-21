package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func originCount(ms []int) int {
	count := 0
	hashMap := make(map[int]int)

	for _, value := range ms {
		if _, exists := hashMap[value]; !exists {
			hashMap[value] = 1
		}
	}

	//fmt.Print(hashMap)

	for _, value := range hashMap {
		count += value
	}

	return count
}

func main() {
	var data []int
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')

	input = strings.TrimSpace(input)
	input_msv := strings.Fields(input)

	for i := 0; i < len(input_msv); i++ {
		curr_num, _ := strconv.Atoi(input_msv[i])
		data = append(data, curr_num)
	}

	fmt.Println(originCount(data))
}
