# Habr Parser

Небольшой Python-скрипт для парсинга популярных статей на [Habr](https://habr.com) с указанием заголовков и количества просмотров.
Проект выполнен по плану: https://solvit.space/projects/habr_parser
---

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/arhipov-om/habr-parser.git
cd habr-parser
```

2. Установите зависимости через pip:

```bash
python -m pip install httpx lxml
```
Или используя uv 

```bash
uv sync 
```

> Проект тестировался на Python >= 3.11.

## Пример запуска скрипта:

```bash
python -m habr_parser
```