<template>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:100, 10000, 25000">
    <title>FoodMonitor Inventory</title>
</head>
<body>
    <div class="box">
        <div class="firstline">
            <form action="views/vistasvue/mainscreen.vue" class="formback">
                <button type="submit" class="back">Back</button>
            </form>

            <img src="views/vistasvue/pictures/foodwhite.png" class="image"/>

            <form class="formuser">
                <button type="submit" class="user">Username</button>
            </form>
        </div>

        <div class="secondline">
            <form class="u_image">
                <button class="user_image">

                </button>
            </form>

            <span class="inputbox">

                <form>
                    <input type="text" placeholder="Name" class="inputinfo"/>
                </form>

                <form>
                    <input type="text" placeholder="Last Name" class="inputinfo"/>
                </form>

                <form>
                    <input type="text" placeholder="Phone Number" class="inputinfo"/>
                </form>

                <form>
                    <input type="text" placeholder="Email" class="inputinfo"/>
                </form>

                <form class="saveform">
                    <button class="save">Save Changes</button>
                </form>

            </span>

            <span class="role">
                <h3 class="roletext">Select user's role</h3>
                <form class="guestform">
                    <button class="guest">Guest</button>
                </form>

                <form class="famform">
                    <button class="fam">Family</button>
                </form>
            </span>


        </div>
    </div>


        <div class="thirdline">
            <div id="products" class="productos">
                <h3 style="margin-left: 3%;">Your Products</h3>
             <!-- agregar mas table rows automaticamente-->
            </div>
        </div>

        <div class="fourthline">
            <button class="prodbutton"></button>
            <button class="prodbutton"></button>
            <button class="prodbutton"></button>
            <button class="prodbutton"></button>
        </div>
</body>
</html>
</template>

<script>

</script>

<style>
.box{
    width: 100%;
    height: 50vh;
    background-image: linear-gradient(75deg, aqua, teal);
    border-radius: 0%;
}

.firstline{
    display: flex;
    flex-direction: row;
    justify-content:space-evenly;
    align-items:center;
    height: 10vh;
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
    color: teal;
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
    color: teal;
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
    height: 30vh;
    margin-top: 1%;;
    margin-bottom: 2%;;
}

.u_image{
    width: 15vw;
    height: 15vw;

}

.user_image{
    width: 15vw;
    height: 15vw;
    border: transparent;
    border-radius: 2vw;
}

.inputbox{
    display: flex;
    flex-direction: column;
    vertical-align: middle;
    justify-content: space-evenly;
    margin-left: 6%;
    margin-right: 6%;
    width: 35vw;
    height: 15vw;
}

.inputinfo{
    height: 2.2vw;
    width: 34.6vw;
    border: transparent;
    border-color: gray;
    border-radius: 0.4vw;
    font-family: 'Montserrat', sans-serif;
    font-size: 1vw;
    text-align: center;
}

.savebox{
    display: flex;
    flex-direction: column;
    vertical-align: middle;
    justify-content: space-evenly;
    margin-left: 3%;
    width: 15vw;
    height: 15vw;
}

.saveform{
    text-align: center;
    height: 2vw;
    width: 35vw;
}

.save{
    height: 100%;
    width: 100%;
    border-radius: 1vw;
    border: transparent;
    background-color: transparent;
    text-align: center;
    font-family: 'Montserrat';
    font-weight: bolder;
    font-size: 1.1vw;
    color: white;
}

.role{
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    width: 20vw;
    height: 15vw;
}

.guestform{
    width: 20vw;
    height: 5vw;
}

.guest{
    width: 100%;
    height: 100%;
    border-radius: 1vw;
    border: transparent;
    font-family: 'Montserrat', sans-serif;
    font-weight: bolder;
    font-size: 1.5vw;
    color: teal;
}

.famform{
    width: 20vw;
    height: 5vw;
}

.fam{
    width: 100%;
    height: 100%;
    border-radius: 1vw;
    border: transparent;
    font-family: 'Montserrat', sans-serif;
    font-weight: bolder;
    font-size: 1.5vw;
    color: teal;
}

.roletext{
    font-size: 1vw;
    font-family: 'Montserrat';
    font-weight: bolder;
    color: white;
    margin: 0px ;
}

.thirdline{
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items:baseline;
    vertical-align: bottom; 
    height: 7vh;
}

.productos{
    width: 100%;
    font-family: 'Montserrat', sans-serif;
    color: white;
    font-weight: bolder;
}

#products{
    text-align: left;
    background-color: teal;
    border-radius: 0% 0% 1.5vw 1.5vw;
}

.fourthline{
    display: flex;
    flex-direction: row;
    margin-top: 6%;
    justify-content: space-evenly;
    height: 20vh;
    width: 100%;
}

.prodbutton{
    width: 15vw;
    height: 15vw;
    border-width: 1vw;
    border-image: linear-gradient(75deg, aqua, teal)1;
}
</style>
