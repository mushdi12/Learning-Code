package main

// не меняйте импорты, они нужны для проверки
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// account представляет счет
type account struct {
	balance   int
	overdraft int
}

func main() {
	var acc account
	var trans []int
	defer func() {
		fmt.Print("-> ")
		err := recover()
		if err != nil {
			fmt.Println(err)
			return
		}
		fmt.Println(acc, trans)
	}()
	acc, trans = parseInput()
}

// parseInput считывает счет и список транзакций из os.Stdin.
func parseInput() (account, []int, err) {
	accSrc, transSrc := readInput()
	acc, err := parseAccount(accSrc)
	if err != nil {
		return account{}, nil, err
	}
	trans, err := parseTransactions(transSrc)
	if err != nil {
		return account{}, nil, err
	}
	return acc, trans
}

// readInput возвращает строку, которая описывает счет
// и срез строк, который описывает список транзакций.
// эту функцию можно не менять
func readInput() (string, []string) {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	scanner.Scan()
	accSrc := scanner.Text()
	var transSrc []string
	for scanner.Scan() {
		transSrc = append(transSrc, scanner.Text())
	}
	return accSrc, transSrc
}

// parseAccount парсит счет из строки
// в формате balance/overdraft.
func parseAccount(src string) (account, err) {
	parts := strings.Split(src, "/")
	balance, err := strconv.Atoi(parts[0])
	if err != nil {
		return account{}, err
	}
	overdraft, err := strconv.Atoi(parts[1])
	if err != nil {
		return account{}, err
	}
	if overdraft < 0 {
		panic("expect overdraft >= 0")
	}
	if balance < -overdraft {
		panic("balance cannot exceed overdraft")
	}
	return account{balance, overdraft}, nil
}

// parseTransactions парсит список транзакций из строки
// в формате [t1 t2 t3 ... tn].
func parseTransactions(src []string) ([]int, err) {
	trans := make([]int, len(src))
	for idx, s := range src {
		t, err := strconv.Atoi(s)
		if err != nil {
			return trans, err
		}
		trans[idx] = t
	}
	return trans, nil
}
