<template>
  <div id="app">
    <NavBar id="navBarMain"/>
    <!-- <ColorPicker/> -->
    <router-view/>
  </div>
</template>

<script>
import NavBar from "@/components/navbar/NavBar.vue";
// import ColorPicker from "@/components/color-picker/ColorPicker.vue";

export var globalDark = "red";

export default {
  name: "mainApp",
  components: {
    // ColorPicker,
    NavBar
  }
};
</script>


<style>
:root {
  --light-color: white;
  --light-medium-color: lightblue;
  --medium-color: blue;
  --medium-dark-color: darkblue;
  --dark-color: black;
}

body {
  margin: 0px;
  padding: 0px;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0px;
  padding: 0px;
}
#nav {
  padding: 30px;
}

#navBarMain {
  position: sticky;
  top: 0px;
}
</style>
