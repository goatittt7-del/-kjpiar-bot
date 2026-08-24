import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = os.getenv("BOT_TOKEN")

menu = [
    ["📢 Продвижение", "💰 Заработать KJCOIN"],
    ["➕ Добавить канал / бота", "👤 Профиль"],
    ["💳 Пополнить KJCOIN", "💸 Вывод средств"],
    ["ℹ️ Как это работает", "🆘 Поддержка"],
]

keyboard = ReplyKeyboardMarkup(
    menu,
    resize_keyboard=True
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name

    text = f"""
👋 Добро пожаловать, {name}, в KJPIAR!

🎁 Вам начислено 500 KJCOIN — стартовый бонус для первого продвижения.

🪙 KJCOIN — внутренняя валюта сервиса. С её помощью вы можете заказывать:

👥 Подписчиков — от 75 KJCOIN
👁 Просмотры — от 30 KJCOIN
🔥 Реакции — от 100 KJCOIN
🤖 Запуски ботов — от 250 KJCOIN
⚡️ Бусты — от 2 100 KJCOIN

📈 Как работает продвижение?

Вы сами устанавливаете награду за выполнение заказа. Чем выше цена — тем выше ваш заказ располагается в списке заданий и тем быстрее он может быть выполнен.

💰 KJCOIN можно зарабатывать, выполняя задания других пользователей, либо пополнять баланс.

👇 Выберите нужный раздел в меню.
"""

    await update.message.reply_text(
        text,
        reply_markup=keyboard
    )
async def promotion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    promotion_menu = [
        ["📢 Канал", "👥 Группа"],
        ["👁 Пост", "🤖 Бот"],
        ["🔥 Реакции", "⚡ Буст"],
        ["⬅️ Назад"]
    ]

    keyboard = ReplyKeyboardMarkup(
        promotion_menu,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "📢 Что вы хотите рекламировать?",
        reply_markup=keyboard
    )
    

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Regex("^📢 Продвижение$"), promotion))

    app.run_polling()


if __name__ == "__main__":
    main()
