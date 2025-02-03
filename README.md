# 🤖 Telegram Sarcasm Detector Bot

This is a Telegram bot that detects sarcasm in text messages using a **RoBERTa-based sarcasm detection model**. Simply send a message, and the bot will analyze and return its sarcasm probability.

---

## 📌 Features
✔️ Uses **jkhan447/sarcasm-detection-RoBerta-base-CR** for sarcasm detection.  
✔️ Returns sarcasm probability as a percentage.  
✔️ Works with natural language text inputs.  
✔️ Simple and easy to use via Telegram.  

---

## 🛠 Installation & Setup

### 1️⃣ Clone the repository:
```bash
git clone https://github.com/your-repo/sarcasm-detector-bot.git
cd sarcasm-detector-bot
```

### 2️⃣ Install dependencies:
```bash
pip install python-telegram-bot transformers torch
```

### 3️⃣ Set up the bot:
- Get your **Telegram Bot Token** from [@BotFather](https://t.me/BotFather) on Telegram.
- Replace `YOUR_BOT_TOKEN` in `main()` with your actual bot token.

### 4️⃣ Run the bot:
```bash
python bot.py
```

---

## 🎯 Usage
1. Start the bot on Telegram using `/start`.
2. Send any text message.
3. The bot will analyze the message and return:
   - `"Sarcasm Detected! 😏"` if sarcasm probability is **above 50%**.
   - `"Not Sarcasm. 😊"` if sarcasm probability is **below 50%**.

---

## 🚀 Deployment (Optional)
For continuous running, deploy on a server:
- **Using PythonAnywhere**
- **Using AWS Lambda**
- **Using Docker**

---

## 🔍 Model Details
- **Model:** `jkhan447/sarcasm-detection-RoBerta-base-CR`
- **Pretrained Transformer:** RoBERTa
- **Tokenizer & Model Used for Inference**

---

## 📜 License
This project is **open-source** and available under the MIT License.

---

## ✨ Credits
- Developed by **Vedant**
- **Telegram Bot API** used for interaction.
- **Hugging Face Transformers** used for NLP model inference.

---

📬 For any issues, open an **[Issue](https://github.com/your-repo/sarcasm-detector-bot/issues)** in the repository!
