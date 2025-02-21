package main

import "fmt"

// начало решения

// Map - карта "ключ-значение".
type Map[K comparable, V any] map[K]V

// Set устанавливает значение для ключа.
func (m Map[K, V]) Set(key K, val V) {
	m[key] = val
}

// Get возвращает значение по ключу.
func (m Map[K, V]) Get(key K) V {
	return m[key]
}

// Keys возвращает срез ключей карты.
// Порядок ключей неважен, и не обязан совпадать
// с порядком значений из метода Values.
func (m Map[K, V]) Keys() []K {
	result := []K{}

	for k := range m {
		result = append(result, K(k))
	}

	return result
}

// Values возвращает срез значений карты.
// Порядок значений неважен, и не обязан совпадать
// с порядком ключей из метода Keys.
func (m Map[K, V]) Values() []V {
	result := []V{}

	for _, v := range m {
		result = append(result, v)
	}

	return result
}

// конец решения

func main() {
	m := Map[string, int]{}
	m.Set("one", 1)
	m.Set("two", 2)

	fmt.Println(m.Get("one")) // 1
	fmt.Println(m.Get("two")) // 2

	fmt.Println(m.Keys())   // [one two]
	fmt.Println(m.Values()) // [1 2]
}
