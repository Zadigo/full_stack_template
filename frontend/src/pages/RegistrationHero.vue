<template>
  <div id="hero">
    <header>
      <div class="bg-image shadow-2-strong" id="intro">
        <div class="mask d-flex align-items-center">
          <div class="container h-100">
            <router-view />
          </div>
        </div>
      </div>
    </header>
  </div>
</template>

<style scoped>
  #intro {
    background-image: url("https://images.unsplash.com/photo-1619785690726-89c6b3bd3849?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1280&q=80");
    height: 100vh;
  }
</style>
