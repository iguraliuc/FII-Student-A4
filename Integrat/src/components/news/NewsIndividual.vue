<template>
  <div class="container">
    <div class="board">
      <p>Materii-Ingineria Programarii</p>
      <h1>Acesta este titlul</h1>
      <div class="subtitle">
        <p>
          <i>-Autorul-</i>
        </p>
        <p>08/09/2019 Miercuri</p>
      </div>
      <div class="content">
        <p>
          Este ultimul prilej pentru ca toţi românii pasionaţi de IT să se înscrie la faza naţională a Campionatului European de Securitate Cibernetică de anul acesta din toamnă. Competiţia va avea loc pentru prima oară în România, la Palatul Parlamentului. Scopul este de la le testa tinerilor europeni aptitudinile de „hackeri”.
          În Campionatul European de Securitate Cibernetică de anul acesta, se vor întrece peste 20 de echipe din toată Europa. Acestea sunt formate din 5 juniori şi 5 seniori cu vârste între 16 şi 25 de ani care să îşi reprezinte ţara în competiţie. Organizatorii aşteaptă ca românii pasionaţi de securitate cibernetică să se înscrie într-un număr căt mai mare la faza naţională.
          Anton Rog – director Cyberint: „Există un site, cybersecuritychallenge.ro. Avem deja 300 de tineri. Înscrierile se pot face până pe 5 aprilie. Etapa de selecţie iniţială presupune rezolvarea unui număr de probe. Cei mai buni 30, pentru că o să avem nevoie şi de rezerve la lot, vor fi selectaţi pentru stagiile de pregătire”.
          Astfel, pentru a se pregăti de campionat, tinerii sunt antrenaţi intensiv de specialişti în domeniul securităţii cibernetice.
          Andrei Avădanei – coordonator tehnic: „Scopul este să-i învăţăm anumite tehnici de exploatare, de pivotare, de atac în infrastructură, dar şi să protejeze anumite tehnologii. Rolul activităţii este acela de a selecta cei mai buni 10 finalişti. Am pregătit o serie de probleme şi provocări care vor simula foarte mult din ce vor simula în etapa finală”.
          Cătălin Aramă – director CERT.RO: „Este un eveniment important pentru că implică tinerii în cadrul acestui campionat. Noi vorbim de educaţie digitală, vorbim de educaţie cibernetică şi vorbim de nevoia unei culturi a riscului de securitate cibernetică de la vârste cât se poate de fragede”.
          De-a lungul timpului, România a reuşit să fie vicecampioană de două ori, iar anul trecut a ieşit pe locul 9.
          Matei Bădănoiu – participant anul trecut în echipa României: „Am fost la etapa din 2018. (….) Faza de calificare a fost puţin grea. Ai nevoie de un pic de experienţă şi recomand oricui. Chiar dacă nu crede că are putere în el să treacă de prima etapă, totuşi, să încerce. E o experienţă unică”.
          A cincea ediţie a Campionatului European de Securitate Cibernetică va avea loc în în România, la Palatul Parlamentului, între 9 şi 11 octombrie, anul acesta.
        </p>
      </div>
    </div>

    <router-link to="/home" class="meniu">
      <img src="@/assets/undo-solid.svg">
      <p>Intoarcere la pagina cu anunturi!</p>
    </router-link>
  </div>
</template>


<script>
export default {};
</script>


<style scoped>
* {
  margin: 0px;
  padding: 0px;
  font-size: 15px;
}
body {
  font-family: "Montserrat";
}

li {
  list-style: none;
}

.board h1 {
  font-size: 40px;
  margin-bottom: 10px;
}

.subtitle {
  margin: auto;
  width: 80%;
  display: flex;
  justify-content: space-between;
  border-bottom: 1px gray solid;
  padding-bottom: 10px;
}

.subtitle > p:last-child {
  color: gray;
}
.container {
  margin: auto;
  margin-top: 20px;
  width: 80%;
  display: flex;
}
.board {
  text-align: center;
  width: 80%;
  box-shadow: 3px 0px 6px 4px rgba(0, 0, 0, 0.16);
  -moz-box-shadow: 3px 0px 6px 4px rgba(0, 0, 0, 0.16);
  -webkit-box-shadow: 3px 0px 6px 4px rgba(0, 0, 0, 0.16);
  padding: 50px;
  box-sizing: border-box;
}

.board .content {
  margin-top: 20px;
}

.board > p:first-child {
  padding: 5px;
  background-color: #09bcff;
  color: white;
  width: 20%;
  font-weight: bold;
  font-size: 20px;
}
.meniu {
  width: 18%;
  box-shadow: 3px 0px 6px 4px rgba(0, 0, 0, 0.16);
  -moz-box-shadow: 3px 0px 6px 4px rgba(0, 0, 0, 0.16);
  -webkit-box-shadow: 3px 0px 6px 4px rgba(0, 0, 0, 0.16);
  margin-left: 20px;
  display: flex;
  justify-content: space-around;
  height: 100px;
  padding: 10px;
}

.meniu:hover {
  transition: 0.5s;
  width: 18%;
  box-shadow: 3px 0px 6px 4px rgba(0, 0, 0, 0.16);
  -moz-box-shadow: 3px 0px 6px 4px rgba(0, 0, 0, 0.16);
  -webkit-box-shadow: 3px 0px 6px 4px rgba(0, 0, 0, 0.16);
  margin-left: 20px;
  display: flex;
  justify-content: space-around;
  height: 100px;
  padding: 10px;
  background-color: #09bcff;
}
.meniu:hover p {
  color: white;
}
.meniu {
  text-align: center;
  text-decoration: none;
}
.meniu p {
  margin: auto;
}
.meniu img {
  width: 50px;
}

.btn {
  border: none;
  outline: none;
  padding: 12px 16px;
  background-color: #f1f1f1;
  cursor: pointer;
  display: block;
  width: 100%;
  margin-bottom: 10px;
}

.btn:hover {
  background-color: #ddd;
}

.btn.active {
  background-color: #666;
  color: white;
}
</style>
