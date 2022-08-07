<template>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:100, 10000, 25000">
    <title>Shopping List</title>
</head>
<body>
    <div class="box">
        <div class="firstline">
            <form action="views/vistasvue/mainscreen.html" class="formback">
                <button type="submit" class="back">Back</button>
            </form>

            <img src="views/vistasvue/pictures/foodwhite.png" class="image"/>

            <form class="formuser">
                <button type="submit" class="user">Username</button>
            </form>
        </div>

        <div class="secondline">
            <h2 class="text">Shopping List</h2>
        </div>

        <div class="thirdline">
            <form action="" class="forminput">
                <label for="search" class="label">Search</label>
                <input type="text" id="search" class="input" placeholder="Search for products">
            </form>
            <form action="" class="formadd">
                <button class="add">Add Product</button>
            </form>
        </div>
    </div>

    <table id="products" class="productos">
        <tr> 
            <th>Id</th>
            <th>Nombre</th>
            <th>Cantidad</th>
            <th>Compra</th>
            <th>Expiración</th>
        </tr>

        <!-- agregar mas table rows automaticamente-->
    </table>
</body>
</html>
</template>

<script>

</script>

<style>
.box{
    width: 100%;
    height: 25vh;
    background-image: linear-gradient(75deg, #7654E8, #2B06AC);
    border-radius: 0%;
}

.firstline{
    display: flex;
    flex-direction: row;
    justify-content:space-evenly;
    align-items:center;
    height: 8vh;
}

.formback{
    width: 10%;
    height: 40%;
    border: transparent;
    border-radius: 1vw; 
}

.back{
    width: 100%;
    height: 100%;
    border: transparent;
    border-radius: 1vw;
    color: #2B06AC;
    font-weight: bolder;
    font-family: 'Montserrat', sans-serif;
    font-size: 1.5vw;
}

.back:hover{
    transform: scale(1.1);
    transition: transform .2s;
}

.image{
    width: 7vw;
    height: 7vw;
    margin-left: 35%;
    margin-right: 35%;
}

.formuser{
    width: 10%;
    height: 40%;
    border: transparent;
    border-radius: 1vw; 
}

.user{
    width: 100%;
    height: 100%;
    border: transparent;
    border-radius: 1vw;
    color: #2B06AC;
    font-weight: bolder;
    font-family: 'Montserrat', sans-serif;
    font-size: 1.5vw;
}

.user:hover{
    transform: scale(1.1);
    transition: transform .2s;
}

.secondline{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: 8vh;
    margin-top: 1%;;
    margin-bottom: 2%;;
}

.text{
    font-size: 4vw;
    font-family: 'Montserrat', sans-serif;
    font-weight: bolder;
    color: white;
}

.thirdline{
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items:baseline;
    vertical-align: bottom; 
    height: 4vh;
}

.forminput{
    width: 25%;
    height: 100%;
    margin-left: 2%;
}

.input{
    width: 75%;
    height: 50%;
    border-radius: 1vw;
    border: transparent;
    text-align: center;
}

.label{
    font-family: 'Montserrat', sans-serif;
    font-size: 1.2vw;
    font-weight: bolder;
    color: white;
}

.formadd{
    width: 10%;
    height: 60%;
    border-radius: 1vw;
    border: transparent;
    background-color: transparent;
}

.add{
    width: 100%;
    height: 100%;
    border-radius: 1vw;
    border: transparent;
    background-color: transparent;
    font-size: 1.2vw;
    font-family: 'Montserrat', sans-serif;
    font-weight: bolder;
    color: white;
}

.productos{
    width: 100%;
    font-family: 'Montserrat', sans-serif;
    color: white;
    font-weight: bolder;
}

#products{
    padding-top: 1vw;
    padding-bottom: 1vw;
    text-align: center;
    background-color: #2B06AC;
    border-radius: 0% 0% 1.5vw 1.5vw;
}
</style>