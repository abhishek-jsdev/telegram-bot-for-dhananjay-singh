const TELEGRAM_BOT_USERNAME = "@HerryNoharaBot",
  TELEGRAM_BOT_TOKEN = "6234414329:AAHJUFeOulbBl5nkrFCluikD-uvRTUwZn7Q";

/**
 * https://api.telegram.org/bot6234414329:AAHJUFeOulbBl5nkrFCluikD-uvRTUwZn7Q/getUpdates
 * https://api.telegram.org/bot6234414329:AAHJUFeOulbBl5nkrFCluikD-uvRTUwZn7Q/sendMessage?chat_id=977022300&text=MESSAGE_TEXT
 * https://api.telegram.org/bot6234414329:AAHJUFeOulbBl5nkrFCluikD-uvRTUwZn7Q/sendMessage?chat_id=1315464303&text=Did you saw our 5 year old son named Shinchan Nohara
 */

import TelegramBot from "node-telegram-bot-api";
import unshorter from "unshorter";

const bot = new TelegramBot(TELEGRAM_BOT_TOKEN, { polling: true });

bot.sendMessage("@SlothPANDAkoala", "hii");

const shortUrl = "https://s.id/aliazhar-github";

unshorter(shortUrl)
  .then((longUrl) => console.info("Result:", longUrl))
  .catch((err) => console.error("Oops!"));
