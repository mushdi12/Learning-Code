package main

import (
	"database/sql"
	"errors"
	"fmt"

	_ "github.com/mattn/go-sqlite3"
)

// начало решения

// SQLMap представляет карту, которая хранится в SQL-базе данных
type SQLMap struct {
	db   *sql.DB
	stmt *sql.Stmt
}

// NewSQLMap создает новую SQL-карту в указанной базе
func NewSQLMap(db *sql.DB) (*SQLMap, error) {
	if db == nil {
		return nil, errors.New("error")
	}

	query := "create table if not exists map(key text primary key, val blob)"

	_, err := db.Exec(query)

	if err != nil {
		return nil, errors.New("failed to create table")
	}

	return &SQLMap{db: db}, nil
}

// Get возвращает значение для указанного ключа.
// Если такого ключа нет - возвращает ошибку sql.ErrNoRows.
func (m *SQLMap) Get(key string) (any, error) {
	stmt, err := m.db.Prepare(`select val from map where key = ?`)
	row := stmt.QueryRow(key)
	var value any
	err = row.Scan(&value)

	if err != nil {
		return nil, err
	}

	return value, nil
}

// Set устанавливает значение для указанного ключа.
// Если такой ключ уже есть - затирает старое значение (это не считается ошибкой).
func (m *SQLMap) Set(key string, val any) error {
	stmt, err := m.db.Prepare(`insert into map(key, val) values (?, ?) on conflict (key) do update set val = excluded.val`)

	_, err = stmt.Exec(key, val)

	if err != nil {
		return err
	}
	return nil
}

// SetItems устанавливает значения указанных ключей.
func (m *SQLMap) SetItems(items map[string]any) error {
	stmt, err := m.db.Prepare(`insert into map(key, val) values (?, ?) on conflict (key) do update set val = excluded.val`)
	if err != nil {
		return err
	}

	for index, val := range items {
		_, err := stmt.Exec(index, val)
		if err != nil {
			return err
		}
	}
	return nil
}

// Delete удаляет запись карты с указанным ключом.
// Если такого ключа нет - ничего не делает (это не считается ошибкой).
func (m *SQLMap) Delete(key string) error {
	stmt, err := m.db.Prepare(`delete from map where key = ?`)

	_, err = stmt.Exec(key)

	if err != nil {
		return err
	}
	return nil
}

// Close освобождает ресурсы, занятые картой в базе.
func (m *SQLMap) Close() error {
	return nil
}

// конец решения

func main() {
	db, err := sql.Open("sqlite3", ":memory:")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	m, err := NewSQLMap(db)
	if err != nil {
		panic(err)
	}
	defer m.Close()

	m.Set("name", "Alice")

	items := map[string]any{
		"name": "Bob",
		"age":  42,
	}
	m.SetItems(items)

	name, err := m.Get("name")
	fmt.Printf("name = %v, err = %v\n", name, err)
	// name = Bob, err = <nil>

	age, err := m.Get("age")
	fmt.Printf("age = %v, err = %v\n", age, err)
	// age = 42, err = <nil>
}
