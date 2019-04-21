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
          <h1>LOG IN</h1>
          <h3>Bine ati venit!</h3>
        </div>
        <form>
          <div class="icon">
            <img src="@/assets/user-solid.svg">
            <div class="pass-container">
              <input type="text" name="Username" placeholder="Username">
            </div>
          </div>
          <div class="icon">
            <img src="@/assets/unlock-alt-solid.svg">
            <div class="pass-container">
              <input type="text" name="Password" placeholder="Password">
              <router-link to="/forgot-password" class="a-class">Am uitat parola</router-link>
            </div>
          </div>
          <div class="bottom">
            <input type="submit" value="LOG IN">
            <router-link to="/register" class="a-class">Creeaza un cont</router-link>
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
  height: 20vw;
  align-self: center;
  position: relative;
  top: 20vh;
}

* {
  margin: 0;
  padding: 0;
}
p {
  color: #35363a;
  font-family: "Verdana", Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
}

h1,
h3 {
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

h3 {
  font-size: 20px;
}
.container {
  display: flex;
  height: calc(100vh - 3.2vw);
}

.left {
  width: 50%;
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
  margin-top: 10%;
}
.right .titlu {
  text-align: center;
}

form {
  height: 90%;
  width: 80%;
  margin: auto;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
}

form .a-class {
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

form img {
  margin-right: auto;
  height: 100%;
}
form .icon {
  height: 50px;
  display: flex;
  width: 100%;
  justify-content: center;

  animation-name: appear;
  animation-duration: 2s;
}
form .bottom {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  height: 70px;
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
