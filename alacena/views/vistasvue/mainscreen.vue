<template>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8"/>
        
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:100, 10000, 25000">
        <div style="display: flex; justify-content: center; flex-direction: row; text-align: center; vertical-align: middle;">
            <img src="views/vistasvue/pictures/foodblue.png" class="image" />
            <span>
                <button style=" width: 3vw; height: 3vw; border-radius: 50px; "></button>
            </span>
        </div>
    </head>
    <body>
        <div style="margin: auto;" class="containerup">
            
            <div class="date">
                <p class="text" style="font-size: 2.5vw; margin-top: 4%; margin-bottom: -15%;">JUNE</p>
                <p class="text" style="font-size: 2.5vw; margin-bottom: -15%;">23rd</p>
                <p class="text" style="font-size: 2.5vw;">00:00:00</p>
            </div>

            <div class="next">
                <p class="text" style="font-size: 1.5vw; margin-top: 4%; margin-bottom: 0%;">To prepare next:</p>
                <p class="text" style="font-size: 1.5vw; margin-bottom: -4%;">Cabbage - Bought on June 10th.</p>
                <p class="text" style="font-size: 1.5vw; margin-bottom: -4%;">Carrot - Bought on June 12th.</p>
                <p class="text" style="font-size: 1.5vw; margin-bottom: -4%;">Greek Yogurt - Expires on June 25th.</p>
            </div>

            <div class="recipe">

            </div>

            

        </div>
        <div style="margin: auto;" class="containerdown">

            <form action="views/vistasvue/pantry.vue" class="inventory">
            <button class="inventory-text">
            INVENTARIO
            </button>
            </form>

            <span class="verticalwish">

                <form action="views/vistasvue/wishlist.vue" class="wish">
                    <button class="wish-text">
                    WISHLIST
                    </button>
                </form>

                <form action="views/vistasvue/shopping.vue" class="shop">
                    <button class="shop-text">
                    SHOPPING
                    </button>
                </form>

            </span>

            <form action="views/vistasvue/userselect.vue" class="users">
                <button class="users-text">
                USERS
                </button>
            </form>            

        </div>
        
        <footer>
            
        </footer>
    </body>
</html>
</template>

<script>

</script>

<style>
/*UPPER PART*/

.image{
    margin-bottom: 0px;
    width: 11.11vh;
    height: 11.11vh;
    margin-right: 40vw;
    margin-left: 40vw;
}

.containerup{
    display: flex;
    align-items:center;
    justify-content: space-evenly;
    padding: 10px;
    max-width: 85%;
}

.date {
height: 22.91vh; width: 17.91vw; background-image: linear-gradient(75deg, aqua, teal);
margin-right: 20px;
border-radius: 35px;
border-color: transparent;
text-align:left;
vertical-align: middle;
}

.text{
    margin-left: 11%;
    font-size: auto; min-width: 10vw;
    font-family: 'Montserrat', sans-serif;
    color: white;
    font-weight: bolder;
}

.next {
height: 22.91vh; width: 43.05vw; background-image: linear-gradient(75deg, aqua, teal);
max-height: fit-content;
border-radius: 35px;
border-color: transparent;
text-align: center;
vertical-align: middle;
}

.recipe {
height: 22.91vh; width: 33.125vw; background-image: linear-gradient(75deg, aqua, teal);
margin-left: 20px;
border-radius: 35px;
border-color: transparent;
text-align: center;
vertical-align: middle;
}

/* BOTTOM PART*/

.verticalwish{
    display: flex; flex-direction: column;
    align-items: center;
    min-width: 29.16%;
}

.containerdown{
    display:flex;
    align-items: center;
    justify-content: space-evenly;
    padding: 10px;
}

.inventory:hover{
    transform: scale(1.05);
    transition: transform .2s ;
}

.wish:hover{
    transform: scale(1.05);
    transition: transform .2s ;
}

.shop:hover{
    transform: scale(1.05);
    transition: transform .2s ;
}

.users:hover{
    transform: scale(1.05);
    transition: transform .2s ;
}

.inventory {
    width: 29.16%; height: 38vh;
    background-image: url(views/vistasvue/pictures/fruitdark.jpg);
    background-size: cover; background-position: 61%;
    margin-top: 35px ;
    margin-bottom: 35px ;
    margin-right: 20px ;
    margin-left: 0px ;
    border-radius: 0.8vw;
    border-width: 0.8vw;
    border-style: solid;
    border-image: linear-gradient(75deg, aqua, teal)1;
    box-shadow: 20px 10px 20px teal;
}

.inventory-text{
    font-size: 2vw; 
    color: white; 
    font-family: 'Montserrat', sans-serif; 
    font-weight: bolder ;
    width: 100%; 
    height: 38vh; 
    background-color: transparent; 
    border: transparent;
}

.users {
    width: 29.16%; height: 38vh;
    background-image: url(views/vistasvue/pictures/userdark.jpg);
    background-size: cover; background-position: 50%;
    margin-top: 35px ;
    margin-bottom: 35px ;
    margin-right: 0px ;
    margin-left: 20px ;
    border-radius: 0.8vw;
    border-width: 0.8vw;
    border-style: solid;
    border-image: linear-gradient(75deg, aqua, teal)1;
    box-shadow: 20px 10px 20px teal;
}

.users-text{
    font-size: 2vw; 
    color: white; 
    font-family: 'Montserrat', sans-serif; 
    font-weight: bolder ;
    width: 100%; 
    height: 38vh; 
    background-color: transparent; 
    border: transparent;
    border-width: 30px;
}

.wish {
    width: 100%; height: 15vh;
    background-image: url(views/vistasvue/pictures/wishlistdark.jpg);
    background-size: cover; background-position: 2% 2%;
    margin-top: 0px ;
    margin-bottom: 17px ;
    margin-right: 0px ;
    margin-left: 0px ;
    border-radius: 0.8vw;
    border-width: 0.8vw;
    border-style: solid;
    border-image: linear-gradient(75deg, aqua, teal)1;
    box-shadow: 20px 10px 20px teal;
}

.wish-text{
    font-size: 2vw; 
    color: white; 
    font-family: 'Montserrat', sans-serif; 
    font-weight: bolder ;
    width: 100%; 
    height: 15vh; 
    background-color: transparent; 
    border: transparent;
}

.shop {
    width: 100%; height: 15vh;
    background-image: url(views/vistasvue/pictures/wishlistdark.jpg);
    background-size: cover; background-position: 2% 2%;
    margin-top: 17px ;
    margin-bottom: 0px ;
    margin-right: 0px ;
    margin-left: 0px ;
    border-radius: 0.8vw;
    border-width: 0.8vw;
    border-style: solid;
    border-image: linear-gradient(75deg, aqua, teal)1;
    box-shadow: 20px 10px 20px teal;
}

.shop-text{
    font-size: 2vw; 
    color: white; 
    font-family: 'Montserrat', sans-serif; 
    font-weight: bolder ;
    width: 100%; 
    height: 15vh; 
    background-color: transparent; 
    border: transparent;
}
</style>