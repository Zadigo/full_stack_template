<template>
  <section class="section team-section mt-2 mb-6" id="team">
    <div class="container">
      <div class="row">

        <div class="col-md-12 div-color-2">
          <div class="divider-new">
            <h3 class="text-center font-up font-bold mr-3 ml-3">
              Our Guests opinions
            </h3>
          </div>
        </div>

        <p class="section-description">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, error amet 
          numquam iure provident voluptate esse quasi, veritatis totam voluptas nostrum 
          quisquam eum porro a pariatur accusamus veniam.
        </p>

        <div class="row text-center">

          <div v-for="(teamate, index) in teamates" :key="index" class="col-md-4 mb-r">
            <div class="testimonial">
              <div class="avatar">
                <img :src="teamate.image" class="rounded-circle img-fluid z-depth-1-half">
              </div>

              <!--Content-->
              <h4>{{ teamate.author }}</h4>
              <p><i class="fa fa-quote-left "></i> {{ teamate.content }}</p>

              <!--Review-->
              <div class="green-text">
                <font-awesome-icon v-for="score in teamate.score" :key="score" icon="star"></font-awesome-icon>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Team',
  data () {
    return {
      teamates: [
        {
          image: 'https://mdbootstrap.com/img/Photos/Avatars/img%20%285%29.jpg',
          author: 'Anna Deynah',
          content: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quod eos id officiis hic tenetur quae quaerat ad velit ab.',
          score: 5
        },
        {
          image: 'https://mdbootstrap.com/img/Photos/Avatars/img%20%289%29.jpg',
          author: 'John Doe',
          content: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quod eos id officiis hic tenetur quae quaerat ad velit ab.',
          score: 3
        },
        {
          image: 'https://mdbootstrap.com/img/Photos/Avatars/img%20%288%29.jpg',
          author: 'Tom Smith',
          content: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quod eos id officiis hic tenetur quae quaerat ad velit ab.',
          score: 5
        }
      ]
    }
  }
}
</script>

<style scoped>
  .section-description {
    color: #757575;
    margin-bottom: 4rem;
    /* margin-left: 15%; */
    /* margin-right: 15%; */
    text-align: center;
  }

  .section.team-section .avatar .rounded-circle {
    max-width: 170px;
  }
  
  .section.team-section .avatar img {
    max-width: 200px;
    height: auto;
  }
  
  .section img {
    width: 100%;
    height: auto;
  }

  .section.team-section .avatar {
    margin-bottom: 2rem;
    height: auto;
  }
</style>
