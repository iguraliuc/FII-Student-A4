<template>
  <aside class="menu">
    <img alt="Vue logo" src="../assets/placeholder.jpg">
    <p class="menu-label">General</p>
    <ul class="menu-list">
      <li>
        <router-link to="/" exact-active-class="is-active">Dashboard</router-link>
      </li>
      <li>
        <router-link to="/about" active-class="is-active">Pagina Mea</router-link>
      </li>
    </ul>
    <p class="menu-label">Materii</p>
    <ul class="menu-list">
      <li v-for="item in materii" :key="item">
        <a>{{item}}</a>
      </li>
    </ul>
    <p class="menu-label" v-if="isAdmin">Administrare</p>
    <ul class="menu-list" v-if="isAdmin">
      <li>
        <a>Resurse</a>
        <a>Orar</a>
      </li>
    </ul>
    <p class="menu-label">Cont</p>
    <ul class="menu-list">
      <li>
        <router-link to="/XX" active-class="is-active">Setari</router-link>
      </li>
      <li>
        <a>Logout</a>
      </li>
    </ul>
  </aside>
</template>

<script>
import axios from "axios";
export default {
  name: "Menu",
  props: {
    materii: {
      type: Array,
      default: []
    },
    isAdmin: {
      type: Boolean,
      default: false
    }
  }
};
</script>

<style scoped>
</style>
