<template>
  <div id="homePage">
    
    <Container id="home" orientation="horizontal" 
    @drop="onContainerDrop($event)"
    drag-handle-selector=".drag-handle"
    :drop-placeholder="upperDropPlaceholderOptions"
    >
      <Draggable class="home-draggable boards-news">
         <div :class="pageContainers.containers[0].props.className" :style="boardsContainerStyle">
            <div class="drag-handle">
              <span>&#x2630;</span>
              {{ pageContainers.containers[0].name }}
            </div>
            <Container group-name="col" 
            @drop="(event) => onComponentDrop(pageContainers.containers[0].id, event)" 
            :get-child-payload="getComponentPayload(pageContainers.containers[0].id)"
            drag-handle-selector=".drag-handle-comp"
            :drop-placeholder="dropPlaceholderOptions"
            >
              <Draggable v-for="component in pageContainers.containers[0].components" :key="component.id">
                <div :class="component.props.className" class="drag-handle-comp" :style="component.props.style">
                  <p>{{ component.content }}</p>
                  <!-- <BoardNews targetBoardTitle="Ingineria Programarii" boardsNewsArray="boardsNews"/> -->
                </div>
              </Draggable>
          </Container>
          </div>
      </Draggable>

      <Draggable class="home-draggable" id="generalNews">
         <div :class="pageContainers.containers[1].props.className" :style="generalNewsContainerStyle">
            <div class="drag-handle">
              <span>&#x2630;</span>
              {{ pageContainers.containers[1].name }}
            </div>
            <Container group-name="col" 
            @drop="(event) => onComponentDrop(pageContainers.containers[1].id, event)" 
            :get-child-payload="getComponentPayload(pageContainers.containers[1].id)"
            drag-handle-selector=".drag-handle-comp"
            :drop-placeholder="dropPlaceholderOptions"
            >
              <Draggable v-for="component in pageContainers.containers[1].components" :key="component.id">
                <div :class="component.props.className" class="drag-handle-comp general-news-comp" :style="component.props.style">
                  <p>{{ component.content }}</p>
                </div>
              </Draggable>
          </Container>
          </div>
      </Draggable>

      <Draggable class="home-draggable boards-news">
         <div :class="pageContainers.containers[2].props.className" :style="boardsContainerStyle">
            <div class="drag-handle">
              <span>&#x2630;</span>
              {{ pageContainers.containers[2].name }}
            </div>
            <Container group-name="col" 
            @drop="(event) => onComponentDrop(pageContainers.containers[2].id, event)" 
            :get-child-payload="getComponentPayload(pageContainers.containers[2].id)"
            drag-handle-selector=".drag-handle-comp"
            :drop-placeholder="dropPlaceholderOptions"
            >
              <Draggable v-for="component in pageContainers.containers[2].components" :key="component.id">
                <div :class="component.props.className" class="drag-handle-comp" :style="component.props.style">
                  <p>{{ component.content }}</p>
                </div>
              </Draggable>
          </Container>
          </div>
      </Draggable>

    </Container>

    
   
  </div>
</template>

<script>
// import BoardNews from "@/components/BoardNews.vue"
import { Container, Draggable } from "vue-smooth-dnd";
import { applyDrag, generateItems } from "@/utils/helpers.js";

const generalNewsContainerStyle = {backgroundColor: '#00a8e8'};
const boardsContainerStyle = {backgroundColor: '#007ea7'};

const containerNames = ["Boards", "Anunturi Generale", "Boards"];

// var boardsNews = [
// {
//   date: "04/07/2019",
//   day: "Mie.",
//   boardTitle: "Ingineria Programarii",
//   title: "Schimbare data examen",
//   content: "Examenul de pe data de 04/27/2019 s-a mutat pe data de 04/28/2019 la ora 10:00"
// },
// {
//   date: "04/07/2019",
//   day: "Mie.",
//   boardTitle: "Ingineria Programarii",
//   title: "Schimbare data examen-2",
//   content: "Examenul de pe data de 04/28/2019 s-a mutat pe data de 04/29/2019 la ora 10:00"
// },
// {
//   date: "04/07/2019",
//   day: "Mie.",
//   boardTitle: "Programare Avansata",
//   title: "Schimbare data examen",
//   content: "Examenul de pe data de 04/27/2019 s-a mutat pe data de 04/28/2019 la ora 10:00"
// }
// ];

