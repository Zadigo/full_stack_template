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
    background-image: url("https://images.unsplash.com/photo-1516575150278-77136aed6920?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MzR8fG1vZGVsfGVufDB8MHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1280&q=60");
    height: 100vh;
  }
</style>
