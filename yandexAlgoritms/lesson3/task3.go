package main

import (
	"fmt"
	"sort"
	"strconv"
)

func getCountsAndColors(a_b []int, a_lim int) {

	hashMap := make(map[int]int)

	for _, value := range a_b {
		hashMap[value]++
	}

	both_cnt := 0
	var both_result string
	for key, value := range hashMap {
		if value > 1 {
			both_cnt += 1
			both_result += strconv.Itoa(key)
			both_result += " "
		}
	}

	a_result, a_cnt := packagingResults(hashMap, a_b[:a_lim])
	b_result, b_cnt := packagingResults(hashMap, a_b[a_lim:])

	fmt.Println(both_cnt)
	fmt.Println(both_result)
	fmt.Println(a_cnt)
	fmt.Println(a_result)
	fmt.Println(b_cnt)
	fmt.Println(b_result)

}
func packagingResults(curr_map map[int]int, curr_msv []int) (string, int) {
	curr_cnt := 0
	var result string
	sort.Ints(curr_msv)
	for _, value := range curr_msv {
		if curr_map[value] < 2 {
			curr_cnt += 1
			result += strconv.Itoa(value)
			result += " "
		}
	}
	return result, curr_cnt
}

func main() {
	var a_b []int
	var a_count, b_count int
	fmt.Scan(&a_count, &b_count)

	i := 0
	var number int
	for i < a_count+b_count {
		fmt.Scan(&number)
		a_b = append(a_b, number)
		i++
	}
	fmt.Println("=======================")
	getCountsAndColors(a_b, a_count)

}
