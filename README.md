# 🔁 File Intercepter - Replace Downloads on the Fly

This Python script intercepts HTTP downloads of `.exe` files and redirects them to a specified link using NetfilterQueue and Scapy.

⚠️ For educational and ethical hacking purposes only.

---

## 🧠 How It Works
- Listens to network packets using `netfilterqueue`.
- Intercepts HTTP requests for `.exe` files.
- Replaces the response with a redirection to a custom file download.

---

## ⚙️ Requirements

Install dependencies:
```bash
pip install scapy NetfilterQueue
