package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
)

// начало решения

// Handy предоставляет удобный интерфейс
// для выполнения HTTP-запросов
type Handy struct {
	DefaultClient *http.Client
	Uri           string
	Headers       map[string]string
	Params        map[string]string
	Body          io.Reader
	Error         error
}

// NewHandy создает новый экземпляр Handy
func NewHandy() *Handy {
	return &Handy{
		DefaultClient: http.DefaultClient,
		Headers:       make(map[string]string),
		Params:        make(map[string]string)}
}

// URL устанавливает URL, на который пойдет запрос
func (h *Handy) URL(uri string) *Handy {
	h.Uri = uri
	return h
}

// Client устанавливает HTTP-клиента
// вместо умолчательного http.DefaultClient
func (h *Handy) Client(client *http.Client) *Handy {
	h.DefaultClient = client
	return h
}

// Header устанавливает значение заголовка
func (h *Handy) Header(key, value string) *Handy {
	h.Headers[key] = value
	return h
}

// Param устанавливает значение URL-параметра
func (h *Handy) Param(key, value string) *Handy {
	h.Params[key] = value
	return h
}

// Form устанавливает данные, которые будут закодированы
// как application/x-www-form-urlencoded и отправлены в теле запроса
// с соответствующим content-type
func (h *Handy) Form(form map[string]string) *Handy {
	data := url.Values{}
	for key, value := range form {
		data.Add(key, value)
	}
	h.Body = bytes.NewBufferString(data.Encode())
	h.Header("Content-Type", "application/x-www-form-urlencoded")
	return h
}

// JSON устанавливает данные, которые будут закодированы
// как application/json и отправлены в теле запроса
// с соответствующим content-type
func (h *Handy) JSON(v any) *Handy {

	body, err := json.Marshal(v)
	if err != nil {
		h.Error = err
		return h
	}
	h.Body = bytes.NewBuffer(body)
	h.Header("Content-Type", "application/json")
	return h
}

// Get выполняет GET-запрос с настроенными ранее параметрами
func (h *Handy) Get() *HandyResponse {

	if h.Error != nil {
		return &HandyResponse{Error: h.Error}
	}

	req, err := http.NewRequest(http.MethodGet, h.Uri, nil)

	if err != nil {
		return nil
	}

	for k, v := range h.Headers {
		req.Header.Add(k, v)
	}

	queryParams := url.Values{}

	for k, v := range h.Params {
		queryParams.Add(k, v)
	}

	req.URL.RawQuery = queryParams.Encode()

	if err != nil {
		return nil
	}

	resp, err := h.DefaultClient.Do(req)

	if err != nil {
		return &HandyResponse{Error: h.Error}
	}

	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)

	if err != nil {
		return nil
	}

	return &HandyResponse{StatusCode: resp.StatusCode, Body: body}
}

// Post выполняет POST-запрос с настроенными ранее параметрами
func (h *Handy) Post() *HandyResponse {

	if h.Error != nil {
		return &HandyResponse{Error: h.Error}
	}

	req, err := http.NewRequest(http.MethodPost, h.Uri, h.Body)

	if err != nil {
		return nil
	}

	for k, v := range h.Headers {
		req.Header.Add(k, v)
	}

	queryParams := url.Values{}

	for k, v := range h.Params {
		queryParams.Add(k, v)
	}

	req.URL.RawQuery = queryParams.Encode()

	if err != nil {
		return nil
	}

	resp, err := h.DefaultClient.Do(req)

	if err != nil {
		return &HandyResponse{Error: h.Error}
	}

	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)

	if err != nil {
		return nil
	}

	return &HandyResponse{StatusCode: resp.StatusCode, Body: body}
}

// HandyResponse представляет ответ на HTTP-запрос
type HandyResponse struct {
	StatusCode int
	Body       []byte
	Error      error
}

// OK возвращает true, если во время выполнения запроса
// не произошло ошибок, а код HTTP-статуса ответа равен 200
func (r *HandyResponse) OK() bool {
	if r != nil && r.StatusCode == 200 {
		return true
	}
	return false
}

// Bytes возвращает тело ответа как срез байт
func (r *HandyResponse) Bytes() []byte {
	return r.Body
}

// String возвращает тело ответа как строку
func (r *HandyResponse) String() string {
	return string(r.Body)
}

// JSON декодирует тело ответа из JSON и сохраняет
// результат по адресу, на который указывает v
// работает аналогично json.Unmarshal()
// если при декодировании произошла ошибка,
// она должна быть доступна через r.Err()
func (r *HandyResponse) JSON(v any) {
	if r == nil || r.Body == nil || r.Err() != nil {
		r.Error = fmt.Errorf("JSON decode failed: %v", r.Err())
		return
	}

	err := json.Unmarshal(r.Body, &v)
	if err != nil {
		r.Error = err
	}

}

// Err возвращает ошибку, которая возникла при выполнении запроса
// или обработке ответа
func (r *HandyResponse) Err() error {
	return r.Error
}

// конец решения

func main() {
	{
		// примеры запросов

		// GET-запрос с параметрами
		NewHandy().URL("https://httpbingo.org/get").Param("id", "42").Get()

		// HTTP-заголовки
		NewHandy().
			URL("https://httpbingo.org/get").
			Header("Accept", "text/html").
			Header("Authorization", "Bearer 1234567890").
			Get()

		// POST формы
		params := map[string]string{
			"brand":    "lg",
			"category": "tv",
		}
		NewHandy().URL("https://httpbingo.org/post").Form(params).Post()

		// POST JSON-документа
		NewHandy().URL("https://httpbingo.org/post").JSON(params).Post()
	}

	{
		// пример обработки ответа

		// отправляем GET-запрос с параметрами
		resp := NewHandy().URL("https://httpbingo.org/get").Param("id", "42").Get()
		if !resp.OK() {
			panic(resp.String())
		}

		// декодируем ответ в JSON
		var data map[string]any
		resp.JSON(&data)

		fmt.Println(data["url"])
		// "https://httpbingo.org/get"
		fmt.Println(data["args"])
		// map[id:[42]]
	}
}
