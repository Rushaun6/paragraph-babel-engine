# Paragraph Babel Engine

Paragraph Babel Engine is a simple Python project that encodes paragraphs into a long key and allows them to be decoded and searched later. The goal of the project is to demonstrate basic concepts such as text normalization, encoding systems, command line tools, and automated testing with GitHub.

---

## Features

- Encode paragraphs into a unique key
- Decode keys back into readable text
- Search words inside encoded data
- Search across multiple encoded paragraphs
- Command-line tools for easy use
- Automated testing with GitHub Actions

---

## Project Structure

```
paragraph-babel-engine
│
├── babel_engine.py      # Encoding and decoding logic
├── encode.py            # Generate a key from text
├── scanner.py           # Decode a key from terminal
├── search.py            # Search for a word in encoded text
├── search_index.py      # Search across multiple encoded paragraphs
├── test_engine.py       # Automated test script
└── .github/workflows    # GitHub Actions CI workflow
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Rushaun6/paragraph-babel-engine.git
cd paragraph-babel-engine
```

Make sure Python is installed on your system.

---

## Usage

### Encode a Paragraph

Run the following command:

```bash
python encode.py "Technology continues to change the way people communicate."
```

This will generate a key representing the encoded paragraph.

---

### Decode a Key

To decode a key back into readable text:

```bash
python scanner.py KEY_HERE
```

---

### Search Inside Encoded Text

You can search for a word inside encoded text without manually decoding everything.

Example:

```bash
python search.py science KEY_HERE
```

Example output:

```
Word found 1 time(s)!

Decoded text preview:
technology continues to change the way people communicate...
```

---

### Search Across Multiple Encoded Paragraphs

Store multiple keys inside a file called `database.txt`.

Example:

```
KEY1
KEY2
KEY3
```

Then run:

```bash
python search_index.py science
```

This will search all stored encoded paragraphs for the word.

---

## Example

Original text:

```
Technology continues to change the way people communicate and share ideas.
```

Encoded key:

```
NO0CSvs256yjbBcYuI9nGPcFhBJsbbdNlNHQ2tBO...
```

Search result:

```
Word found 1 time(s)!
```

---

## Automated Testing

The project uses GitHub Actions to automatically run tests whenever new code is pushed.

Workflow:

```
Push code
   ↓
GitHub Actions runs
   ↓
test_engine.py executes
   ↓
Encode → Decode test
   ↓
Pass or Fail
```

This ensures the encoding and decoding system always works correctly.

---

## Purpose

This project was created as a learning experiment in:

- Python scripting
- Text encoding systems
- Command line tools
- Searchable encoded data
- Continuous integration with GitHub

---

## License

MIT License
