package main

import (
	"strings"
	"testing"
)

// начало решения

// slugify возвращает "безопасный" вариант заголовока:
// только латиница, цифры и дефис
func slugify(src string) string {

	result := strings.ToLower(src)
	result = strings.Map(checkVerify, result)
	resultMap := strings.Fields(result)
	result = strings.Join(resultMap, "-")
	return result
}

func checkVerify(r rune) rune {
	verifSumbols := "abcdefghijklmnopqrstuvwxyz01234567890- "
	if strings.ContainsRune(verifSumbols, r) {
		return r
	}
	return ' '
}

// конец решения

func Test(t *testing.T) {
	const phrase = "Go Is Awesome!"
	const want = "go-is-awesome"
	got := slugify(phrase)
	if got != want {
		t.Errorf("%s: got %#v, want %#v", phrase, got, want)
	}
}
