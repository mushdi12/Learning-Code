package main

import (
	"fmt"
	"strconv"
	"strings"
	"testing"
)

// начало решения

// prettify возвращает отформатированное
// строковое представление карты
func prettify(m map[string]int) string {
	var b strings.Builder

	if len(m) == 0 {
		b.WriteString("{}")
	} else if len(m) == 1 {
		b.WriteString("{ ")
		for key, value := range m {
			writeKeyValue(&b, key, value)
		}
		b.WriteString(" }")
	} else {
		b.WriteString("{\n")
		for key, value := range m {
			b.WriteString("    ")
			writeKeyValue(&b, key, value)
			b.WriteString(",\n")
		}
		b.WriteString("}")
	}

	return b.String()
}

func writeKeyValue(b *strings.Builder, key string, value int) {
	b.WriteString(key)
	b.WriteString(": ")
	strValue := strconv.Itoa(value)
	b.WriteString(strValue)
}

// конец решения

func Test(t *testing.T) {
	m := map[string]int{"one": 1, "two": 2, "three": 3}
	const want = "{\n    one: 1,\n    three: 3,\n    two: 2,\n}"
	got := prettify(m)
	if got != want {
		t.Errorf("%v\ngot:\n%v\n\nwant:\n%v", m, got, want)
	}
}

func main() {
	m := map[string]int{"one": 1, "two": 2, "three": 3}
	m1 := map[string]int{"one": 1}
	m2 := map[string]int{}
	fmt.Println(prettify(m))
	fmt.Println(prettify(m1))
	fmt.Println(prettify(m2))
}
