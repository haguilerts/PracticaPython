class Usuario {
    //Propiedades de la clase
    nombre = "default";
    apellido = "default";
    edad = 99;
    gustosMusicales = [];

    //Constructor
    constructor(nombre="default",apellido="default",edad=99,gustosMusicales=[]) {
      this.nombre = nombre;
      this.apellido = apellido;
      this.edad = edad;
      this.gustosMusicales = gustosMusicales;
    }

    presentacion(){
      return `Hola! soy ${this.nombre} ${this.apellido}`;
    } 
  }
//----------------------------------------------------------- 

  const user1 = new Usuario("Juan","Rodriguez",30,["Rock","Electrónica","Jazz"]);
  user1.nombre = "José";
  for (let prop in user1) {
    console.log(`Propiedad: ${prop} = ${user1[prop]}`);
  }

  const arr = [10,20,30]; 
  for(let elem of arr){
  }


  const usuario = {};

  usuario.nombre = "Juan";
  usuario.apellido = "Rodriguez";
  usuario.edad = 30;
  usuario.gustosMusicales = ["Rock","Electrónica","Jazz"];
  usuario.presentacion = function (){
    return `Hola! soy ${this.nombre} ${this.apellido}`;
  };

  console.log(usuario.presentacion());

  const otroUsuario = {
    nombre: "Juan",
    apellido: "Rodriguez",
    edad: 30,
    gustosMusicales: ["Rock","Electrónica","Jazz"],
    presentacion: function(){
      return `Hola! soy ${this.nombre} ${this.apellido}`;
    }
  };

  console.log(otroUsuario.presentacion());