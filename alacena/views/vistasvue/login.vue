<template>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>FoodMonitor</title>
    <link rel="stylesheet" href="loggin/assets/css/style.css">
</head>
<body>

    <div class="divlogin">
        <div class="container">
          <div class="divcont1">
          <img src="loggin/assets/img/foodblue.png" alt="Logo1" height="300px" width="300px" class="imagen1">
            <div class="divcont">
                <h3>INICIAR SESIÓN</h3>
                <form @submit.prevent="sendForm()">
                    <input type="email" class="{'error':validaEmail}" placeholder="Correo Electronico" v-model="form.email">
                    <input type="password" v-if="form.type!=2" :class="{'error':validaPassword}" placeholder="Introduce contraseña" v-model="form.password" >
                    <input type="password" v-if="form.type==1" :class="{'error':validaRepetirPassword}" placeholder="Repetir contraseña" v-model="form.passwordos" >
                    <div>
                        <form action="mainscreen.html" style="position: absolute;">
                            <button style="height: 0vh; width: 0vw; border: transparent; background-color: transparent; margin-top: -8%;"></button>
                        </form>
                    </div>

                    <div>
                        <form action="userselect.html">
                            <button class="pinch">Iniciar Sesión</button>
                        </form>
                    </div>
                    <a href="javascript:void(0)" @click="form.type=2" v-if="form.type!=2" >Recuper contraseña</a>
                    <a href="javascript:void(0)" @click="form.type=1" v-if="form.type!=1" >Registrarme</a>
                    <a href="javascript:void(0)" @click="form.type=0" v-if="form.type!=0" >Iniciar sesión</a>
                </form>
            </div>
          </div>
        </div>
    </div>
</body>
</html>

</template>

<script>
new Vue({
    el:".divlogin",
    data:{
        form:{
            type:0, // 0 = Login , 1 = Registro 2- Recuperar contraseña
            email:"",
            password:"",
            passwordos:""}
    },
    methods:{
        sendForm(){
            if(this.validaType()){
                console.log(this.form);
            }
        },
        validaType(){
            if(this.form.type==0 && !this.validaEmail && !this.validaPassword){
                return true;
            }
            else if(this.form.type==1 && !this.validaEmail && !this.validaRepetirPassword){
                return true;
            }
            else if(this.form.type==2 && !this.validaEmail){
                return true;
            }
            return false;
        },
        signup(){
        }
    },
    computed:{
        validaEmail(){
            var exp = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
            if(exp.test(this.form.email)){
                return false;
            } else{
                return true;
            }
        },
        validaPassword(){
            var exp = /^(?=.*\d)(?=.*[a-záéíóúüñ]).*[A-ZÁÉÍÓÚÜÑ]/;
            if(exp.test(this.form.password)){
                return false;
            } else{
                return true;
            }
        },
        validaRepetirPassword(){
            if(this.form.password==this.form.passwordos){
                return false;
            } else{
                return true;
            }
        },
        title(){
            return (this.form.type==0)?'Login':(this.form.type==1)?'Registro':'Recuperar contraseña';
        }
    }
});
new Vue({

});

</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Montserrat:100, 10000, 25000');

html,body{ padding: 0px; margin: 0px; width: 100%; height: 100vh; font-family: "Montserrat"; color: black;  }
.divlogin{
    background-color: white;
    background-size: cover;
    background-position: center center;
    width: 100%;
    height: 100vh;
    display: flex;
    align-content: center;
    align-items: center;
    padding-top: 0px;
}
.divlogin .container{
    width: 100%;
    text-align: center;
}
.divlogin .container .divcont1{
    width: 100%;
    max-width: 300px;
    margin-left: 10px;
    display: inline-block;
    align-items: center;
}
.divlogin .container .divcont{
    width: 100%;
    max-width: 300px;
    background: white;
    padding: 20px;
    border-radius: 40px;
    display: inline-block;
    border-width: 3px;
    border-style: solid;
    border-color: teal;

}
.divlogin .container .divcont h3{
    margin-top: 0px;
}
.divlogin .container .divcont input{
    height: 5vh;
    margin: 0px;
    border: 0px;
    outline: none;
    padding: 10px;
    border-radius: 5px;
    width: 90%;
    margin-bottom: 10px;
    border-width: 3px;
    border-style: solid;
    border-color: teal;
}
.divlogin .container .divcont input.error{ border-bottom: 3px solid teal; }
.divlogin .container .divcont button{
    margin: 0px;
    border:0px;
    display: block;
    margin: auto;
    padding: 10px 30px;
    background-image: transparent;
    color: white;
    border-radius: 5px;
    margin-bottom: 10px;
}
.divlogin .container .divcont a{
    font-size: 12px;
    margin-right: 10px;
    color: teal;
    display: inline-block;
}

.pinch{
    height: 4vh;
    width: 15vw;
    background-image: linear-gradient(75deg, aqua, teal);
}

.pinch:hover{
    background-image: linear-gradient(75deg, #04D057, #009A3E);
    transform: scale(1.1);
    transition: transform .2s;

}
</style>