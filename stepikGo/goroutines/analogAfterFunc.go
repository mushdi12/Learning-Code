package main

import (
	"fmt"
	"math/rand"
	"time"
)

// начало решения

func delay(dur time.Duration, fn func()) func() {
	canceled := make(chan struct{})

	timer := time.NewTimer(dur)

	go func() {
		select {
		case <-timer.C:
			fn()
		case <-canceled: // Отмена
			// Выходим из горутины

		}
	}()

	cancel := func() {
		if !timer.Stop() {
			return
		}
		close(canceled)
	}

	return cancel
}

// конец решения

func main() {
	work := func() {
		fmt.Println("work done")
	}

	cancel := delay(100*time.Millisecond, work)

	time.Sleep(10 * time.Millisecond)
	if rand.Float32() < 0.5 {
		cancel()
		fmt.Println("delayed function canceled")
	}
	time.Sleep(100 * time.Millisecond)
}
