<template>
  <base-site-vue>
    <template #default>
      <section id="press">
        <base-intro-vue id="contact" class="border-bottom">
          <template #default>
            <div class="py-5 my-5 text-center">
              <h1 class="fw-bold mb-3">Join us. From anywhere.</h1>
              <p class="font-weight-bold">Want to help everyone become more productive at work? We’re hiring.</p>
  
              <a href="#jobs" class="btn btn-lg btn-primary">Job openings</a>
            </div>
          </template>
        </base-intro-vue>
  
        <div class="container">
          <!-- Presentation -->
          <div class="row mt-4 mb-2">
            <div class="col-12">
              <div class="row">
                <div class="col-12">
                  <h2 class="display-5 mb-3">How We Work</h2>
                </div>
  
                <div class="col-6 fw-light">
                  <p>
                    Freedom and flexibility. Spread across 17 time zones in 28 countries, we sign into Slack and open up our work tools on the schedule that fits our lives best. We communicate asynchronously, work autonomously, and take ownership of our work.
                    Diversity, inclusion, and belonging. We’re building a global community—one that’s safe for people of all backgrounds. We have regular open discussions on topics like gender equality, unconscious bias, and celebrating our differences. When you join our team, you agree to a code of conduct.
                    Camaraderie from afar. 100% distributed doesn’t hold us back from building bonds—daily conversation in chat includes non-work topics like #fun-cooking and #fun-scifi, weekly posts to our company blog show off pictures of pets and hobbies, and twice-annually, we come together for an all-team retreat that includes activities like crafting, basketball, karaoke, and rock climbing. We make space for whatever your flavor of fun.
                  </p>
                </div>
  
                <div class="col-6 fw-light">
                  <p>
                    Learning on- and offline. You start your role with an immersive remote onboarding experience to learn about our product, culture, and business. Then meet your team to pick up new skills and tools. And the learning doesn’t stop there—ongoing feedback from your manager and peers is one of our five team values, and we continuously support your professional development.
                    Interesting problems to solve. Our product integrates 3,000+ online tools to make it easy for anyone to connect apps and get more work done. Supporting and evolving our product is no easy task itself, though. Our "build the robot" value yields outsized results, and our all-hands support approach gives everyone insights into our users’ experience.
                  </p>
                </div>
              </div>
            </div>
          </div>
  
          <!-- Images -->
          <div class="row my-5 g-3">
            <div class="col-sm-12 col-md-6">
              <img src="https://images.unsplash.com/uploads/14110635637836178f553/dcc2ccd9?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Z2lybHxlbnwwfDB8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1280&q=60" class="img-fluid rounded shadow-sm" alt="work-environment" role="img">
            </div>
  
            <div class="col-sm-12 col-md-6">
              <img src="https://images.unsplash.com/photo-1510832198440-a52376950479?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Z2lybHxlbnwwfDB8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1280&q=60" class="img-fluid rounded shadow-sm" alt="work-environment" role="img">
            </div>
            
            <div class="col-sm-12 col-md-12">
              <img src="https://images.unsplash.com/photo-1469334031218-e382a71b716b?ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8Z2lybHxlbnwwfDB8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1280&q=60" class="img-fluid rounded shadow-sm" alt="work-environment" role="img">
            </div>
          </div>
  
          <!-- Presentation -->
          <div class="row mt-5 mb-3">
            <div class="col-12">
              <div class="row">
                <div class="col-6">
                  <h2 class="display-5 mb-3">How We Work</h2>
                  <p class="fw-light">
                    Freedom and flexibility. Spread across 17 time zones in 28 countries, we sign into Slack and open up our work tools on the schedule that fits our lives best. We communicate asynchronously, work autonomously, and take ownership of our work.
                    Diversity, inclusion, and belonging. We’re building a global community—one that’s safe for people of all backgrounds. We have regular open discussions on topics like gender equality, unconscious bias, and celebrating our differences. When you join our team, you agree to a code of conduct.
                    Camaraderie from afar. 100% distributed doesn’t hold us back from building bonds—daily conversation in chat includes non-work topics like #fun-cooking and #fun-scifi, weekly posts to our company blog show off pictures of pets and hobbies, and twice-annually, we come together for an all-team retreat that includes activities like crafting, basketball, karaoke, and rock climbing. We make space for whatever your flavor of fun.
                  </p>
                </div>
  
                <div class="col-6">
                  <img src="https://images.unsplash.com/photo-1497215728101-856f4ea42174?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8b2ZmaWNlfGVufDB8MHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=60" class="img-fluid rounded shadow-sm" alt="work-environment" role="img">
                </div>
              </div>
            </div>
          </div>
  
          <!-- Jobs -->
          <div id="jobs" class="row mt-5 mb-3">
            <div class="col-12">
              <h2 class="display-5 mb-4">Job Openings</h2>
  
              <article class="job">
                <h5 class="mt-2 mb-4">Accounting and Finance</h5>
                <div class="list-group">
                  <router-link :to="{ name: 'home_view' }" class="list-group-item list-group-item-action">Accounting and Finance - Director, FP&A</router-link>
                </div>
              </article>
            </div>
          </div>
        </div>
      </section>
    </template>
  </base-site-vue>
</template>

<script>
import BaseIntroVue from '@/layouts/BaseIntro.vue'
import BaseSiteVue from '@/layouts/BaseSite.vue'

export default {
    name: "JobsView",
    components: {
      BaseSiteVue,
      BaseIntroVue
    }
}
</script>
