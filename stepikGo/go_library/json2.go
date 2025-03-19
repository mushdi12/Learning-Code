package main

import (
	"encoding/json"
	"fmt"
)

// начало решения

// Genre описывает жанр фильма
type Genre struct {
	Name string `json:"name"`
}

// Movie описывает фильм
type Movie struct {
	Title  string  `json:"name"`
	Year   int     `json:"released_at"`
	Genres []Genre `json:"tags"`
}

// Вспомогательная структура для декодирования JSON
type rawMovie struct {
	Name       string `json:"name"`
	ReleasedAt int    `json:"released_at"`
	Tags       []struct {
		Name string `json:"name"`
	} `json:"tags"`
}

// Реализуем кастомный UnmarshalJSON
func (m *Movie) UnmarshalJSON(data []byte) error {
	var raw rawMovie
	if err := json.Unmarshal(data, &raw); err != nil {
		return err
	}

	m.Title = raw.Name
	m.Year = raw.ReleasedAt
	for _, tag := range raw.Tags {
		m.Genres = append(m.Genres, Genre(tag.Name))
	}

	return nil
}

// конец решения

func main() {
	const src = `{
		"name": "Interstellar",
		"released_at": 2014,
		"director": "Christopher Nolan",
		"tags": [
			{ "name": "Adventure" },
			{ "name": "Drama" },
			{ "name": "Science Fiction" }
		],
		"duration": "2h49m",
		"rating": "★★★★★"
	}`

	var m Movie
	err := json.Unmarshal([]byte(src), &m)
	fmt.Println(err)
	// nil
	fmt.Println(m)
	// {Interstellar 2014 [Adventure Drama Science Fiction]}
}
