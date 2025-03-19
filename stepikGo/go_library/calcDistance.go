package main

import (
	"fmt"
	"strconv"
	"strings"
	"testing"
)

// начало решения

// calcDistance возвращает общую длину маршрута в метрах
func calcDistance(directions []string) int {
	summaryDistance := 0
	for _, direction := range directions {
		direction = strings.ReplaceAll(direction, "m", "")

		if !strings.Contains(direction, ".") {
			direction = strings.ReplaceAll(direction, "k", "000")
		} else {
			direction = strings.ReplaceAll(direction, ".", "")
			direction = strings.ReplaceAll(direction, "k", "00")
		}

		directionMsv := strings.Fields(direction)
		
		for _, w := range directionMsv {
			distance, err := strconv.Atoi(w)
			if err == nil {
				summaryDistance += distance
			}
		}
	}
	return summaryDistance
}

// конец решения

func Test(t *testing.T) {
	directions := []string{
		"100m to intersection",
		"turn right",
		"straight 300m",
		"enter motorway",
		"straight 5km",
		"exit motorway",
		"500m straight",
		"turn sharp left",
		"continue 100m to destination",
	}
	const want = 6000
	got := calcDistance(directions)
	if got != want {
		t.Errorf("%v: got %v, want %v", directions, got, want)
	}
}

func main() {

	directions := []string{
		"100m to intersection",
		"turn right",
		"straight 300m",
		"enter motorway",
		"straight 5.1km",
		"exit motorway",
		"500m straight",
		"turn sharp left",
		"continue 100m to destination",
	}
	fmt.Println(calcDistance(directions))

}
