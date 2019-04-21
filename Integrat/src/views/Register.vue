<template>
  <div class="container">
    <div class="left">
      <div class="titlu">
        <div class="logo">
          <img src="../assets/logo-alb.png" alt="FiiStudent logo">
        </div>
      </div>
    </div>

    <div class="right-container">
      <div class="right">
        <div class="titlu">
          <h2>INREGISTRARE</h2>
        </div>
        <form action="login" method="get">
          <div class="pass-container">
            <input type="text" name="Email" placeholder="Email">
          </div>
          <div class="pass-container">
            <input type="text" name="Password" placeholder="Parola">
          </div>
          <div class="pass-container">
            <input type="text" name="RePassword" placeholder="Confirmare parola">
          </div>
          <div class="pass-container">
            <input type="text" name="Last" placeholder="Nume:">
          </div>
          <div class="pass-container">
            <input type="text" name="First" placeholder="Prenume:">
          </div>
          <div class="pass-container">
            <select id="rol">
              <option value disabled selected>Selecteaza rolul</option>
              <option value="Profesor">Profesor</option>
              <option value="Student">Student</option>
              <option value="Masterand">Masterand</option>
              <option value="Doctorand">Doctorand</option>
            </select>
          </div>

          <div class="pass-container">
            <select id="an">
              <option value disabled selected>Selecteaza anul</option>
              <option value="I">An I</option>
              <option value="II">An II</option>
              <option value="III">An III</option>
            </select>
          </div>
          <div class="pass-container">
            <select id="grupa">
              <option value disabled selected>Selecteaza grupa</option>
              <option value="A1">A1</option>
              <option value="A2">A2</option>
              <option value="A3">A3</option>
              <option value="A4">A4</option>
              <option value="A5">A5</option>
              <option value="A6">A6</option>
              <option value="A7">A7</option>
              <option value="B1">B1</option>
              <option value="B2">B2</option>
              <option value="B3">B3</option>
              <option value="B4">B4</option>
              <option value="B5">B5</option>
              <option value="B6">B6</option>
              <option value="B7">B7</option>
              <option value="X1">X1</option>
              <option value="X2">X2</option>
              <option value="X3">X3</option>
              <option value="alta">Alta grupa</option>
            </select>
          </div>
          <div class="pass-container">
            <select id="tip">
              <option value disabled selected>Selecteaza tipul de studiu</option>
              <option value="Licenta">Licenta</option>
              <option value="Master">Master</option>
              <option value="Doctorat">Doctorat</option>
            </select>
          </div>

          <div class="bottom">
            <input type="submit" value="Creeaza cont">
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.logo > img {
  height: 40vw;
  align-self: center;
}

* {
  margin: 0;
  padding: 0;
}
p {
  color: #35363a;
  font-family: Arial, Helvetica, sans-serif;
  font-style: normal;
  font-weight: normal;
}
a {
  font-family: Arial, Helvetica, sans-serif;
  font-style: normal;
  font-weight: normal;
}

h1 {
  font-family: Arial, Helvetica, sans-serif;
  font-style: normal;
  font-size: 50px;
  font-weight: normal;
}

h2 {
  color: #35363a;
  font-family: Arial, Helvetica, sans-serif;
  font-style: normal;
  font-size: 30px;
  font-weight: normal;
}

.container {
  display: flex;
  height: calc(100vh - 3.2vw);
}

.left {
  width: 100%;
  height: calc(100vh - 3.2vw);
  background-color: #3b3d6d;

  background-image: url("../assets/login-tech.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}

.left .titlu h1,
.left .titlu p {
  color: white;
}
.right-container {
  background-color: #e6e7f4;
  height: calc(100vh - 3.2vw);
  width: 100%;
}
.right {
  background-color: #e6e7f4;
  /* display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
    */
  width: 100%;
  height: calc(80vh - 3.5vw);
  margin-top: 5%;
}
.right .titlu {
  text-align: center;
  margin-bottom: 2.5vw;
}

form {
  height: 100%;
  width: 80%;
  margin: auto;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
}

form a {
  text-decoration: none;
  font-size: 18px;
  color: #45419a;
}

form .pass-container {
  text-align: center;
  width: 100%;
}

form .pass-container input[type="text"] {
  margin: auto;
}

form .bottom {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  margin-top: 2vw;
  height: 3vw;
}

select {
  border: none;
  color: white;
  background-image: linear-gradient(
    to right,
    #bfbedf,
    #c8c8e4,
    #d2d2ea,
    #dcddef,
    #e6e7f4
  );
  padding: 15px;
  width: 80%;
}

select option {
  color: black;
}
/* animation */

@keyframes expand {
  from {
    width: 0%;
  }
  to {
    width: 80%;
  }
}

@keyframes appear {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* end animations */

input[type="text"] {
  display: block;
  width: 80%;
  border-style: none;
  height: 50px;
  padding-left: 10px;
  box-sizing: border-box;

  background-image: linear-gradient(
    to right,
    #bfbedf,
    #c8c8e4,
    #d2d2ea,
    #dcddef,
    #e6e7f4
  );

  animation-name: expand;
  animation-duration: 2s;
}

input[type="text"]:focus {
  outline: none;
  border: 1px #7877b8 solid;
}

input[type="text"]::-webkit-input-placeholder {
  color: white;
}

input[type="submit"] {
  height: 40px;
  width: 120px;
  border: 1px solid #7877b8;
  background-color: #e6e7f4;
  color: #7877b8;
  font-weight: bold;
  border-radius: 20px;
}

input[type="submit"]:hover {
  transition: 200ms;
  height: 40px;
  width: 120px;
  border: 1px solid #7877b8;
  background-color: #7877b8;
  color: #e6e7f4;
  font-weight: bold;
  border-radius: 20px;
}
</style>
