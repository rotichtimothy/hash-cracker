# 🔓 Hash Cracker - Web App

A simple yet educational **password hash cracker** built with Python and Flask. This web app demonstrates how cryptographic hashes can be cracked using **dictionary attacks** and **brute force methods**, helping users understand why weak passwords and outdated hashing algorithms are dangerous.

> ⚠️ **Disclaimer:** This project is for **educational purposes only**. Do not use it on hashes or systems you do not own or have explicit permission to test.

---

## ✨ Features

- 🔑 **Hash Generator** – Generate MD5, SHA1, and SHA256 hashes for testing
- 📖 **Dictionary Attack** – Crack hashes using a wordlist (e.g., rockyou.txt)
- 🔨 **Brute Force Attack** – Try every combination with configurable charset & length
- 🧠 **Auto Hash Detection** – Automatically detects MD5, SHA1, or SHA256 based on hash length
- ⏱️ **Performance Stats** – Displays attempts made and time taken
- 🎨 **Clean UI** – Simple dark-themed interface

---

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask
- **Frontend:** HTML, CSS, JavaScript (Vanilla)
- **Hashing:** Python's built-in `hashlib`

---

## 📁 Project Structure

```
hash-cracker/
├── app.py                  # Flask server
├── cracker.py              # Core cracking logic
├── requirements.txt        # Python dependencies
├── .gitignore
├── README.md
├── wordlists/
│   └── rockyou-small.txt   # Sample wordlist
├── templates/
│   └── index.html          # Frontend UI
└── static/
    └── style.css           # Styling
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rotichtimothy/hash-cracker.git
   cd hash-cracker
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add a wordlist**
   A small sample wordlist is included in `wordlists/rockyou-small.txt`.
   For better results, download a larger wordlist (like the full `rockyou.txt`) and place it in the `wordlists/` folder.

5. **Run the app**
   ```bash
   python app.py
   ```

6. **Open in your browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 🧪 How to Use

### 1. Generate a Test Hash
- Enter any text (e.g., `password`)
- Choose an algorithm (MD5, SHA1, or SHA256)
- Click **Generate Hash**

Example output for `password` (MD5):
```
5f4dcc3b5aa765d61d8327deb882cf99
```

### 2. Crack the Hash
- Paste the hash in the **Crack a Hash** section
- Choose your method:
  - **Dictionary Attack** → uses your wordlist
  - **Brute Force** → choose charset and max length
- Click **Crack It!** and watch the magic happen 🎉

---

## 🧠 Concepts Demonstrated

| Concept | Explanation |
|---------|-------------|
| **Hashing is one-way** | You can't reverse a hash — you can only guess inputs |
| **Weak passwords are insecure** | Common passwords get cracked in milliseconds |
| **MD5 & SHA1 are outdated** | They're fast = easy to brute force |
| **No salt = vulnerable** | Identical passwords produce identical hashes |
| **Modern alternatives** | Use **bcrypt**, **Argon2**, or **PBKDF2** for password storage |

---

## 📊 Example Test Cases

| Plaintext | Algorithm | Hash | Crackable? |
|-----------|-----------|------|------------|
| `password` | MD5 | `5f4dcc3b5aa765d61d8327deb882cf99` | ✅ Instantly (dictionary) |
| `abc` | SHA1 | `a9993e364706816aba3e25717850c26c9cd0d89d` | ✅ Brute force (a-z, len 3) |
| `123456` | SHA256 | `8d969eef6ecad3c29a3a629280e686cf...` | ✅ Instantly (dictionary) |

---

## 📚 Learning Resources

- [OWASP: Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [Why MD5 is broken](https://en.wikipedia.org/wiki/MD5#Security)
- [Python hashlib documentation](https://docs.python.org/3/library/hashlib.html)
- [How password hashing works](https://auth0.com/blog/hashing-passwords-one-way-road-to-security/)

---

## ⚖️ Legal & Ethical Notice

This tool is intended **strictly for educational and research purposes**. Cracking hashes you don't own or don't have permission to test is **illegal** and unethical. The author assumes no liability for misuse.

By using this tool, you agree to:
- Use it only on hashes you own or have explicit permission to test
- Not use it for any malicious or unauthorized activities
- Take full responsibility for your actions

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repo
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

⭐ **If you found this project useful, please give it a star on GitHub!** ⭐