package main

import (
	"fmt"
	"os"
	"strings"
)

// начало решения

// readLines возвращает все строки из указанного файла
func readLines(name string) ([]string, error) {
	data, err := os.ReadFile(name)
	if err != nil {
		return nil, err
	}

	content := string(data)
	//fmt.Println(content)
	lines := strings.Split(content, "\n")
	if lines[len(lines)-1] == "" {
		return lines[:len(lines)-1], nil
	}

	return lines, nil
}

// конец решения

func main() {
	lines, err := readLines("1.txt")
	if err != nil {
		panic(err)
	}
	for idx, line := range lines {
		fmt.Printf("%d: %s\n", idx+1, line)
	}
}
