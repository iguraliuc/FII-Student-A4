<template>
  <div>
    <NewsComponent/>
  </div>
</template>

<script>
// @ is an alias to /src
import NewsComponent from "@/components/news/NewsComponent.vue";

export default {
  name: "home",
  components: {
    NewsComponent
  }
};
</script>
