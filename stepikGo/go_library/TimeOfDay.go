package main

import (
	"errors"
	"fmt"
	"testing"
	"time"
)

// начало решения

// TimeOfDay описывает время в пределах одного дня
type TimeOfDay struct {
	hour     int
	minute   int
	second   int
	location *time.Location
}

// Hour возвращает часы в пределах дня
func (t TimeOfDay) Hour() int {
	return t.hour
}

// Minute возвращает минуты в пределах часа
func (t TimeOfDay) Minute() int {
	return t.minute
}

// Second возвращает секунды в пределах минуты
func (t TimeOfDay) Second() int {
	return t.second
}

// String возвращает строковое представление времени
// в формате чч:мм:сс TZ (например, 12:34:56 UTC)
func (t TimeOfDay) String() string {
	timeStr := fmt.Sprintf("%02d:%02d:%02d", t.hour, t.minute, t.second)
	tz := t.location.String()
	return fmt.Sprintf("%s %s", timeStr, tz)
}

// Equal сравнивает одно время с другим.
// Если у t и other разные локации - возвращает false.
func (t TimeOfDay) Equal(other TimeOfDay) bool {
	if other.location.String() != t.location.String() {
		return false
	}

	if t.hour == other.hour && t.minute == other.minute && t.second == other.second {
		return true
	} else {
		return false
	}
}

// Before возвращает true, если время t предшествует other.
// Если у t и other разные локации - возвращает ошибку.
func (t TimeOfDay) Before(other TimeOfDay) (bool, error) {
	if other.location.String() != t.location.String() {
		return false, errors.New("not implemented")
	}

	if t.hour < other.hour {
		return true, nil
	}
	if t.hour == other.hour && t.minute < other.minute {
		return true, nil
	}
	if t.hour == other.hour && t.minute == other.minute && t.second < other.second {
		return true, nil
	}
	return false, nil

}

// After возвращает true, если время t идет после other.
// Если у t и other разные локации - возвращает ошибку.
func (t TimeOfDay) After(other TimeOfDay) (bool, error) {
	if other.location != t.location {
		return false, errors.New("not implemented")
	}

	if t.hour > other.hour {
		return true, nil
	}
	if t.hour == other.hour && t.minute > other.minute {
		return true, nil
	}
	if t.hour == other.hour && t.minute == other.minute && t.second > other.second {
		return true, nil
	}
	return false, nil
}

// MakeTimeOfDay создает время в пределах дня
func MakeTimeOfDay(hour, min, sec int, loc *time.Location) TimeOfDay {
	return TimeOfDay{hour: hour, minute: min, second: sec, location: loc}
}

// конец решения

func Test(t *testing.T) {
	t1 := MakeTimeOfDay(17, 45, 22, time.UTC)
	t2 := MakeTimeOfDay(20, 3, 4, time.UTC)

	if t1.Equal(t2) {
		t.Errorf("%v should not be equal to %v", t1, t2)
	}

	before, _ := t1.Before(t2)
	if !before {
		t.Errorf("%v should be before %v", t1, t2)
	}

	after, _ := t1.After(t2)
	if after {
		t.Errorf("%v should NOT be after %v", t1, t2)
	}
}
