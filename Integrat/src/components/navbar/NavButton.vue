<template>
  <!-- :style="{'background-color':bgcolor, 'color':textColor}" -->
  <div class="nav-button">
    <span>{{text}}</span>
  </div>
</template>


<script>
export default {
  name: "NavButton",
  props: {
    text: String
    //     bgcolor: String,
    //     textColor: String
  },
  data() {
    return {
      text
      //       bgcolor,
      //       textColor
    };
  }
};
</script>

<style scoped>
.nav-button {
  background-color: pink;
  color: black;
}

.nav-button > span {
  align-content: center;
  align-items: center;
  align-self: center;
}

.nav-button:hover {
  background-color: red;
  color: white;
}
</style>
