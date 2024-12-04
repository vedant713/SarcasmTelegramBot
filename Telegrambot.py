from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import string

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("jkhan447/sarcasm-detection-RoBerta-base-CR")
model = AutoModelForSequenceClassification.from_pretrained("jkhan447/sarcasm-detection-RoBerta-base-CR")

# Preprocess text input
def preprocess_data(text: str) -> str:
    return text.lower().translate(str.maketrans("", "", string.punctuation)).strip()

# Function to predict sarcasm
def predict_sarcasm(user_input, model=model, tokenizer=tokenizer):
    try:
        tokenized_text = tokenizer([preprocess_data(user_input)], padding=True, truncation=True, max_length=256, return_tensors="pt")
        output = model(**tokenized_text)
        probs = output.logits.softmax(dim=-1).tolist()[0]
        sarcasm_probability = round(probs[1] * 100, 2)
        return sarcasm_probability
    except Exception as e:
        return f"Error occurred: {str(e)}"

# Telegram bot handlers
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hi! I'm a Sarcasm Detector bot. Send me a message, and I'll tell you how sarcastic it is!Haha made by vedant xd")

async def analyze_sarcasm(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    sarcasm_score = predict_sarcasm(user_input)
    if isinstance(sarcasm_score, str):
        await update.message.reply_text(sarcasm_score)  # Display error message
    else:
        result = "Sarcasm Detected! 😏" if sarcasm_score > 50 else "Not Sarcasm. 😊"
        await update.message.reply_text(f"Result: {result}\nSarcasm Probability: {sarcasm_score}%")

# Main function to start the bot
def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
    application = Application.builder().token("7483234434:AAEZuCfL-IHXUII5DblKXM5k8KtEMMt-d2g").build()

    # Register command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, analyze_sarcasm))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
