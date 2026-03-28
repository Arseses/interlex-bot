import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import asyncio

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен вашего бота
BOT_TOKEN = "8643588873:AAFQDZwl6NP3V2_7B1tf6K2a7SL9i5xcdes"

# ========== ТЕКСТЫ ДЛЯ КНОПОК ==========

TEXTS = {
    "description": (
        "📚 *Описание программы*\n\n"
        "**Направление подготовки:** 45.03.02 Лингвистика\n"
        "**Отрасль:** Гуманитарные науки\n"
        "**Институт:** Уральский гуманитарный институт\n"
        "**Уровень образования:** Бакалавриат\n"
        "**Язык обучения:** Русский\n"
        "**Форма и срок обучения:** Очная, 4 года\n\n"
        "Кафедра иностранных языков и перевода уже более 25 лет готовит специалистов.\n\n"
        "🎯 *Цель программы:* подготовка специалистов, владеющих тремя языками."
    ),
    
    "languages": (
        "🌐 *Изучаемые языки*\n\n"
        "**1️⃣ Первый язык:** Английский или Немецкий\n"
        "**2️⃣ Второй язык:** Английский, Немецкий, Французский, Испанский, Китайский\n"
        "**3️⃣ Третий язык:** Английский, Немецкий, Французский, Испанский, Китайский, Корейский"
    ),
    
    "curriculum": (
        "📖 *Что изучают*\n\n"
        "• Практический курс иностранных языков\n"
        "• Теория и практика перевода\n"
        "• Межкультурная коммуникация\n"
        "• Устный и письменный перевод\n"
        "• Основы методики преподавания"
    ),
    
    "scores": (
        "✅ *Минимальные баллы 2026*\n\n"
        "Иностранный язык: 40\n"
        "Русский язык: 40\n"
        "История/Литература: 40\n"
        "Обществознание: 45\n\n"
        "Бюджетных мест: 7"
    ),
    
    "partners": (
        "🤝 *Партнеры и работодатели*\n\n"
        "• Союз переводчиков России\n"
        "• УГМК-Холдинг\n"
        "• Уральская ТПП\n"
        "• Генеральное консульство КНР\n"
        "• Балтийский федеральный университет"
    ),
    
    "contacts": (
        "📞 *Контакты*\n\n"
        "Горячая линия: 8 905 800 35 95 (WhatsApp)\n"
        "ВКонтакте: официальное сообщество УрФУ\n"
        "Адрес: УрФУ, Уральский гуманитарный институт"
    ),
    
    "welcome": (
        "🌟 *Добро пожаловать!* 🌟\n\n"
        "Я бот программы **«Перевод и межкультурная коммуникация»**\n"
        "🏛 *Уральского федерального университета (УрФУ)*\n\n"
        "Выберите раздел:"
    )
}

def get_main_keyboard():
    keyboard = [
        [InlineKeyboardButton("📚 Описание программы", callback_data="description")],
        [InlineKeyboardButton("🌐 Изучаемые языки", callback_data="languages")],
        [InlineKeyboardButton("📖 Что изучают", callback_data="curriculum")],
        [InlineKeyboardButton("✅ Минимальные баллы", callback_data="scores")],
        [InlineKeyboardButton("🤝 Партнеры", callback_data="partners")],
        [InlineKeyboardButton("📞 Контакты", callback_data="contacts")],
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        TEXTS["welcome"],
        parse_mode="Markdown",
        reply_markup=get_main_keyboard()
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = TEXTS.get(query.data, "Информация")
    await query.edit_message_text(
        text,
        parse_mode="Markdown",
        reply_markup=get_main_keyboard()
    )

def main():
    try:
        # Создаем приложение
        app = Application.builder().token(BOT_TOKEN).build()
        
        # Добавляем обработчики
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(button_callback))
        
        print("✅ Бот запущен!")
        logger.info("🚀 Бот запущен!")
        
        # Запускаем
        app.run_polling()
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        logger.error(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
