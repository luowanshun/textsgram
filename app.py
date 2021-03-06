from flask import Flask, request
from telegram.ext import Dispatcher, CommandHandler
from translate import translate
import telegram
from config import TOKEN, APP_KEY, APP_SECRET
app = Flask(__name__)

bot = telegram.Bot(token=TOKEN)
dispatcher = Dispatcher(bot,None, use_context=True)

@app.route('/textsgram', methods=['POST'])
def handle():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
        return 'ok', 200
    return 'successful'

def trans(update, context):
    result = translate(context.args[0])
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)

dispatcher.add_handler(CommandHandler('trans', trans))

if __name__ == "__main__":
    app.run(debug=False,port=4999)
