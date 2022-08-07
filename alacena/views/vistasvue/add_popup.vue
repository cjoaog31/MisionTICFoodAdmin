<template>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:100, 10000, 25000">
</head>
<body>

    <div class="shadow">

    </div>
    <div class="container">
        <div class="box">
            <div class="firstline">
                <h3 class="fonttext" style="margin-right: 33%; margin-left: 37%;">Add Product</h3>
                <form action="views/vistasvue/pantry.vue">
                    <button class="close_x fonttext">x</button>
                </form>
            </div>
            <div class="secondline">
                <form action="" class="formname">
                    <label for="Name" class="fonttext2">Name of Product:</label>
                    <input type="text"  id="Name" class="nameinput" required placeholder="Insert Name">
                </form>

                <form action="" class="formqua">
                    <label for="Name" class="fonttext2">Quantity:</label>
                    <input type="text"  id="Name" class="quainput" required placeholder="#">
                </form>
            </div>

            <div class="thirdline">
                <form action="" class="formbought">
                    <label for="Name" class="fonttext2">Bought:</label>
                    <input type="date"  id="Name" class="bought" placeholder="DD/MM/AA">
                </form>

                <form action="" class="formexp">
                    <label for="Name" class="fonttext2">Expires:</label>
                    <input type="date"  id="Name" class="exp" placeholder="DD/MM/AA">
                </form>
            </div>

            <div class="fourthline">
                <form action="views/vistasvue/pantry.vue" class="saveform">
                    <button class="save">Save</button>
                </form>
            </div>
        </div>
    </div>

</body>
</html>
</template>

<script>

</script>

<style>


.shadow{
    width: 100%;
    height: 100%;
    margin-top: 0%;
    position: absolute;
    background-color: white;
    filter: brightness(.5);
}

.container{
    display: flex;
    position: relative;
    flex-direction: row;
    justify-content: center;
    vertical-align: middle;
}

.box{
    width: 60vw;
    height: 40vh;
    background-image: linear-gradient(75deg, #7654E8, #2B06AC);
    border-radius: 2vw;
    margin-top: 35vh;
    margin-bottom: 35vh;
    margin-left: 2vw;
    margin-right: 2vw;
}

.firstline{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
}

.close_x{
    background-color: transparent;
    border: transparent;
}

.fonttext{
    font-family: 'Montserrat', sans-serif;
    color: white;
    font-size: 1.8vw;
    font-weight: bolder;
}

.fonttext2{
    font-family: 'Montserrat', sans-serif;
    color: white;
    font-size: 1.2vw;
    font-weight: bolder;
}

.secondline{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin-top: 1%;
}

.nameinput{
    width: 60%;
    margin-left: 3%;
    text-align: center;
    border: transparent;
    border-radius: 2vw;
    height: 60%;
}

.formname{
    width: 55%;
    height: 5vh;
    margin-left: 3%;
}

.quainput{
    width: 30%;
    margin-left: 3%;
    text-align: center;
    border: transparent;
    border-radius: 2vw;
    height: 60%;
}

.formqua{
    width: 25%;
    height: 5vh;
    margin-left: 3%;
}

.thirdline{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin-top: 2%;
}

.bought{
    width: 60%;
    text-align: center;
    border: transparent;
    border-radius: 2vw;
    height: 60%;
    margin-left: 3%;
}

.formbought{
    width: 40%;
    height: 5vh;
    margin-left: 3%;
}

.exp{
    width: 60%;
    text-align: center;
    border: transparent;
    border-radius: 2vw;
    height: 60%;
    margin-left: 3%;
}

.formexp{
    width: 40%;
    height: 5vh;
}

.fourthline{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin-top: 2%;
}

.saveform{
    width: 20%;
    height: 4vh;
}

.save{
    width: 100%;
    height: 100%;
    border-radius: 1vw;
    border: transparent;
    text-align: center;
    font-size: 1.5vw;
    font-family: 'Montserrat', sans-serif;
    color: #2B06AC;
    font-weight: bolder;
}

.save:hover{
    transform: scale(1.1);
    transition: transform .2s;
}
</style>