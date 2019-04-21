<template>
  <div>
    <div class="filtru">
      <button class="button toti active" v-on:click="filter('Toti')">Toti anii</button>
      <button class="button anI" v-on:click="filter('An I')">An I</button>
      <button class="button anII" v-on:click="filter('An II')">An II</button>
      <button class="button anIII" v-on:click="filter('An III')">An III</button>
    </div>
    <div class="main">
      <div class="card">
        <div class="box">
          <div class="box-container">
            <div class="top-container">
              <p class="titlu">MATEMATICA</p>
              <p class="an">An I</p>
              <p class="prof">Lect. dr. Florin Iacob/Lect. dr. Andreea Arusoaie</p>
            </div>
            <div class="bottom-container">
              <p
                class="descriere"
              >Prezentarea unor elemente de matematică utile în abordarea și parcurgerea programelor analitice ale disciplinelor de informatică prevăzute în cadrul studiilor de licență.</p>
            </div>
          </div>
        </div>
        <div class="triangle"></div>
        <button class="btn">JOIN BOARD</button>

        <button class="btn verified">
          Joined!
          <img src="correct.png">
        </button>
      </div>
      <div class="card">
        <div class="box">
          <div class="box-container">
            <div class="top-container">
              <p class="titlu">MATEMATICA</p>
              <p class="an">An I</p>
              <p class="prof">Lect. dr. Florin Iacob/Lect. dr. Andreea Arusoaie</p>
            </div>
            <div class="bottom-container">
              <p
                class="descriere"
              >Prezentarea unor elemente de matematică utile în abordarea și parcurgerea programelor analitice ale disciplinelor de informatică prevăzute în cadrul studiilor de licență.</p>
            </div>
          </div>
        </div>
        <div class="triangle"></div>
        <button class="btn">JOIN BOARD</button>

        <button class="btn verified">
          Joined!
          <img src="correct.png">
        </button>
      </div>
      <div class="card">
        <div class="box">
          <div class="box-container">
            <div class="top-container">
              <p class="titlu">MATEMATICA</p>
              <p class="an">An I</p>
              <p class="prof">Lect. dr. Florin Iacob/Lect. dr. Andreea Arusoaie</p>
            </div>
            <div class="bottom-container">
              <p
                class="descriere"
              >Prezentarea unor elemente de matematică utile în abordarea și parcurgerea programelor analitice ale disciplinelor de informatică prevăzute în cadrul studiilor de licență.</p>
            </div>
          </div>
        </div>
        <div class="triangle"></div>

        <button class="btn">JOIN BOARD</button>

        <button class="btn verified">
          Joined!
          <img src="correct.png">
        </button>
      </div>

      <div class="card">
        <div class="box">
          <div class="box-container">
            <div class="top-container">
              <p class="titlu">LOGICA</p>
              <p class="an">An II</p>
              <p class="prof">Lect. dr. Florin Iacob/Lect. dr. Andreea Arusoaie</p>
            </div>
            <div class="bottom-container">
              <p
                class="descriere"
              >Prezentarea unor elemente de matematică utile în abordarea și parcurgerea programelor analitice ale disciplinelor de informatică prevăzute în cadrul studiilor de licență.</p>
            </div>
          </div>
        </div>
        <div class="triangle"></div>

        <button class="btn">JOIN BOARD</button>

        <button class="btn verified">
          Joined!
          <img src="@/assets/correct.png">
        </button>
      </div>

      <div class="card">
        <div class="box">
          <div class="box-container">
            <div class="top-container">
              <p class="titlu">MATEMATICA</p>
              <p class="an">An III</p>
              <p class="prof">Lect. dr. Florin Iacob/Lect. dr. Andreea Arusoaie</p>
            </div>
            <div class="bottom-container">
              <p
                class="descriere"
              >Prezentarea unor elemente de matematică utile în abordarea și parcurgerea programelor analitice ale disciplinelor de informatică prevăzute în cadrul studiilor de licență.</p>
            </div>
          </div>
        </div>
        <div class="triangle"></div>

        <button class="btn">JOIN BOARD</button>

        <button class="btn verified">
          Joined!
          <img src="correct.png">
        </button>
      </div>

      <div class="card">
        <div class="box">
          <div class="box-container">
            <div class="top-container">
              <p class="titlu">Limbaje formale, automate si calculatoare</p>
              <p class="an">An II</p>
              <p class="prof">Lect. dr. Florin Iacob/Lect. dr. Andreea Arusoaie</p>
            </div>
            <div class="bottom-container">
              <p
                class="descriere"
              >Prezentarea unor elemente de matematică utile în abordarea și parcurgerea programelor analitice ale disciplinelor de informatică prevăzute în cadrul studiilor de licență.</p>
            </div>
          </div>
        </div>
        <div class="triangle"></div>

        <button class="btn">JOIN BOARD</button>

        <button class="btn verified">
          Joined!
          <img src="correct.png">
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    filter(an) {
      var btns = document.getElementsByClassName("button");

      for (var i = 0; i < btns.length; i++) {
        btns[i].addEventListener("click", function() {
          var current = document.getElementsByClassName("active");
          current[0].className = current[0].className.replace(" active", "");
          this.className += " active";
        });
      }

      var button = document.getElementsByClassName("an");
      for (var i = 0; i < button.length; i++) {
        var board =
          button[i].parentElement.parentElement.parentElement.parentElement;
        if (button[i].textContent != an) {
          if (an == "Toti") {
            board.style.display = "block";
            board.style.visibility = "visible";
          } else {
            board.style.display = "none";
            board.style.visibility = "hidden";
          }
        } else {
          board.style.display = "block";
          board.style.visibility = "visible";
        }
      }
    },
    join() {
      var joined = document.getElementsByClassName("btn");
      for (var i = 0; i < joined.length; i++) {
        if (joined[i].className.includes("joined")) {
          joined[i].style.display = "none";
          joined[i].style.visibility = "hidden";

          var verified = joined[i].parentElement.getElementsByClassName(
            "verified"
          )[0];
          verified.style.display = "block";
          verified.style.visibility = "visible";
        }
      }
    },
    main() {
      var btns = document.getElementsByClassName("btn");
      for (var i = 0; i < btns.length; i++) {
        btns[i].addEventListener("click", function() {
          if (this.className.includes("joined")) {
            this.className = this.className.replace(" joined", "");
          } else if (!this.className.includes("verified")) {
            this.className += " joined";
          }

          if (this.className.includes("verified")) {
            this.style.display = "none";
            this.style.visibility = "hidden";
            var show = this.parentElement.getElementsByClassName("joined")[0];
            show.className = show.className.replace(" joined", "");
            show.style.display = "block";
            show.style.visibility = "visible";
          }
          join();
        });
      }
    }
  }
};
</script>

