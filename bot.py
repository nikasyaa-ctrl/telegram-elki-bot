from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7948592986:AAEH1NmgtadA8aF1FX-6aOQ6lPvdXLjM4eQ"

# Категории
categories = {
    "Елки ПВХ": ["Дания с белыми кончиками", "Вьюга заснеженная"],
    "Зеленые литые": [
        "Мерида", "Венгрия", "Империя", "Австрия", "Швейцария",
        "Франция зеленая", "Норвегия", "Словения"
    ],
    "Голубые литые": ["Франция голубая"],
    "Заснеженные": [
        "Вьюга заснеженная", "Франция заснеженная", "Нью-Йорк",
        "Мерида", "Франция голубая"
    ]
}

tree_descriptions = {
    "Дания с белыми кончиками": """Ель «Дания с белыми кончиками» ⚡️

➖Данная модель считается бюджетной и самой популярной ёлочкой, но это ни чуть не влияет на её качество. У ёлочки идёт в комплекте пластиковая подставка. Высота ёлочки считается от пола до кончика верхушки вместе с подставкой. 

Состав: сделана из мягкой плёнки ПВХ  
Страна производитель: Россия  
Размеры: 110/140/160/180/200/220/250/300 см  
Цена: от 5665 руб""",

    "Вьюга заснеженная": """Ель «Вьюга заснеженная» ⚡️

Веточки все гнутся, загнув их вниз создаётся впечатление, что они провисли под тяжестью снега. У ёлочки идёт в комплекте металлическая или пластиковая подставка (зависит от размера).

Состав: мягкая плёнка ПВХ с добавлением искусственного снега — флок  
Страна производитель: Россия  
Размеры: 60/70/90/110/140/160/180/220/250/300 см  
Цена: от 4290 руб""",

    "Франция заснеженная": """Ель «Франция заснеженная» ⚡️

Ёлка из литой хвои — все веточки литые. Равномерно заснеженные, с металлической подставкой.

Состав: литая (силиконовая) хвоя  
Страна производитель: Россия  
Размеры: 90/120/150/180/210/250/290 см  
Цена: от 9900 руб""",

    "Остин": """Ель «Остин»

Новинка! Елка относится к классу «ЛЮКС». Очень пышная, много веток, на каждой из которых 7 кончиков. Елка на шарнирной системе, а верхушка на откидной системе. В комплекте металлическая, устойчивая подставка, которая гарантирует устойчивость даже если на елку прыгнет кот.

Состав: сделана из литой (силиконовой) хвои.  
Страна изготовитель: Россия  
Размеры: 150/180/210 см  
Цена: от 13200 руб""",
    
    "Нью-Йорк": """Ель «Нью-Йорк» заснеженная

Елка Нью-Йорк словно только что занесена с улицы, где бушует настоящая метель, настолько густое напыление нанесено на веточки. Материал напыления — хлопок, экологичный и безопасный. Веточки смотрят вниз — уникальная особенность, но игрушки на них держатся отлично.

Состав: литая (силиконовая) хвоя, металлическая подставка  
Страна изготовитель: Россия  
Размеры: 0,9/1,2/1,6/1,8/2,1/2,4/2,7 метра  
Цена: от 9900 руб""",

    "Мерида": """Ель "Мерида"

Шикарная модель Мерида! Полностью отлитая из силикона елочка — это означает, что она прослужит вам вечность! Веточки крупные, как у Нью-Йорка, прокрашены под натуральную елочку: основание коричневое, иголочки темно-зеленые. В комплекте металлическая крестовина.

Состав: литая (силиконовая) хвоя, крупные веточки  
Страна изготовитель: Россия  
Размеры: 150/180/200/230/250/270/300 см  
Цена: от 15900 руб""",

    "Венгрия": """Ель "Венгрия"

Очень пушистая елочка! Кончики лапок чуть светлее основного цвета, основание веточек прокрашено вручную. Зеленый цвет как у натуральной ели с молодыми побегами. Крупные веточки на шарнирной системе.

Состав: литая (силиконовая) хвоя, металлическая подставка  
Страна изготовитель: Россия  
Размеры: 1,5/1,8/2,1/2,25/2,7 метра  
Цена: от 18150 руб""",

    "Империя": """Ель «Империя»

Самая большая ёлка в ассортименте! Пышная, роскошная и максимально реалистичная. Самый большой диаметр у основания — выглядит величественно. Крупные веточки с натуральным окрасом, множество веточек — ёлка густая и объемная. В комплекте надежная металлическая подставка.

Состав: литая силиконовая хвоя  
Размеры: 1,8/2,1/2,3 метра  
Цена: от 20500 руб""",

    "Австрия": """Ель «Австрия»

На шарнирной системе с металлической подставкой для устойчивости. Два вида веточек: длинные с длинными иголочками и веточки с 7 кончиками с короткими иголочками. Диаметр у основания меньше, чем в середине — придает особенную форму.

Состав: полностью из литой силиконовой хвои  
Размеры: 1,8/2,1/2,4/3 метра  
Цена: от 24200 руб""",

    "Швейцария": """Ель «Швейцария»

Самая популярная елка всех времен! Полностью отлита из силикона — это делает её вечной. Шарнирная система креплений и металлическая подставка. Веточки литые, прокрашены как у натуральной ели, на кончиках есть проволока для изменения направления веточек. Даже тяжелые игрушки держатся отлично!

Состав: литая (силиконовая) хвоя  
Размеры: 45/60/70/80/100/120/155/185/215/230/260 см  
Цена: от 4500 руб""",

    "Франция зеленая": """Ель «Франция зеленая»

Очень много веточек, больше чем у «Австрии». Огромный диаметр у основания. Форма — ровный треугольник. Елка на шарнирной системе крепежей.

Состав: литая (силиконовая) хвоя  
Размеры: 180/210/240 см  
Цена: от 26950 руб""",

    "Норвегия": """Ель «Норвегия»

Полностью отлита из силикона, не имеет срока годности, прослужит вечно. Веточки длинные, прокрашены коричневым и темно-зеленым цветом, на шарнирной системе с металлической подставкой. Похож на «Швейцарию», но с менее пышной верхушкой.

Состав: литая (силиконовая) хвоя  
Размеры: 150/180/210/2440/270/300/425 см  
Цена: от 16500 руб""",

    "Франция голубая": """Ель «Франция голубая»

На шарнирной системе, полностью отлита из силикона, служит целую вечность! Широкая у основания, голубой цвет, форма треугольника. Металлическая подставка в комплекте — отличная устойчивость, даже если на елку прыгнет кот!

Состав: литая (силиконовая) хвоя  
Размеры: 180/210/240 см  
Цена: от 26950 руб"""
}

