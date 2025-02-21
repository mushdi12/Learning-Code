package main

// не удаляйте импорты, они используются при проверке
import (
    "fmt"
    "math/rand"
    "os"
    "testing"
)

// IntSet реализует множество целых чисел
// (элементы множества уникальны).
type IntSet map[int] struct {}

// MakeIntSet создает пустое множество.
func MakeIntSet() IntSet {
    return IntSet{}
}

// Contains проверяет, содержится ли элемент в множестве.
func (s IntSet) Contains(elem int) bool {
	_, isContain := s[elem]
    return isContain
}

// Add добавляет элемент в множество.
// Возвращает true, если элемент добавлен,
// иначе false (если элемент уже содержится в множестве).
func (s IntSet) Add(elem int) bool {
	if s.Contains(elem){
		s[elem] = struct{}{}
		return true
	} 
	return false
	

}