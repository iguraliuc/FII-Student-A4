<template>
  <nav class="navbar">
    <div class="logo">
      <img src="../../assets/logo-alb.png" alt="FiiStudent logo">
    </div>

    <form class="search" action="/action_page.php">
      <input type="text" placeholder="Search.." name="search">
    </form>

    <ul class="navlinks">
      <li class="navitem dropdown">
        <router-link to="/login" class="a-class active dropli home-button">Log in / Register</router-link>
      </li>

      <li class="navitem dropdown">
        <router-link to="/home" class="a-class active dropli home-button">Home</router-link>
      </li>

      <li class="navitem dropdown">
        <router-link to="/orar" class="a-class active dropli home-button">Orar</router-link>
        <div class="dropdown-content">
          <router-link to="/orar" class="a-class active dropli home-button">Orarul Meu</router-link>
          <router-link to="/orar" class="a-class active dropli home-button">Grupe</router-link>
          <router-link to="/orar" class="a-class active dropli home-button">Sali</router-link>
          <router-link to="/orar" class="a-class active dropli home-button">Cadre Didactice</router-link>
        </div>
      </li>

      <li class="navitem dropdown">
        <router-link to="/boarduri" class="a-class active dropli home-button">Boarduri</router-link>
      </li>

      <li class="navitem dropdown">
        <router-link to="/contul-meu" class="a-class active dropli home-button">Contul Meu</router-link>
      </li>

      <li class="navitem dropdown">
        <router-link to class="a-class active dropli home-button">Mai multe...</router-link>
        <div class="dropdown-content">
          <router-link to="/" class="a-class active dropli home-button">Cadre Didactice</router-link>
          <router-link to="/" class="a-class active dropli home-button">Sali</router-link>
          <router-link to="/" class="a-class active dropli home-button">Stagii de practica</router-link>
        </div>
      </li>
    </ul>
  </nav>
</template>



<script>
export default {};
</script>


<style scoped>
*,
*::before,
*::after {
  box-sizing: inherit;
  margin: 0px;
  padding: 0px;
  align-items: center;
}

html {
  margin: 0px;
  padding: 0px;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  margin: 0px;
  padding: 0px;
}

.navbar {
  width: 100%;
  margin: 0px;
  padding: 0px;
  background-color: var(--dark-color);
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  position: sticky;
}

.logo {
  display: flex;
  flex: 0.3;
  justify-content: center;
}

.logo img {
  vertical-align: middle;
  height: 3vw;
}

.search input[type="text"] {
  text-align: left;
  width: 100%;
  margin: 0;
  padding: 0.6vw;
}

.navlinks {
  list-style: none;
  display: flex;
  flex: 2;
  justify-content: flex-end;
  align-items: center;
  overflow: hidden;
}

.navitem .a-class {
  display: inline-block;
  padding: 1vw 1vw;
  width: 8vw;
  text-decoration: none;
  outline: 0;
  -moz-outline-style: none;
  text-align: center;
  color: white;
}

.navitem:hover {
  background-color: white;
}

.navitem:hover > .a-class {
  color: black;
}

.dropdown {
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;

  background-color: black; /*#b8a9c9*/
  color: white;
  min-width: 8vw;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
}

.dropdown-content > .a-class {
  text-decoration: none;
  color: white;
  outline: 0;
  -moz-outline-style: none;
  display: block;
  text-align: center;
}

.dropdown-content > .a-class:hover {
  background-color: white;
  color: black;
}

.dropdown:hover .dropdown-content {
  display: block;
}
</style>
