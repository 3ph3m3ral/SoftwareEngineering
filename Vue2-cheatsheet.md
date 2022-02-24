# VueJs Tutorial
### Index
- Shell Commands
- Vue Compontents

<slot>
_________________________________________________

## INSTALL

- npm install -g @vue/cli
- vue create todo-app

## VISUALIZE
- vue ui

###  Modi per utilizzare VueJS
    a. Utilizzo di CDN includendo il tag <script> nel file HTML;
    b. Installazione tramite package manager (npm o yarn);
    c. Utilizzo di @vue/cli per inizializzare il progetto.
    
## Example project structure
todo-app
├── node_modules
├── public
│   ├── favicon.ico
│   └── index.html
├── src
│   ├── App.vue
│   ├── assets
│   │   └── logo.png
│   ├── components
│   │   └── HelloWorld.vue
│   └── main.js
├── README.md
├── babel.config.js
├── package.json
└── yarn.lock

## Shell
Vue command line interface for project maneagement and creation
``` bash
 vue cli 
```
Vue run node client server without building and automate the dependency fixing.
``` bash
node run serve --fix
```

``` bash
vue ui
```
### Data Interpolation
``` html
<p> {{ my_variabile }} </p>
<p> {{ my_function( ) }} </p>
```

### Vue components: General

Basic syntax
    v-{nomedirettiva}:{nomeargomento}
#### Vue components: v-on

v-on : aggancia un listener di eventi all’elemento. Il tipo di evento è indicato dall’argomento. 
L’espressione può essere un nome di metodo, un’istruzione inline. 
Per esempio se vogliamo agganciare un evento click 
ad un pulsante la sintassi è 

<button v-on:click='submitForm'>...</button> .

na forma abbreviata è la seguente 

<button @click="submitForm">...</button> 
 
 
``` html
    <div v-if="showMovies">
      <li v-for="movie in movies">{{ movie }}</li>
```
#### Vue components: v-show
``` html
    <div v-if="showMovies">
      <li v-for="movie in movies">{{ movie }}</li>
```
#### Vue components: v-for
v-for : che effettua il rendering dell’elemento più volte in base ai dati di origine.
 Utilizza una sintassi del tipo alias in expression per fornire un alias per l’elemento 
 corrente su cui si sta iterando;

``` html
    <div v-if="showMovies">
      <li v-for="movie in movies">{{ movie }}</li>
```
#### Vue components: v-if
v-if : questa direttiva permette di effettuare il rendering di un componente 
o di un elemento del DOM basandosi su una condizione specifica
 (solitamente riguardante uno specifico valore dei nostri dati);

``` html
    <div v-if="showMovies">
      <li v-for="movie in movies">{{ movie }}</li>
```
#### Vue components: v-bind
v-bind : Associa dinamicamente uno o più attributi, o una proprietà, del componente ad un’espressione;

