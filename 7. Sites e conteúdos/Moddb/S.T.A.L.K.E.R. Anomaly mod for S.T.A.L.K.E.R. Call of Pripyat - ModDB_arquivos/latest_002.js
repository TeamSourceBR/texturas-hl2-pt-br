var scr = document.createElement('script');
scr.async = true;
scr.type = 'text/javascript';
var now = Date.now();
try {
  if(window.sessionStorage){
    now = window.sessionStorage.getItem('latest_ts') || now;
    window.sessionStorage.setItem('latest_ts', now);
  }
} catch (e){}
scr.src = 'https://static.kueezrtb.com/js/latest.js?_=' + now;
var node = document.getElementsByTagName('script')[0];
node.parentNode.insertBefore(scr, node);