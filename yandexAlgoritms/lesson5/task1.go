package main

import (
	"fmt"
	"math"
)

func inputData() []int {
	var n int
	fmt.Scan(&n)
	result := make([]int, n)

	for i := 0; i < n; i++ {
		var element int
		fmt.Scan(&element)
		result[i] = element
	}
	return result
}

func binSearchM(f_num int, msv []int) int {
	l := 0
	r := len(msv) - 1
	for l+1 < r {
		m := (l + r) / 2
		if msv[m] > f_num {
			r = m
		} else {
			l = m
		}
	}

	if math.Abs(float64((msv[l])-f_num)) < math.Abs(float64((msv[r])-f_num)) {
		return msv[l]
	}

	return msv[r]
}

func getCnt(mk, sh []int) (int, int) {
	var mka, shorts int
	difference := 100000.0
	for i := 0; i < len(mk); i++ {
		curr_shorts := binSearchM(mk[i], sh)
		//fmt.Println("Mayka :", mk[i], " Shorty :", curr_shorts)
		curr_dif := math.Abs(float64(curr_shorts) - float64(mk[i]))

		if curr_dif < difference {
			mka = mk[i]
			shorts = int(curr_shorts)
			difference = curr_dif
		}
	}
	return mka, shorts
}

func main() {
	shirts := inputData()
	shorts := inputData()
	fmt.Println(getCnt(shirts, shorts))
}
