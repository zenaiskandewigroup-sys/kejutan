from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>I LOVE YOU ASMA ❤️</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    background:#000;
    height:100vh;
    overflow:hidden;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    font-family:Arial,sans-serif;
    position:relative;
}

/* Bintang */

.star{
    position:absolute;
    background:white;
    border-radius:50%;
    animation:twinkle 2s infinite alternate;
}

@keyframes twinkle{
    from{
        opacity:.2;
    }
    to{
        opacity:1;
    }
}

/* Shooting Star */

.shooting-star{
    position:absolute;
    width:150px;
    height:2px;
    background:linear-gradient(to right, white, transparent);
    transform:rotate(-35deg);
    animation:shoot 6s linear infinite;
}

.s1{
    top:10%;
    left:-20%;
    animation-delay:0s;
}

.s2{
    top:30%;
    left:-30%;
    animation-delay:3s;
}

.s3{
    top:55%;
    left:-25%;
    animation-delay:6s;
}

@keyframes shoot{
    0%{
        transform:translateX(0) translateY(0) rotate(-35deg);
        opacity:0;
    }
    10%{
        opacity:1;
    }
    100%{
        transform:translateX(1800px) translateY(500px) rotate(-35deg);
        opacity:0;
    }
}

/* Tulisan */

h1{
    color:#ff4d6d;
    font-size:4rem;
    z-index:10;

    text-shadow:
    0 0 10px #ff4d6d,
    0 0 20px #ff4d6d,
    0 0 40px #ff4d6d,
    0 0 80px #ff4d6d;

    animation:pulse 2s infinite;
}

/* Love besar */

.heart{
    position:relative;
    width:240px;
    height:240px;

    background:#ff1744;

    transform:rotate(-45deg);

    margin-top:120px;

    animation:heartbeat 1.2s infinite;

    box-shadow:
    0 0 30px #ff1744,
    0 0 70px #ff1744,
    0 0 120px #ff1744;

    z-index:10;
}

.heart:before,
.heart:after{
    content:'';
    position:absolute;
    width:240px;
    height:240px;
    background:#ff1744;
    border-radius:50%;
}

.heart:before{
    top:-120px;
    left:0;
}

.heart:after{
    left:120px;
    top:0;
}

/* Love kecil */

.small-heart{
    position:absolute;
    color:#ff4d6d;
    font-size:20px;
    animation:fall linear infinite;
    opacity:.8;
}

@keyframes fall{
    from{
        transform:translateY(-100px);
        opacity:1;
    }

    to{
        transform:translateY(120vh);
        opacity:0;
    }
}

@keyframes heartbeat{

    0%{
        transform:rotate(-45deg) scale(1);
    }

    25%{
        transform:rotate(-45deg) scale(1.08);
    }

    50%{
        transform:rotate(-45deg) scale(1);
    }

    75%{
        transform:rotate(-45deg) scale(1.12);
    }

    100%{
        transform:rotate(-45deg) scale(1);
    }
}

@keyframes pulse{

    0%{
        transform:scale(1);
    }

    50%{
        transform:scale(1.05);
    }

    100%{
        transform:scale(1);
    }
}

</style>
</head>

<body>

<div class="shooting-star s1"></div>
<div class="shooting-star s2"></div>
<div class="shooting-star s3"></div>

<h1>I LOVE YOU ASMA ❤️</h1>

<div class="heart"></div>

<script>

/* Bintang */

for(let i=0;i<120;i++){

    let star=document.createElement('div');

    star.className='star';

    let size=Math.random()*3+1;

    star.style.width=size+'px';
    star.style.height=size+'px';

    star.style.left=Math.random()*100+'vw';
    star.style.top=Math.random()*100+'vh';

    star.style.animationDelay=Math.random()*3+'s';

    document.body.appendChild(star);
}

/* Love jatuh */

for(let i=0;i<40;i++){

    let heart=document.createElement('div');

    heart.className='small-heart';

    heart.innerHTML='❤';

    heart.style.left=Math.random()*100+'vw';

    heart.style.fontSize=
        (Math.random()*25+15)+'px';

    heart.style.animationDuration=
        (Math.random()*8+5)+'s';

    heart.style.animationDelay=
        Math.random()*8+'s';

    document.body.appendChild(heart);
}

</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
