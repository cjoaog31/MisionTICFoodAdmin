<template>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="stylespassword.css" rel="stylesheet">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:100, 10000, 25000" rel="stylesheet">
        <div style="text-align: center;">
            <img src="pictures/foodblue.png" class="image"/>
        </div>
        <title>FoodMonitor Log In</title>
    </head>
    <body>
        <div style="display: flex; flex-direction: row; align-items: center; justify-content: center;">

            <div class="userbox" style="font-size: 1vw;">


                <img src="pictures/loglogo.png" style="width: 45%; height: 45%;"/>
                <h2 class="font" style="max-width: 60%;">CURRENT USER</h2>

                <form action="" style="width: 80%; height: 15%;">
                    <input type="password" maxlength="4" required class="input" style="text-align: center; width: 100%; height: 100%; background-color: lightseagreen;">
                </form>




            </div>

        </div>

        
    </body>
</html>
</template>

<script>

</script>

<style>
.userbox{
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
height: 50vh;
width: 50vh;
border-radius: 10%;
border: transparent;
background-image: linear-gradient(#05BEAD, #027675);
vertical-align: middle;
}

.input{
font-size: 5vh; 
color: white;
border-radius: 2vw;
border: transparent;
}

.font{
font-family: 'Montserrat', sans-serif;
margin-top: 1%;
margin-bottom: 1%;
font-weight: 25000;
color: white;
}


.containerup{
    display:flex;
    align-items: center;
    justify-content: space-evenly;
}

.image{
    margin-bottom: 0%;
    width: 11.11vh;
    height: 11.11vh;
    margin-right: 40vw;
    margin-left: 40vw;
}
</style>