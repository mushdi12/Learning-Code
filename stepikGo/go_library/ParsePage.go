// asLegacyDate преобразует время в легаси-дату
func asLegacyDate(t time.Time) string {
    sec := t.Unix()
    nano := t.UnixNano() - sec*1e9
    if nano == 0 {
        return fmt.Sprintf("%d.0", sec)
    }
    str := fmt.Sprintf("%d.%09d", sec, nano)
    return strings.TrimRight(str, "0")
}

// parseLegacyDate преобразует легаси-дату во время.
// Возвращает ошибку, если легаси-дата некорректная.
func parseLegacyDate(d string) (time.Time, error) {
    strSec, strNano, ok := strings.Cut(d, ".")
    if !ok {
        return time.Time{}, fmt.Errorf("invalid date: %v", d)
    }

    sec, err := strconv.ParseInt(strSec, 10, 64)
    if err != nil {
        return time.Time{}, fmt.Errorf("invalid date: %v", d)
    }

    if len(strNano) == 0 {
        return time.Time{}, fmt.Errorf("invalid date: %v", d)
    }
    strNano = padZerosRight(strNano, 9)
    nano, err := strconv.ParseInt(strNano, 10, 64)
    if err != nil {
        return time.Time{}, fmt.Errorf("invalid date: %v", d)
    }

    return time.Unix(sec, nano), nil
}

// padZerosRight отбивает строку нулями справа до указанной длины
func padZerosRight(str string, length int) string {
    if len(str) >= length {
        return str
    }
    return str + strings.Repeat("0", length-len(str))
}