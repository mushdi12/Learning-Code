package main

// не удаляйте импорты, они используются при проверке
import (
    "fmt"
    "math/rand"
    "os"
    "strings"
    "testing"
)

// Words работает со словами в строке.
type Words struct {
    words_map map[string]int
}

// MakeWords создает новый экземпляр Words.
func MakeWords(s string) Words {
	words := strings.Fields(s)
	msv := make(map[string]int,len(words))
	for index, word := range words{
		if _, ok := msv[word]; !ok{
			msv[word] = index
		}
	}
    return Words{msv}
}

// Index возвращает индекс первого вхождения слова в строке,
// или -1, если слово не найдено.
func (w Words) Index(word string) int {
	if index, ok := w.words_map[word]; ok {
		return index
	}
	return -1
}