// var generalNews = [
// {
//   date: "04/07/2019",
//   day: "Mie.",
//   title: "Secretariat",
//   content: "Studenti trebuie sa se prezinte la secretariat pentru a semna fisele semestriale in intervalul orar 10-12"
// },
// {
//   date: "04/07/2019",
//   day: "Mie.",
//   title: "Noutati",
//   content: "Campionatul European de Securitate Cibernetică, în România. Înscrierile, până pe 5 aprilie. Este ultimul prilej pentru ca toţi românii pasionaţi de IT să se înscrie la faza naţională a Campionatului European de Securitate Cibernetică de anul acesta din toamnă. Competiţia va avea loc pentru prima oară în România, la Palatul Parlamentului."
// }
// ];

// const components = generateItems(5, j => ({
//       id: `component${j}`,
//       props: {
//         className: 'container-component',
//         style: {backgroundColor: 'yellow'}
//       },
//       content: `component${j} maine dimineata`
//     }));

const containers = generateItems(3, i => ({
    id: `container${i}`,
    name: containerNames[i],
    props: {
      orientation: 'vertical',
      className: 'page-container',
      // style: {backgroundColor: 'red'}
    },
    components: generateItems(5, j => ({
      id: `component${j}${i}`,
      props: {
        className: 'container-component',
        // style: {backgroundColor: 'yellow'}
      },
      content: `component${i}${j} content`
    }))
  }));

const pageContainers = {
  props: {
    orientation: 'horizontal'
  },
  containers: containers
}

export default {
  name: "Simple",
  components: { Container, Draggable },
  data() {
    return {
      // boardsNews,
      // generalNews,
      boardsContainerStyle,
      generalNewsContainerStyle,
      pageContainers,
      upperDropPlaceholderOptions: {
        className: 'cards-drop-preview',
        animationDuration: '150',
        showOnTop: true
      },
      dropPlaceholderOptions: {
        className: 'drop-preview',
        animationDuration: '150',
        showOnTop: true
      }
    }
  },
  methods: {
    getComponentPayload (containerId) {
      return index => {
        return this.pageContainers.containers.filter(cont => cont.id === containerId)[0].components[index];
      }
    },
    onContainerDrop (dropResult) {
      const pageContainers = Object.assign({}, this.pageContainers);
      pageContainers.containers = applyDrag(pageContainers.containers, dropResult);
      this.pageContainers = pageContainers;
    },
    onComponentDrop (containerId, dropResult) {
      if (dropResult.removedIndex !== null || dropResult.addedIndex !== null) {
        const pageContainers = Object.assign({}, this.pageContainers);
        const container = pageContainers.containers.filter(cont => cont.id === containerId)[0];
        const containerIndex = pageContainers.containers.indexOf(container);

        const newContainer = Object.assign({}, container);
        newContainer.components = applyDrag(newContainer.components, dropResult);
        pageContainers.containers.splice(containerIndex, 1, newContainer);

        this.pageContainers = pageContainers;
      }
    }
  }
  
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.home-draggable{
  justify-items: center;
  align-items: center;
}

.home-draggable.boards-news{
  color: white;
  flex:1;
}

.home-draggable#generalNews{
  border: 5px solid #00171f;
  color: white;
  flex:1;

}


.drag-handle{
  user-select: none;
  height: 2em;
}

.drag-handle-comp{
  color: darkblue;
  background-color: #bbc7ce;
  height: 300px;
  width: 85%;
  margin-left: auto;
  margin-right: auto;
}

.drag-handle-comp.general-news-comp{
  height: 400px;
  width: 90%;
  color: darkblue;
}

#home{
  width:100%;
  display: flex;
  gap: 4px;
  justify-content: space-between;
}
</style>
