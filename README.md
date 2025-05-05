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

# How to use
Create user list file

![image](https://github.com/user-attachments/assets/5af99606-ed6c-43b8-a31d-36b8ae4467ed)

Generating email

```python3 name2user.py -d demo.test -u user.txt```

![image](https://github.com/user-attachments/assets/e1877f30-836e-44d2-ae65-b78a138913c7)


Generating email and output to a file

```python3 name2user.py -d demo.test -u user.txt -o email-list.txt```

![image](https://github.com/user-attachments/assets/1a077799-9928-483a-bcef-c0523aa91dde)

![image](https://github.com/user-attachments/assets/9a313c99-d6c4-4b7a-878d-03c5ac2e4676)


Generating usernames

```python3 name2user.py -u user.txt```

![image](https://github.com/user-attachments/assets/57b2f574-4650-4904-9f61-a11bcd8157a8)


Generating usernames and output to a file

```python3 name2user.py -u user.txt -o user-list.txt```

![image](https://github.com/user-attachments/assets/dd43400c-8073-404e-b725-8de933290357)

![image](https://github.com/user-attachments/assets/639f5aad-ad94-45fc-b06d-886c380bc736)






