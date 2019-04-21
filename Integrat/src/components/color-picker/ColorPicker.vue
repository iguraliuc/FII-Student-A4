<template>
  <div>
    <!-- <chrome-picker v-model="colors"></chrome-picker> -->
    <chrome-picker :value="colors" @input="updateValue"></chrome-picker>
  </div>
</template>

<script>
import { Chrome } from "vue-color";

var propsDefault = { h: 10, s: 0.66, v: 0.3 };

export default {
  components: {
    "chrome-picker": Chrome
  },
  methods: {
    updateValue(value) {
      this.colors = value;
      if (value) {
        document.documentElement.style.setProperty("--dark-color", value.hex);
      }
    }
  },
  data() {
    return {
      colors: propsDefault
    };
  },
  mounted() {}
};
</script>

<style>
</style>