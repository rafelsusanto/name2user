# name2user
Generate common corporate email and username combinations from full names.

<br>

## 🔧 Installation

1. Clone the repository using the following command:

```bash
git clone https://github.com/rafelsusanto/name2user.git
cd name2user
```


2. Ensure you have Python 3 installed. You can check your Python version with:
```bash
python3 --version
```

<br>

## 🚀 Features

- Supports names with 1, 2, or 3 components (e.g., first name, first and last name, or full name including middle).
- Generates common patterns using separators like `.`, `_`, and `-`.
- Automatically deduplicates results to avoid repetitions.
- Optional domain (`-d`) to append to usernames.
- Optional output file (`-o`) to save the generated list.

<br>

## 📄 Usage

```bash
python3 name2user.py -u users.txt [-d DOMAIN] [-o OUTPUT_FILE]
```

<br>

## 🔧 Examples
```
#1
python3 name2user.py -u user.txt -d demo.test

#2
python3 name2user.py -u user.txt -d demo.test -o email-list.txt

#3
python3 name2user.py -u user.txt

#4
python3 name2user.py -u user.txt -o user-list.txt
```

<br>

## 📝 Input File Format
The input file (user.txt) should contain one name per line. Names can be single, double, or triple word:

![image](https://github.com/user-attachments/assets/f49a021e-2f20-4efe-b605-a8eac5c623de)

<br>

## 📦 Output Examples
```
##Example: Generate Email List from Names with One, Two, or Three Words
python3 name2user.py -u user.txt -d demo.test
```

![image](https://github.com/user-attachments/assets/bd38af8d-f48d-439b-98e5-4133dadfa878)








