const { PythonShell } = require('python-shell');
var EventLogger = require('node-windows').EventLogger;
let logThread = new EventLogger('Astrum-Telegram-3.0')

setInterval(() => {logThread.info('[Logger]')}, 1000)

setInterval(() => {
    PythonShell.run('script.py', null, function (err, results) {
        if (err) throw err;
        logThread.info(`[results: ${results}]`);
      });
}, 5000)