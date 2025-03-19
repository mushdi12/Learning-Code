package main

import (
	"bufio"
	"fmt"
	mathrand "math/rand"
	"os"
	"path/filepath"
)

// алфавит планеты Нибиру
const alphabet = "aeiourtnsl"

// Census реализует перепись населения
// Записи о рептилоидах хранятся в каталоге census в отдельных файлах
// по одному файлу на каждую букву алфавита.
type Census struct {
	files map[byte]*os.File
	count int
}

// NewCensus создает новую перепись и пустые файлы для будущих записей о населении.
func NewCensus() *Census {
	_ = os.Mkdir("census", os.ModePerm)

	files := make(map[byte]*os.File)
	for i := range alphabet {
		filename := filepath.Join("census", string(alphabet[i])+".txt")
		file, err := os.OpenFile(filename, os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0644)
		if err != nil {
			panic(err)
		}
		files[alphabet[i]] = file
	}

	return &Census{files: files}
}

// Add записывает сведения о рептилоиде.
func (c *Census) Add(name string) {
	if len(name) == 0 {
		return
	}
	file := c.files[name[0]]
	_, _ = file.WriteString(name + "\n")
	c.count++
}

// Count возвращает общее количество переписанных рептилоидов.
func (c *Census) Count() int {
	return c.count
}

// Close закрывает файлы, использованные переписью.
func (c *Census) Close() {
	for _, file := range c.files {
		_ = file.Close()
	}
}

var rand = mathrand.New(mathrand.NewSource(0))

// randomName возвращает имя очередного рептилоида.
func randomName(n int) string {
	chars := make([]byte, n)
	for i := range chars {
		chars[i] = alphabet[rand.Intn(len(alphabet))]
	}
	return string(chars)
}

// main демонстрирует работу Census.
func main() {
	census := NewCensus()
	defer census.Close()

	for i := 0; i < 1024; i++ {
		reptoid := randomName(5)
		census.Add(reptoid)
	}

	fmt.Println(census.Count())

	// Подсчет записей в файле n.txt и вывод 42-й записи
	filename := "census/n.txt"
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	names := []string{}
	for scanner.Scan() {
		names = append(names, scanner.Text())
	}

	if len(names) >= 42 {
		fmt.Printf("%d %s\n", len(names), names[41])
	} else {
		fmt.Printf("%d -\n", len(names))
	}
}
