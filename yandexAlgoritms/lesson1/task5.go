package main

import "fmt"

func main() {
	var K1, M, K2, P2, N2 int
	fmt.Scan(&K1, &M, &K2, &P2, &N2)

	q := (K2-1)/M + 1 // кол-во квартир на этаже

	fmt.Println(q)

	checkP2 := (K2-1)/q + 1
	checkN2 := (K2-1)/(q*checkP2) + 1

	fmt.Println(checkP2)
	fmt.Println(checkN2)

	if checkP2 != P2 && checkN2 != N2 {
		fmt.Println("-1 -1")
		return
	}

	P1 := (K1-1)/q + 1
	N1 := (K1-1)/(P1*q) + 1

	fmt.Print(P1, N1)

}
