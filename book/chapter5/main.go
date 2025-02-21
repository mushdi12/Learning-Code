package main

import "fmt"

func task1(number int) (float64, bool) {
	result := float64(number) / 2
	if int(result)%2 == 0 {
		return result, true
	} else {
		return result, false
	}
}

func task2(numbers ...int) int {
	maximum := 0
	for _, number := range numbers {
		if number > maximum {
			maximum = number
		}
	}
	return maximum
}

func makeOddGenerator() func() uint {
	i := uint(1)
	return func() (ret uint) {
		ret = i
		i += 2
		return
	}
}

func fib(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	return fib(n-1) + fib(n-2)
}

func main() {
	// task 1
	result1, result11 := task1(100)
	fmt.Println("Task №1:", result1, result11)

	// task 2
	fmt.Println("Task №2:", task2(1, 2, 3, 4, 5))

	//task 3
	makeOdd := makeOddGenerator()
	fmt.Print("Task №3: ", makeOdd())
	fmt.Print(" ", makeOdd())
	fmt.Println(" ", makeOdd())

	//task 4
	fmt.Println("Task №4: ", fib(8))
}
