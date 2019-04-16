<template>
  <div id="app">
    <div class="menu">
      <Menu :materii="this.materii" :isAdmin="this.isAdmin"/>
    </div>

    <div id="router-view-div">
      <router-view/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Menu from "@/components/Menu.vue";

export default {
  name: "App",
  components: {
    Menu
  },
  data() {
    return {
      name: "",
      materii: [],
      isAdmin: false,
      errors: []
    };
  },
  async created() {
    try {
      let res = await this.axios.get("http://127.0.0.1:8081/user.json");
      this.name = res.data.nume;
      this.materii = res.data.materii;
      this.isAdmin = res.data.isAdmin;
      console.log(res.data);
    } catch (error) {
      this.errors.push(error);
    }
  }
};
</script>

<style lang='css'>
@import "../node_modules/bulma/css/bulma.css";

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  display: grid;
  grid-template-columns: 200px 1fr;
  grid-template-rows: 10px 1fr 20px;
}

.menu {
  grid-column: 1/2;
  grid-row: 2/3;
  margin: 10px;
}

#router-view-div {
  margin-bottom: 30px;
  margin-right: 30px;
  margin-top: 30px;
  grid-column: 2/3;
  grid-row: 2/3;
  text-align: center;
  border: solid 1px;
}

@media (max-width: 700px) {
}
</style>
