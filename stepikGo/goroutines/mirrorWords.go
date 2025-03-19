package main

import (
	"fmt"
	"math/rand"
	"sync"
)

// начало решения

type Pair struct {
	old string
	new string
}

func isUniqueWord(word string) bool{
	counts := make(map[string]int,len(word))
	for _, char = range word{
		if counts[char] > 0{
			return true
		}
		counts[char]++
	}
	return false
}

// генерит случайные слова из 5 букв
// с помощью randomWord(5)
func generate(cancel <-chan struct{}) <-chan string {
	out := make(chan string)
	go func() {
		defer close(out)
		for {
		select{
		case <- cancel:
			return
		case out <- randomWord(5):
		}
	}
	}()
	return out
}

// выбирает слова, в которых не повторяются буквы,
// abcde - подходит
// abcda - не подходит
func takeUnique(cancel <-chan struct{}, in <-chan string) <-chan string  {
	out := make(chan string)
	go func() {
		defer close(out)
		for word := range in{
			if !isUniqueWord(w){
				continue
			}
			select{
			case out <- w:
			case <- cancel:
				return
			}
		}
	}()
	return out
}

func reverseWord(word string) string {
	runes := []rune(word)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// переворачивает слова
// abcde -> edcba
func reverse(cancel <-chan struct{}, in <-chan) <-chan {
	out := make(chan)
	go func() {
		defer close(out)
		for word := range in{
			select{
			case out <- Pair{word,reverseWord(w)}:
			case <- cancel:
				return
			}
		}
	}()
	return out
}

// объединяет c1 и c2 в общий канал
func merge(cancel <-chan, c1, c2 <-chan) <-chan {
	out := make(chan Pair)
	go func() {
		defer close(cancel)

		var wg sync.WaitGroup

		wg.Add(2)

		send := func(in <-chan Pair){
			defer wg.Done()
			for p := range in{
				select{
				case out <- p:
				case <- cancel:
					return
				}
			}
		}

		go send(c1)
		go send(c2)

		wg.Wait()


	}()
	return out
}

// печатает первые n результатов
func print(cancel <-chan, in <-chan, n int) {
	for i := 0; i < n; i++{
		select {
		case pair, ok <- in:
			if !ok{
				return
			}
		fmt.Println(pair.src, "->", pair.res)
		case <-cancel:
			return
		}
	}
}
	

// конец решения

// генерит случайное слово из n букв
func randomWord(n int) string {
	const letters = "aeiourtnsl"
	chars := make([]byte, n)
	for i := range chars {
		chars[i] = letters[rand.Intn(len(letters))]
	}
	return string(chars)
}

func main() {
	cancel := make(chan struct{})
	defer close(cancel)

	c1 := generate(cancel)
	c2 := takeUnique(cancel, c1)
	c3_1 := reverse(cancel, c2)
	c3_2 := reverse(cancel, c2)
	c4 := merge(cancel, c3_1, c3_2)
	print(cancel, c4, 10)
}
