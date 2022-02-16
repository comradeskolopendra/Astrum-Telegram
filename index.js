// вызывающий скрипт через питон
// const { Api, TelegramClient } = require("telegram");
// const { StringSession } = require("telegram/sessions");
// const input = require("input"); // npm i input
// var EventLogger = require('node-windows').EventLogger;
// let logThread = new EventLogger('Astrum-Telegram-3.0')

// const apiId = 12338108;
// const apiHash = '7a93a8eb9e0b2738edb502fe752b8f32';
// const stringSession = new StringSession("1AgAOMTQ5LjE1NC4xNjcuNDEBuzaNb4iy8dseXJYMzi87o3Mp9oSE7Uqrk+/+LWk/koiVpQ4J5Piga1qei5N2FGBl753jMxs93K1yS02nwZIVhtUVK6VPXpGHrdKHfA0umKyXPQqBzY1XZrHh6DnZuVNNyLO9EtuKwu7EQODCm60H52Dttp958WLHtIrTZvPEVBFAyyb56PIFkfZ38r4MIGeXjJ6YrAPzxqkQJATBkuDyuT7AXBvK45v1rX39WtcCE98HJjS3B58ycckyietCjUDC4QrE81Sa4OD62QttuXS+JItKlRTrYhpCXCOzRi0crrkCpsQfhAmhalvxG28sheSFMmPH9inUHs8pCLHzWAhKxlI="); // fill this later with the value from session.save()

// // setInterval(() => {
// //     logThread.info('[LOGGER]')
// //     console.log(phone_list)
// // }, 500)


// (async () => {
//     console.log("Loading interactive example...");
//     const client = new TelegramClient(stringSession, apiId, apiHash, {
//         connectionRetries: 5,
//     });
//     await client.start({
//         phoneNumber: async () => await input.text('Please enter your phone: '),
//         password: async () => await input.text("Please enter your password: "),
//         phoneCode: async () =>
//             await input.text("Please enter the code you received: "),
//         onError: (err) => console.log(err),
//     });
//     console.log("Вы подключились к телеграму.");
//     console.log(result); // prints the result
//     setInterval(() => {
//         client.sendMessage("me", { message: "Работает" });
//         logThread.info('Working')
//     }, 1000)
// })();