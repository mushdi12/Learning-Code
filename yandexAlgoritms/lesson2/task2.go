package main

import "fmt"

func checker(ms []int) string {
	if checkCONSTANT(ms) {
		return "CONSTANT"
	} else if checkASCENDING(ms) {
		return "ASCENDING"
	} else if checkWEAKLY_ASCENDING(ms) {
		return "WEAKLY ASCENDING"
	} else if checkDESCENDING(ms) {
		return "DESCENDING"
	} else if checkWEAKLY_DESCENDING(ms) {
		return "WEAKLY DESCENDING"
	}
	return "RANDOM"
}

func checkCONSTANT(ms []int) bool {
	for i := 1; i < len(ms); i++ {
		if ms[i] != ms[0] {
			return false
		}
	}
	return true
}

func checkASCENDING(ms []int) bool {
	for i := 0; i < len(ms)-1; i++ {
		if ms[i] >= ms[i+1] {
			return false
		}
	}
	return true
}

func checkWEAKLY_ASCENDING(ms []int) bool {
	for i := 0; i < len(ms)-1; i++ {
		if ms[i] > ms[i+1] {
			return false
		}
	}
	return true
}

func checkDESCENDING(ms []int) bool {
	for i := 0; i < len(ms)-1; i++ {
		if ms[i] <= ms[i+1] {
			return false
		}
	}
	return true
}

func checkWEAKLY_DESCENDING(ms []int) bool {
	for i := 0; i < len(ms)-1; i++ {
		if ms[i] < ms[i+1] {
			return false
		}
	}
	return true
}

func main() {
	var input_msv []int

	for true {
		var number int

		fmt.Scan(&number)
		if number == -2000000000 {
			break
		}
		input_msv = append(input_msv, number)

	}

	fmt.Print(checker(input_msv))
}
