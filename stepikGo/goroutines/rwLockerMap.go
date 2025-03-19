package main

import (
	"fmt"
	"sync"
)

// начало решения

type Counter struct {
	counterMap map[string]int
	lock       sync.RWMutex
}

func (c *Counter) Increment(str string) {
	c.lock.Lock()
	defer c.lock.Unlock()
	c.counterMap[str]++
}

func (c *Counter) Value(str string) int {
	c.lock.RLock()
	defer c.lock.RUnlock()
	return c.counterMap[str]
}

func (c *Counter) Range(fn func(key string, val int)) {
	c.lock.RLock()
	defer c.lock.RUnlock()
	for key, value := range c.counterMap {
		fn(key, value)
	}
}

func NewCounter() *Counter {
	return &Counter{map[string]int{}, sync.RWMutex{}}
}

// конец решения

func main() {
	counter := NewCounter()

	var wg sync.WaitGroup
	wg.Add(3)

	increment := func(key string, val int) {
		defer wg.Done()
		for ; val > 0; val-- {
			counter.Increment(key)
		}
	}

	go increment("one", 100)
	go increment("two", 200)
	go increment("three", 300)

	wg.Wait()

	fmt.Println("two:", counter.Value("two"))

	fmt.Print("{ ")
	counter.Range(func(key string, val int) {
		fmt.Printf("%s:%d ", key, val)
	})
	fmt.Println("}")
}
