<template>
  <div id="app">
    <NavBar id="navbar"/>
    <Home />
  </div>
</template>


<script>
import Home from '@/views/Home.vue'
import NavBar from '@/components/NavBar.vue'
export default {
   components: {
    NavBar,
    Home
  }
}
</script>


<style>
html{
    margin: 0px;
    padding: 0px;
    border: 0px;
}
#app {
  margin: 0px;
  padding: 0px;
  border: 0px;

  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#navbar {
  margin-left: auto;
  margin-right: auto;
  width: 97vw;
  z-index: 3;
}

</style>
