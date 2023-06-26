const { TelegramClient } =require("telegram");
const { StringSession } =require("telegram/sessions");
const input = require("input");

const apiId = 20340026;
const apiHash = "d1c2010562443ded33c1f4fa64f16bc4";
const stringSession = new StringSession(""); // fill this later with the value from session.save()

(async () => {
  console.log("Loading interactive example...");
  const client = new TelegramClient(stringSession, apiId, apiHash, {
    connectionRetries: 5,
  });
  await client.start({
    phoneNumber: async () => await input.text("Please enter your number: "),
    password: async () => await input.text("Please enter your password: "),
    phoneCode: async () =>
      await input.text("Please enter the code you received: "),
    onError: (err) => console.log(err),
  });
  console.log("You should now be connected.");
  console.log(client.session.save()); // Save this string to avoid logging in again
  await client.sendMessage("me", { message: "Hello!" });
})();


// import unshorter from "unshorter";

// const shortUrl = "https://s.id/aliazhar-github";

// unshorter(shortUrl)
//   .then((longUrl) => console.info("Result:", longUrl))
//   .catch((err) => console.error("Oops!"));
