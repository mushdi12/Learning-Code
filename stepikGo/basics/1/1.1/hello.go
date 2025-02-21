package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	out := bufio.NewWriter(os.Stdout)
	fmt.Fprint(out, "Hello"+", world!")
	out.Flush()
}
