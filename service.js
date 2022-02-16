// Служба windows - в не рабочем состоянии

var Service = require('node-windows').Service;

var svc = new Service({
  name:'Astrum-Telegram-3.0',
  description: 'Testing',
  script: 'C:\\Users\\ComradeSkolopendra\\Desktop\\python github\\pyshell\\index.js',
});

svc.on('install', function(){
  svc.start()
});

// svc.install();
svc.uninstall();

console.log('{Code succes!}')