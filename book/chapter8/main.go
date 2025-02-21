package main

import (
	"fmt"
	"time"
)

func prints() {
	fmt.Println("Hello world")
}

func CustomSleep(duration time.Duration) {
	<-time.After(duration) // Ждём, пока истечёт время
}
func main() {
	fmt.Println("Начало:", time.Now()) // Вывод текущего времени

	go prints()
	// Усыпляем на 2 секунды
	fmt.Println("Конец:", time.Now()) // Вывод времени после задержки
	CustomSleep(time.Millisecond * 1000)

}