tree_images = {
    "Дания с белыми кончиками": [
        "https://static.tildacdn.com/stor3336-3337-4735-b234-636162633865/88928194.png",
        "https://static.tildacdn.com/stor6530-6432-4239-b134-396462646331/46433576.jpg",
        "https://static.tildacdn.com/stor3335-3962-4961-b833-313065623231/76551528.jpg"
    ],
    "Вьюга заснеженная": [
        "https://static.tildacdn.com/stor3831-3465-4832-b536-333462636433/73057560.jpg",
        "https://static.tildacdn.com/stor6439-6130-4236-b462-646565623062/36266372.jpg",
        "https://static.tildacdn.com/stor3237-3762-4365-a237-656432343630/51380551.jpg"
    ],
    "Франция заснеженная": [
        "https://static.tildacdn.com/stor6431-3232-4761-a530-303733643533/97748665.jpg",
        "https://static.tildacdn.com/stor6331-3737-4230-b534-366566626233/44374970.jpg",
        "https://static.tildacdn.com/stor6164-6266-4164-a331-343063363561/56648029.jpg"
    ],
    "Остин": [
        "https://static.tildacdn.com/stor6363-3430-4263-b037-333265356366/93077614.webp",
        "https://static.tildacdn.com/stor3231-6565-4864-b762-656261623564/78017320.webp",
        "https://static.tildacdn.com/stor6665-6263-4535-b938-663565343666/47348652.webp"
    ],
    "Нью-Йорк": [
        "https://static.tildacdn.com/stor3831-3965-4863-a639-336166393132/42318448.jpg",
        "https://static.tildacdn.com/stor3030-3964-4366-b033-393561613061/46718534.jpg",
        "https://static.tildacdn.com/stor3033-3330-4136-b933-303538316462/74442968.jpg"
    ],
    "Мерида": [
        "https://static.tildacdn.com/stor3230-3335-4630-a339-656135353137/90060924.jpg",
        "https://static.tildacdn.com/stor3266-3231-4539-a233-363263383835/17162307.jpg",
        "https://static.tildacdn.com/stor6633-3465-4065-a265-383135653936/32299409.jpg"
    ],
    "Венгрия": [
        "https://static.tildacdn.com/stor3765-3364-4061-b132-623733663236/40765044.jpg",
        "https://static.tildacdn.com/stor3239-3862-4635-b562-656337366661/69880920.jpg",
        "https://static.tildacdn.com/stor3432-3932-4264-a161-326337313530/71620266.jpg"
    ],
    "Империя": [
        "https://static.tildacdn.com/stor3534-6630-4333-b634-616439363633/97123545.jpg",
        "https://static.tildacdn.com/stor3639-3763-4035-a432-623832613165/60214215.jpg",
        "https://static.tildacdn.com/stor3934-3562-4337-b337-303265373162/46154610.jpg"
    ],
    "Австрия": [
        "https://static.tildacdn.com/stor3365-3562-4235-b064-643062643162/32054610.jpg",
        "https://static.tildacdn.com/stor3837-3035-4239-b535-663836366437/37065967.jpg",
        "https://static.tildacdn.com/stor6135-3666-4335-b332-613431323161/31631709.jpg"
    ],
    "Швейцария": [
        "https://static.tildacdn.com/stor6433-3561-4166-a634-663762326665/97086744.webp",
        "https://static.tildacdn.com/stor3161-3461-4938-a432-303864303164/87274393.webp",
        "https://static.tildacdn.com/stor3761-3631-4533-a330-366166656334/18040736.webp"
    ],
    "Франция зеленая": [
        "https://static.tildacdn.com/stor6166-3865-4135-b264-633139316336/25587986.jpg",
        "https://static.tildacdn.com/stor6635-3663-4531-a663-393738306538/15707046.jpg",
        "https://static.tildacdn.com/stor6332-6563-4331-b161-383038366337/43103698.jpg"
    ],
    "Норвегия": [
        "https://static.tildacdn.com/stor3834-3964-4064-a363-656131316439/76225993.jpg",
        "https://static.tildacdn.com/stor6632-3731-4738-b763-323330313630/33830736.jpg",
        "https://static.tildacdn.com/stor3163-6434-4566-b266-376234313330/63081288.jpg"
    ],
    "Франция голубая": [
        "https://static.tildacdn.com/stor3430-3663-4430-b562-663263316566/66332652.jpg",
        "https://static.tildacdn.com/stor6438-3534-4136-b637-663736666164/51719203.jpg",
        "https://static.tildacdn.com/stor3064-3664-4266-b864-643033333735/88735670.jpg"
    ]
}

