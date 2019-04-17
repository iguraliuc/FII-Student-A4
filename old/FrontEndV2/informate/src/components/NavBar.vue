<template>
    <nav class = "navbar">
        <a class="logo">
            <img src="logo.png" alt="InforMate logo">
        </a>

        <form class = "search" action="/action_page.php">
            <input type="text" placeholder="Search.." name="search">
        </form>

        <ul class = "navlinks">
            <li class = "navitem dropdown"><a class="active dropli" href="#news">NewsFeed</a>
                <div class="dropdown-content">
                    <a href="#">Link 1</a>
                    <a href="#">Link 2</a>
                    <a href="#">Link 3</a>
                </div>
            </li>

            <li class = "navitem dropdown"><a class = "dropli" href="#board">Boarduri</a>
                <div class="dropdown-content">
                        <a href="#">Link 1</a>
                        <a href="#">Link 2</a>
                        <a href="#">Link 3</a>
                </div>
            </li>

            <li class = "navitem dropdown"><a class = "dropli" href="#orar">Orar</a>
                <div class="dropdown-content">
                        <a href="#">Link 1</a>
                        <a href="#">Link 2</a>
                        <a href="#">Link 3</a>
                </div>
            </li>

            <li class = "navitem dropdown"><a class = "dropli" href="#sali">Sali</a>
                <div class="dropdown-content">
                        <a href="#">Link 1</a>
                        <a href="#">Link 2</a>
                        <a href="#">Link 3</a>
                </div>
            </li>

            <li class = "navitem dropdown"><a class = "dropli" href="#profi">Cadre Didactice</a>
                <div class="dropdown-content">
                        <a href="#">Link 1</a>
                        <a href="#">Link 2</a>
                        <a href="#">Link 3</a>
                </div>
            </li>

            <li class = "navitem dropdown"><a class = "dropli" href="#internship">Internship</a>
                <div class="dropdown-content">
                        <a href="#">Link 1</a>
                        <a href="#">Link 2</a>
                        <a href="#">Link 3</a>
                </div>
            </li>

            <li class = "navitem dropdown"><a class = "dropli" href="#cont">Contul Meu</a>
                <div class="dropdown-content">
                        <a href="#">Link 1</a>
                        <a href="#">Link 2</a>
                        <a href="#">Link 3</a>
                </div>
            </li>
        </ul>
    </nav>
</template>



<script>
export default {
    
}
</script>


<style scoped>

  
  *, *::before, *::after {
    box-sizing: inherit;
    margin: 0;
    padding: 0;
    align-items: center;
  }
  
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  }

  .navbar {
    width: 100%;
    background-image: linear-gradient(260deg, #dad3ff 0%, #8d4b94   100%);
    padding-left: 30px;
    padding-right: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
  }
  
  .logo {
    display: inline-block;
  }
    
  .logo img {
    width: 50px;
    vertical-align: middle;
  }
  
  .search {
    border: 1px solid #8d4b94;
    
  }

  .search input[type = text] {
    text-align: left;
    width: 100%;
    margin: 0;
    padding: 8px;
  }

  .navlinks {
    list-style: none;
    display: flex;
    overflow: hidden;
  }
  
  .navitem {
    float: left;
  }

  .navitem a {
    display: inline-block;
    padding: 10px 15px;
    text-decoration: none;
    color: black;
    text-align: center;
  }
  
  .navitem a.active {
    color: darkgreen;
    background-color:#dec5fc;
    font-weight: bold;
    border-radius: 15px 50px 30px;
    border: 1px solid #8d4b94;
  }

  .navitem:hover {
    background-color: #dec5fc;
    color: darkgreen;
    border-radius: 30px;
    border: 1px solid #8d4b94;
  }
  
  .navitem:hover a {
    color: darkgreen;
  }

  .dropdown:hover .dropbtn {
    background-color: darkgreen;
  }

  .dropdown {
    display: inline-block;
  }

  .dropdown-content {
    display: none;
    position: absolute;
    background-color: white; /*#b8a9c9*/
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
  }

  .dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-align: center;
  }
  
  .dropdown-content a:hover {
    background-color: #f1f1f1
  }
  
  .dropdown:hover .dropdown-content {
    display: block;
  }
</style>
