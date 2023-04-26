var c = document.getElementById("playground");
var dotButton = document.getElementById("circle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("stop");

var ctx = c.getContext("2d");

ctx.fillStyle = "blue";

var requestID;

var clear = (e) => {
    //e.preventDefault();
    ctx.clearRect(0, 0, 1000, 1000);
};

var dvdLogoSetup = () => {
    window.cancelAnimationFrame(requestID);

    var rectWidth = 60;
    var rectHeight = 40;

    var rectX = (c.width - rectWidth) * Math.random();
    var rectY = (c.height - rectHeight) * Math.random();

    var xVel = 2;
    var yVel = 3;

    var logo = new Image();
    logo.src = "logo_dvd.jpg"

    var dvdLogo = () =>{
        clear()
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
        if (rectX < 0 || rectX > c.width - rectWidth){
            xVel = -xVel;
        }
        if (rectY < 0 || rectY > c.height - rectHeight){
            yVel = -yVel;
        }
        rectX += xVel;
        rectY += yVel;
        requestID = window.requestAnimationFrame(dvdLogo)
    }
    dvdLogo();
}

var radius = 0;
var maxRadius = 250;
var growing = true;

var drawDot = () => {
    clear();

    if (growing && radius+1 > maxRadius) {
        growing = false;
    } else if (!growing && radius-1 < 0) {
        growing = true;
    }

    if (growing) {
        radius++; 
    } else {
        radius--;
    }

    ctx.beginPath();
    ctx.arc(maxRadius, maxRadius, radius, 0, Math.PI*2, true);
    ctx.fill();
    ctx.closePath();

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
}

var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    window.cancelAnimationFrame(requestID)
}

dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", dvdLogoSetup)
stopButton.addEventListener("click", stopIt);