
window.onload = function(){
/*     var canvas = document.getElementById("canvas");

    function onClick(e) {
        console.log("click");
    }
    canvas.addEventListener('click', onClick, false);
    canvas.fillText("Hello", 0, 0); */
    var url = location.href;
    var url_pwd = url.split('/').filter(e => Boolean(e));
    var png_name = url_pwd[url_pwd.length - 1]; 

    var img = new Image();
    img.src = 'static/img/' + png_name + '.png';

    var pin = new Image();
    pin.src = 'static/CreatePainting/pin.png'

    var canvas = document.getElementById('canvas');
    var element = document.getElementById('element');
 
    var context = canvas.getContext('2d');
    var el = element.getContext('2d');

    img.onload = function(){
        context.drawImage(img, 0, 0, canvas.width, canvas.height);
        pin.onload = function(){
            context.drawImage(pin, 100, 100, 40, 40);
        }
    }

    el.font = "15px serif";
    el.fillText("クリックした座標は以下の通りです", 0, 40);
    var line_y = 40;

    function onClick(e){
        var x = e.clientX - canvas.offsetLeft;
        var y = e.clientY - canvas.offsetTop;
        var point = "x: " + x + "　　y: " + y;
        line_y += 20;
        if(line_y > canvas.height){
            line = 20;
        }
        el.fillText(point, 0, line_y);
        
        img.onload = function(){
            context.drawImage(img, 0, 0, canvas.width, canvas.height);
            pin.onload = function(){
                context.drawImage(pin, x, y, 40, 40);
            }
        }
    }

    canvas.addEventListener('click', onClick, false);
};