# JSON Research

## What does it stand for?
**JSON** stands for **JavaScript Object Notation**.

## What is it used for?
JSON is a lightweight format for storing and exchanging data. It is most commonly used to send data between a server and a web application (e.g. API responses), and also for configuration files and simple data storage.

## What is it written in?
JSON is plain text. It is language-independent, but its syntax is derived from JavaScript object literals. Files use the `.json` extension, and almost every programming language can read and write it.

## Advantages of using it
- **Easy to read and write** for humans
- **Lightweight**, so it is quick to send over a network
- **Language-independent**, supported by nearly all languages
- **Easy to parse**, with built-in support in JavaScript and libraries elsewhere
- **Structured**, so it can represent nested, complex data

## Data types it can store
| Type | Example |
|---|---|
| String | `"Hello"` |
| Number | `42`, `3.14` |
| Boolean | `true`, `false` |
| Null | `null` |
| Object | `{ "a": 1 }` |
| Array | `[1, 2, 3]` |

## JSON syntax

### Name/value pairs
A key (always a string in double quotes), a colon, then the value:
```json
"name": "Alice"
```

### Objects
Wrapped in curly braces `{ }` and contain name/value pairs:
```json
{
  "name": "Alice",
  "age": 25
}
```

### Separating data
Key/value pairs are separated by **commas**. There is no comma after the last pair:
```json
{
  "name": "Alice",
  "age": 25,
  "student": true
}
```

### Arrays
Wrapped in square brackets `[ ]`, with values separated by commas. Arrays can hold any type, including objects:
```json
{
  "colours": ["red", "green", "blue"],
  "people": [
    { "name": "Alice", "age": 25 },
    { "name": "Bob", "age": 30 }
  ]
}
```

## Key rules
- Keys must use **double quotes** (not single quotes)
- No trailing commas
- No comments allowed