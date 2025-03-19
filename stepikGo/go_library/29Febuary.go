package main

import (
	"testing"
	"time"
)

// начало решения

func isLeapYear(year int) bool {
	days := time.Now().YearDay()
	if 
	return false
}

// конец решения

func Test(t *testing.T) {
	if !isLeapYear(2020) {
		t.Errorf("2020 is a leap year")
	}
	if isLeapYear(2022) {
		t.Errorf("2022 is NOT a leap year")
	}
}