async def show_tree_description(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tree_name = update.message.text
    description = tree_descriptions.get(tree_name, "Описание не найдено.")
    images = tree_images.get(tree_name, [])

    contact_button = KeyboardButton("📞 Связаться с продавцом")
    back_button = KeyboardButton("⬅️ Назад")
    reply_markup = ReplyKeyboardMarkup([[contact_button], [back_button]], resize_keyboard=True)

    if images:
        for img_url in images:
            await update.message.reply_photo(photo=img_url)
        await update.message.reply_text(description, reply_markup=reply_markup)
    else:
        await update.message.reply_text(description, reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text in categories:
        trees = categories[text]
        keyboard = [[KeyboardButton(name)] for name in trees]
        keyboard.append([KeyboardButton("⬅️ Назад")])
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Выберите ёлку:", reply_markup=reply_markup)
        return  # Возвращаемся, чтобы не выполнять дальше

    elif text in tree_descriptions:
        await show_tree_description(update, context)
        return

    elif text == "⬅️ Назад":
        keyboard = [[KeyboardButton(cat)] for cat in categories.keys()]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Выберите категорию:", reply_markup=reply_markup)
        return

    elif text == "📞 Связаться с продавцом":
        await update.message.reply_text("Связаться с продавцом можно тут 👉 @dockiselev")
        return

    else:
        await update.message.reply_text("Не понял вас 🤔 Попробуйте выбрать из списка.")
        return
    # Если ввели что-то непонятное
    await update.message.reply_text("Пожалуйста, выберите вариант с клавиатуры.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton(cat)] for cat in categories.keys()
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Выберите категорию"
    )

    await update.message.reply_text(
        "👋 Привет! Я ёлочный бот. Помогу выбрать идеальную ёлку 🎄\nВыберите категорию ниже:",
        reply_markup=reply_markup
    )
    keyboard = [
        [KeyboardButton(cat)] for cat in categories.keys()
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Выберите категорию"
    )

async def send_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    channel_id = "@push_elka"  # Замените на юзернейм вашего канала

    if context.args:
        text = ' '.join(context.args)
    else:
        text = "Новогодние ёлки уже в продаже! 🎄 Выберите свою и закажите прямо сейчас."

    keyboard = [
        [InlineKeyboardButton("Заказать", url=f"https://t.me/{context.bot.username}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(chat_id=channel_id, text=text, reply_markup=reply_markup)
    await update.message.reply_text("Пост с кнопкой отправлен в канал.")

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CommandHandler("sendchannel", send_to_channel))

    app.run_polling()

if __name__ == "__main__":
    main()