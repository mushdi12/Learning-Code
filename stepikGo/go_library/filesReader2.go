package main

import (
	"bufio"
	"fmt"
	"os"
)

// начало решения

// readLines возвращает все строки из указанного файла
func readLines(name string) ([]string, error) {
	file, err := os.Open(name)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	result := []string{}

	scanner := bufio.NewScanner(file) 
	for scanner.Scan() {              
		line := scanner.Text() 
		result = append(result, line)
		//fmt.Printf("%#v\n", line)
	}

	return result, nil
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
