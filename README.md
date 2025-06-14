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

🧪 How to Run
🪟 Step 1: Setup packet forwarding
Open a terminal and run:

Copy code
sudo service apache2 start
sudo iptables --flush
sudo iptables -I FORWARD -j NFQUEUE --queue-num 0

🧾 Step 2: Run the interceptor script
sudo python3 file_intercepter.py
🌐 Step 3: Enable IP forwarding
In another terminal, run:
echo 1 > /proc/sys/net/ipv4/ip_forward

---

📚 What This Script Does

- Monitors HTTP traffic using Scapy and NetfilterQueue.
- Detects download requests for `.exe` files.
- Stores the ACK number of those requests.
- When a response with the matching SEQ number is detected, it **replaces the response** with a **301 redirect** to a custom `.exe` file.

---

## 🔍 Important Notes
- Only works on HTTP traffic (not HTTPS).
- Make sure your iptables rules are correctly set.
- Requires `root` privileges to run due to packet manipulation.
