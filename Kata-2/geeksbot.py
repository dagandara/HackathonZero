from telegram.ext import Updater, CommandHandler
def main():
    #Inicamos el updater
    updater = Updater(token="1191933043:AAHcWYyfxvEN5QDHFwOz-tMVwzgBdgnuulE", use_context=True)
    
    #Anadiendo comando /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    #Añadir manejador para el comando /repite
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    #Añadir manejador para el comando /suma
    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    #Empezamos a pedir notificaciones a Telegram
    updater.start_polling()

    #Capturamos señales de parada
    updater.idle()

#Definimos qué hace el comando start
def start(update, context):
    update.message.reply_text("Hola ¿Cómo estás?")

#Definimos qué hace el comando repite
def repite(update, context):
    update.message.reply_text(update.message.text)

#Definimos qué hace el comando suma
def suma(update, context):
    #context.args saca los elementos de un listado de palabras los args serían [2, 2]
    #args = [2, 2]
    resultado = int(context.args[0]) + int(context.args[1])
    update.message.reply_text("El resultado es: " + str(resultado))

main()