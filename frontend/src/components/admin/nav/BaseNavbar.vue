<template>
  <nav class="navbar fixed-top navbar-expand-lg navbar-light white scrolling-navbar">
    <div class="container-fluid">
      <!-- Brand -->
      <router-link :to="{ name: 'admin_home' }" class="navbar-brand waves-effect">
        <strong class="blue-text">MDB</strong>
      </router-link>

      <!-- Collapse -->
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Links -->
      <div id="navbarSupportedContent" class="collapse navbar-collapse">
        <!-- Left -->
        <ul class="navbar-nav mr-auto">
          <!-- <li class="nav-item active">
            <a class="nav-link waves-effect" href="#">Home
              <span class="sr-only">(current)</span>
            </a>
          </li> -->
          <!-- <li class="nav-item">
            <a class="nav-link waves-effect" href="https://mdbootstrap.com/docs/jquery/" target="_blank">About
              MDB</a>
          </li> -->
          <!-- <li class="nav-item">
            <a class="nav-link waves-effect" href="https://mdbootstrap.com/docs/jquery/getting-started/download/" target="_blank">Free
              download</a>
          </li> -->
          <li class="nav-item">
            <a class="nav-link waves-effect" href="https://mdbootstrap.com/education/bootstrap/" target="_blank" rel="noopener noreferrer">
              Free tutorials
            </a>
          </li>
        </ul>

        <!-- Right -->
        <ul class="navbar-nav nav-flex-icons">
          <!-- <li class="nav-item">
            <a href="https://www.facebook.com/mdbootstrap" class="nav-link waves-effect" target="_blank">
              <i class="fab fa-facebook-f"></i>
            </a>
          </li>
          <li class="nav-item">
            <a href="https://twitter.com/MDBootstrap" class="nav-link waves-effect" target="_blank">
              <i class="fab fa-twitter"></i>
            </a>
          </li> -->
          <li class="nav-item">
            <router-link :to="{ name: 'home' }" class="nav-link border border-light rounded waves-effect" target="_blank" rel="noopener noreferrer">
              Go to website
            </router-link>
          </li>
        </ul>
      </div>

    </div>
  </nav>
</template>

<style scoped>
  .fixed-top {
    position: fixed;
    top: 0;
    right: 0;
    left: 0;
    z-index: 1030;
  }
</style>
