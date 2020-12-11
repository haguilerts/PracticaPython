const arr = ["a", "bb", "c", "d"];

/*********************************************/
// Con funciones por expresión
const f = function () {
  console.log("forEach: Un elemento.");
};
arr.forEach(f);

/*********************************************/
const funcEvery = function (e) {
    // Si el tamaño del string es igual a 1
    if (e.length == 1) return true;
    else return false;
};

console.log("Every: "+arr.every(funcEvery)); // Le pasamos la función callback todos() a every
/*********************************************/
const funcSome = function (e) {
    if (e.length == 2) return true;
    else return false;
};

console.log("Some: "+arr.some(funcSome)); 
/*********************************************/

const arr2 = ["Ana", "Pablo", "Pedro", "Pancracio", "Heriberto"];

/*********************************************/
const funcMap = function (e) {
    return e.length;    
};
console.log("Map: "+arr2.map(funcMap)); 
/*********************************************/
const funcFilter = function (e) {
    if (e[0] == "P") return true; 
    else return false; 
};
console.log("Filter: "+arr2.filter(funcFilter)); 
/*********************************************/
const funcFind = function (e) {
    if (e.length == 5) return true; 
    else return false; 
};
console.log("Find: "+arr2.find(funcFind)); 
console.log("FindIndex: "+arr2.findIndex(funcFind));
/*********************************************/
const arr3 = [95, 5, 25, 10, 25];
console.log("Reduce: "); 
const funcReduce = function (p,e) {
    console.log("P= "+p+" - E= "+e);
    return p-e; 
};
console.log("Reduce: "+arr3.reduce(funcReduce));
console.log("ReduceRight: "); 
console.log("ReduceRight: "+arr3.reduceRight(funcReduce));  

