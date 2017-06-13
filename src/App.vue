<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
html {
  background-image:url(./assets/background.jpg);
  min-height:100%;
  background-attachment: fixed;
  background-size:cover;
  background-position: center;
  background-repeat: no-repeat;
  /* background-color: #2c2c2c; */
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #eeeeee;
  margin-top: 60px;
}
</style>
