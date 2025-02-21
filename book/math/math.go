package math

// Average - public, average - private
// Имена пакетов совпадают с директориями, в которых они размещены
func Average(x []float64) float64 {
	total := float64(0)
	for _, elements := range x {
		total += elements
	}
	return total / float64(len(x))
}

func Max(x []float64) float64 {
	max := float64(0)
	for _, elements := range x {
		if max < elements {
			max = elements
		}
	}
	return max
}

func Min(x []float64) float64 {
	min := float64(1000)
	for _, elements := range x {
		if min > elements {
			min = elements
		}
	}
	return min
}
