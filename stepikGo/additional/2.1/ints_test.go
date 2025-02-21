package ints

import "testing"

func TestIntMin(t *testing.T) {
	got := IntMin(1, 2)
	want := 1
	if got != want {
		t.Errorf("got %d; want %d", got, want)
	}
}
