# ⚡ ShadowPassword / Chaos Generator ⚡

> **Креативный инструмент для автоматической трансформации базовых слов в высокоэнтропийные L33t-Speak пароли.**

[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Security Focus](https://img.shields.io/badge/Security-L33t--Speak%20Entropy-red?style=for-the-badge&logo=shields.io)](https://github.com/TSMaria04/chaos-gen)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](https://github.com/TSMaria04/chaos-gen)

---

## 🎯 О проекте

Классические генераторы паролей создают случайные последовательности вроде `x8#kL!29@zQ`, которые практически невозможно запомнить без менеджера паролей. 

**ShadowPassword (Chaos Generator)** решает эту проблему: он берет понятное вам базовое слово и накладывает на него **L33t-Speak подстановки**, рандомизацию регистра, а также динамические спецсимволы-префиксы и суффиксы.

> 💡 **Результат:** Пароль обладает высокой стойкостью к брутфорсу (сложный словарь + спецсимволы + цифры) и при этом легко запоминается автором.

---

## 🚀 Ключевой функционал

- 🔀 **Smart L33t-Speak:** Умная вероятностная замена букв на символы и цифры (вероятность 70%).
- 🎲 **Random Case Mixing:** Динамическое перемешивание строчных и прописных букв.
- 🛡 **Хаос-обрамление:** Автоматическая генерация префиксов и суффиксов из спецсимволов и случайных чисел.
- 📋 **Clipboard Sync:** Автоматическое копирование сгенерированного пароля в буфер обмена (`pyperclip`).
- 🎨 **CLI Aesthetics:** Стильный ASCII-арт баннер и цветная подсвечиваемая консоль (`colorama`).

---

## 🔤 Таблица L33t-Замен

| Исходная буква | Варианты подмены | Пример трансформации |
| :---: | :---: | :---: |
| **A / a** | `@`, `4` | `m@rix` / `m4rix` |
| **E / e** | `3` | `cYb3r` |
| **I / i** | `!`, `1` | `h4ck!ng` |
| **S / s** | `$`, `5` | `p4$$w0rd` |
| **T / t** | `7`, `+` | `3l!73` |
| **O / o** | `0` | `c0d3` |
| **B / b** | `8` | `8r41n` |
| **G / g** | `9` | `9h0$7` |

---

## 🛠 Технологический стек

* **Python 3.12** — язык разработки.
* **`pyperclip`** — межплатформенное взаимодействие с системным буфером обмена.
* **`colorama`** — цветное форматирование консольного вывода.
* **`random`** — генерация энтропии и случайных комбинаций.

---

## 📥 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone [https://github.com/TSMaria04/chaos-gen.git](https://github.com/TSMaria04/chaos-gen.git)
cd chaos-gen

```

### 2. Установка зависимостей
```bash
pip install colorama pyperclip
```

### 3. Запуск скрипта
```bash
python chaos.py
