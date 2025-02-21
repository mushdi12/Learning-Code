package math

import "testing"

type testCase struct {
	values  []float64
	average float64
}

var tests = []testCase{
	{[]float64{1, 2, 3, 4, 5}, 3},
	{[]float64{1, 2}, 1.5},
	{[]float64{1, 1, 1, 1, 1, 1}, 1},
	{[]float64{-1, 1}, 0},
}

var minTests = []testCase{
	{[]float64{1, 2, 3, 4, 5}, 1},
	{[]float64{1, 2}, 1},
	{[]float64{1, 1, 1, 1, 1, 1}, 1},
	{[]float64{-1, 1}, -1},
}

var maxTests = []testCase{
	{[]float64{1, 2, 3, 4, 5}, 5},
	{[]float64{1, 2}, 2},
	{[]float64{1, 1, 1, 1, 1, 1}, 1},
	{[]float64{-1, 1}, 1},
}

func TestAverage(t *testing.T) {
	for _, pair := range tests {
		v := Average(pair.values)
		if v != pair.average {
			t.Error(
				"Failed",
				"For", pair.values,
				"expected", pair.average,
				"got", v,
			)
		} else {
			t.Log("Passed")
		}
	}
}

func TestMin(t *testing.T) {
	for _, pair := range minTests {
		v := Min(pair.values)
		if v != pair.average {
			t.Error(
				"Failed",
				"For", pair.values,
				"expected", pair.average,
				"got", v,
			)
		} else {
			t.Log("Passed")
		}
	}
}

func TestMax(t *testing.T) {
	for _, pair := range maxTests {
		v := Max(pair.values)
		if v != pair.average {
			t.Error(
				"Failed",
				"For", pair.values,
				"expected", pair.average,
				"got", v,
			)
		} else {
			t.Log("Passed")
		}
	}
}
