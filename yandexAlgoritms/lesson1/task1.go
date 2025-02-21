package main

import (
	"fmt"
)

var room, cond int
var mode string

func readInput() {
	_, err := fmt.Scan(&room, &cond)

	if err != nil {
		fmt.Print(err)
		return
	}

	_, err1 := fmt.Scan(&mode)

	if err1 != nil {
		fmt.Print(err)
		return
	}
}

func main() {
	readInput()
	//fmt.Println("Введенные числа:", room, cond)
	//fmt.Println("Введенный мод:", mode)

	switch mode {
	case "freeze":
		if cond <= room {
			fmt.Print(cond)
		} else {
			fmt.Print(room)
		}
	case "heat":
		if cond >= room {
			fmt.Print(cond)
		} else {
			fmt.Print(room)
		}
	case "auto":
		fmt.Print(cond)
	default:
		fmt.Print(room)
	}

}
