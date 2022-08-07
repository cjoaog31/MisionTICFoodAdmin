<template>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8"/>
        
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link href="style_userselect.css" rel="stylesheet">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:100, 10000, 25000" rel="stylesheet">
    </head>
    <body>
        <div class="firstline">
            <form action="mainscreen.html" class="formback">
                <button type="submit" class="back">Back</button>
            </form>

            <img src="pictures/foodblue.png" class="image"/>
        </div>


        <div class="secondline">
            <h2 class="title">SELECCIONE SU USUARIO</h2>
        </div>
        
        <div class="thirdline">
            <span>
                <h4 class="usertext">Usuario</h4>
                <form class="boxes">
                    <button class="button"></button>
                </form>
                <h4 class="usertext">Rol</h4>
            </span>

            <span>
                <h4 class="usertext">Usuario</h4>
                <form class="boxes">
                    <button class="button"></button>
                </form>
                <h4 class="usertext">Rol</h4>
            </span>

            <span>
                <h4 class="usertext">Usuario</h4>
                <form class="boxes">
                    <button class="button user1"></button>
                </form>
                <h4 class="usertext">Rol</h4>
            </span>

            <span>
                <h4 class="usertext">Usuario</h4>
                <form class="boxes">
                    <button class="button add" ></button>
                </form>
                <h4 class="usertext">Rol</h4>
            </span>
        </div>
        
        <footer>
            
        </footer>
    </body>
</html>
</template>

<script>

</script>

<style>
.firstline{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    vertical-align: middle;
    width: auto;
    height: 10vh;
    margin-bottom: 3%;
}

.formback{
    width: 8%;
    height: 40%;
    border: transparent;
    border-radius: 1vw; 
    text-align: center;
}

.back{
    width: 100%;
    height: 100%;
    border: transparent;
    border-radius: 1vw;
    color: white;
    background-image: linear-gradient(75deg, #04BFAE, #027273);
    font-weight: bolder;
    font-family: 'Montserrat', sans-serif;
    font-size: 1.5vw;
}

.back:hover{
    transform: scale(1.1);
    transition: transform .2s;
}

.image{
    width: 11.11vh;
    height: 11.11vh;
    margin-left: 30vw;
    margin-right: 38vw;
}

.secondline{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    vertical-align: middle;
    width: auto;
    height: 10vh;
    margin-bottom: 3%;
}

.title{
    font-size: 2.5vw;
    font-family: 'Montserrat', sans-serif;
    font-weight: 100000;
    color:#027273;
    width: 30%;
    text-align: center;
}

.thirdline{
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: center;
}

.boxes{
    height: 15vw;
    width: 15vw;
    border-image: linear-gradient(75deg, #04BFAE, #027273)1;
    border-radius: 2vw;
    border-width: 1vw;
}

.button{
    width: 100%;
    height: 100%;
    border-image: linear-gradient(75deg, #04BFAE, #027273)1;
    border-radius: 2vw;
    border-width: 1vw;
}

.button:hover{
    transform: scale(1.1);
    transition: transform .2s;
}

.usertext{
    text-align: center;
    margin-bottom: 6%;
    margin-top: 6%;
    font-size: 1.5vw;
    font-family: 'Montserrat', sans-serif;
    color: black;
}

.add{
    background-image: url(pictures/add.png);
    resize: both;
    background-size: 60%;
    background-repeat: no-repeat;
    background-position: 50% 50%;
    border-radius: 1vw;
}
</style>