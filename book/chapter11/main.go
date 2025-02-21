package main

import (
	"fmt"
	"sort"
)

type People struct {
	name string
	age  int
	job  string
}
type ByJob []People

func (this ByJob) Len() int {
	return len(this)
}

func (this ByJob) Less(i, j int) bool {
	return this[i].job < this[j].job
}
func (this ByJob) Swap(i, j int) {
	this[i], this[j] = this[j], this[i]
}

func Print(peoples ...People) {
	for _, p := range peoples {
		fmt.Printf("name: %s, age: %d, job: %s\n", p.name, p.age, p.job)
	}

}

func main() {
	p1 := People{"Bob", 20, "Jay"}
	p2 := People{"Roy", 27, "Actor"}
	Print(p1, p2)
	peoples := []People{p1, p2}
	sort.Sort(ByJob(peoples))
	Print(peoples...)

}
