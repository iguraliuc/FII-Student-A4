<template>
    <div>
        <div v-for="boardNews in targetNewsArray" :key="boardNews.title">
        <div class="anunt-container">
            <div class="date">
                <p>{{boardNews.date}}</p> 
                <p class = "day">{{boardNews.day}}</p>
            </div>
            <div class="anunt">
                <p class="top">{{boardNews.title}}</p>
                <p class="continut">{{boardNews.content}}</p>
            </div>
        </div>
        </div>
    </div>
</template>


<script>



var targetNewsArray = this.getTargetBoardNews();

export default {
    props: {
        targetBoardTitle: String,
        boardsNewsArray: Array
    },
    methods: {
        getTargetBoardNews(){
            return this.boardsNewsArray.filter(news => news.boardTitle === this.targetBoardTitle);
        }
    },
    data() {
        return{
            targetNewsArray
        }
    }
}

</script>


<style scoped>



</style>