<style scoped>
* {
  margin: 0px;
  padding: 0px;
  font-size: 15px;
  box-sizing: border-box;
}

body {
  font-family: "Montserrat";
}

.filtru {
  top: 0;
  position: sticky;
  display: flex;
  width: 100%;
  z-index: 11;
}

.filtru .anI,
.filtru .anII,
.filtru .anIII,
.filtru .toti {
  text-align: center;
  background-color: rgb(32, 32, 32);
  color: white;
  padding: 1em;
  border-style: none;
  font-size: 1.3em;
  width: 100%;
}

.filtru .active {
  background-color: gray;
}

.filtru button:hover {
  transition: 0.3s;
  text-align: center;
  background-color: gray;
  color: white;
  padding: 1em;
  border-style: none;
  font-size: 1.3em;
  width: 100%;
}
.main {
  margin: 0 auto;
  width: 80%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
.card {
  position: relative;
  width: 300px;
  height: 550px;
  margin-right: 20px;
  margin-left: 20px;
}

.card:hover {
  position: relative;
  width: 320px;
  height: 550px;
  margin-right: 20px;
  margin-left: 20px;
  transition: 0.5s;
}
.card:hover .box {
  box-shadow: 3px 0px 8px 8px rgba(0, 0, 0, 0.16);
  background-color: #2c34a2;
  width: 100%;
  height: 80%;
  transition: 0.5s;
}
.card:hover .triangle {
  width: 0;
  height: 0;
  border-left: 160px solid transparent;
  border-right: 160px solid transparent;
  border-top: 100px solid #2c34a2;
  transition: 0.5s;
}
.box {
  box-shadow: 3px 0px 6px 4px rgba(0, 0, 0, 0.16);
  background-color: #2c34a2;
  width: 100%;
  height: 80%;
}

.box .box-container {
  height: 90%;
  display: flex;
  flex-direction: column;
  align-content: space-between;
}
.box .top-container {
  padding-top: 2em;
  height: 100%;
  width: 80%;
  margin: 0 auto;
  padding-bottom: 2em;
}

.box .top-container p {
  text-align: center;
  color: white;
  width: 100%;
}

.box .titlu {
  width: 100%;
  font-size: 1.2em;
  font-weight: bold;
}
.box .an,
.box .prof {
  margin-top: 1em;
  font-size: 1em;
  width: 60%;
}
.box .prof {
  font-style: italic;
}
.box .bottom-container {
  width: 100%;
  margin-right: auto;
  margin-left: auto;
  background-color: white;
  width: 100%;
}

.box .descriere {
  margin-right: auto;
  margin-left: auto;
  padding: 1em;
  text-align: center;
  color: black;
  width: 80%;
  font-size: 1em;
}

.triangle {
  width: 0;
  height: 0;
  border-left: 150px solid transparent;
  border-right: 150px solid transparent;
  border-top: 100px solid #2c34a2;
}

.btn {
  text-align: center;
  background-color: #a80db0;
  color: white;
  padding: 0.5em;
  border-style: none;
  font-size: 1em;
  border-radius: 50%;

  width: 100px;
  height: 80px;
  bottom: 12%;
  left: 33%;
  position: absolute;
}

.verified {
  width: 100px;
  height: 80px;
  bottom: 12%;
  left: 33%;
  position: absolute;
  text-align: center;
  background-color: #6ae5d3;
  color: white;
  padding: 0.5em;
  border-style: none;
  font-size: 1em;
  visibility: hidden;
  display: none;
  border-radius: 50%;
}

.verified img {
  width: 50%;
}
</style>
