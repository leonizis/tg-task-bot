import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

openai.api_key = 'OPENAI_API_KEY'

async def start(update: Update, context):
    await update.message.reply_text("Бот готов! Добавьте задачи.")

async def add_task(update: Update, context):
    user_text = update.message.text
    # обработка задачи через OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Определи задачи"},
            {"role": "user", "content": user_text},
        ]
    )
    await update.message.reply_text(f"Задача: {response.choices[0].message.content}")

if __name__ == '__main__':
    app = ApplicationBuilder().token('BOT_TOKEN').build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, add_task))
    app.run_polling()
