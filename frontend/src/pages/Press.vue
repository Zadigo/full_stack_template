<template>
  <base-jumbotron sectionId="press" pageTitle="Press" pageDescription="A quick description">
    <div class="container">

      <!-- Top -->
      <section class="border-bottom pb-4 mb-5">
        <div class="row gx-5">
          <div class="col-md-6 mb-4">
            <div class="bg-image hover-overlay ripple shadow-2-strong rounded-5" data-mdb-ripple-color="light">
              <img :src="news.newsOfTheDay.image" class="img-fluid" />
              <router-link :to="{ name: '', params: { id: 0 } }">
                <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
              </router-link>
            </div>
          </div>

          <div class="col-md-6 mb-4">
            <span class="badge bg-danger px-2 py-1 shadow-1-strong mb-3">
              {{ news.newsOfTheDay.title }}
            </span>
            <h4><strong>Facilis consequatur eligendi</strong></h4>
            <p class="text-muted">{{ news.newsOfTheDay.content }}</p>

            <button type="button" class="btn btn-primary">Read more</button>
          </div>
        </div>
      </section>

      <section>
        <div class="row gx-lg-5">
          <!-- News block -->
          <div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
            <div>
              <!-- Featured image -->
              <div class="bg-image hover-overlay shadow-1-strong ripple rounded-5 mb-4" data-mdb-ripple-color="light">
                <img src="https://mdbootstrap.com/img/new/fluid/city/113.jpg" class="img-fluid" />
                <a href="#!">
                  <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
                </a>
              </div>

              <!-- Article data -->
              <div class="row mb-3">
                <div class="col-6">
                  <a href="" class="text-info">
                    <i class="fas fa-plane"></i>
                    Travels
                  </a>
                </div>

                <div class="col-6 text-end">
                  <u> 15.07.2020</u>
                </div>
              </div>

              <!-- Article title and description -->
              <a href="" class="text-dark">
                <h5>This is title of the news</h5>

                <p>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit, iste aliquid. Sed
                  id nihil magni, sint vero provident esse numquam perferendis ducimus dicta
                  adipisci iusto nam temporibus modi animi laboriosam?
                </p>
              </a>

              <hr />

              <!-- News -->
              <a href="" class="text-dark">
                <div class="row mb-4 border-bottom pb-2">
                  <div class="col-3">
                    <img src="https://mdbootstrap.com/img/new/standard/city/041.jpg"
                        class="img-fluid shadow-1-strong rounded" alt="" />
                  </div>

                  <div class="col-9">
                    <p class="mb-2"><strong>Lorem ipsum dolor sit amet</strong></p>
                    <p>
                      <u> 15.07.2020</u>
                    </p>
                  </div>
                </div>
              </a>

              <!-- News -->
              <a href="" class="text-dark">
                <div class="row mb-4 border-bottom pb-2">
                  <div class="col-3">
                    <img src="https://mdbootstrap.com/img/new/standard/city/042.jpg"
                        class="img-fluid shadow-1-strong rounded" alt="" />
                  </div>

                  <div class="col-9">
                    <p class="mb-2"><strong>Lorem ipsum dolor sit amet</strong></p>
                    <p>
                      <u> 15.07.2020</u>
                    </p>
                  </div>
                </div>
              </a>

              <!-- News -->
              <a href="" class="text-dark">
                <div class="row mb-4 border-bottom pb-2">
                  <div class="col-3">
                    <img src="https://mdbootstrap.com/img/new/standard/city/043.jpg"
                        class="img-fluid shadow-1-strong rounded" alt="" />
                  </div>

                  <div class="col-9">
                    <p class="mb-2"><strong>Lorem ipsum dolor sit amet</strong></p>
                    <p>
                      <u> 15.07.2020</u>
                    </p>
                  </div>
                </div>
              </a>

              <!-- News -->
              <a href="" class="text-dark">
                <div class="row mb-4 border-bottom pb-2">
                  <div class="col-3">
                    <img src="https://mdbootstrap.com/img/new/standard/city/044.jpg"
                        class="img-fluid shadow-1-strong rounded" alt="" />
                  </div>

                  <div class="col-9">
                    <p class="mb-2"><strong>Lorem ipsum dolor sit amet</strong></p>
                    <p>
                      <u> 15.07.2020</u>
                    </p>
                  </div>
                </div>
              </a>
            </div>
            <!-- News block -->
          </div>

          <div class="col-lg-4 col-md-6 mb-4 mb-lg-0">
            <!-- News block -->
            <div>
              <!-- Featured image -->
              <div class="bg-image hover-overlay shadow-1-strong rounded-5 ripple mb-4" data-mdb-ripple-color="light">
                <img src="https://mdbootstrap.com/img/new/fluid/city/011.jpg" class="img-fluid" />
                <a href="#!">
                  <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
                </a>
              </div>

              <!-- Article data -->
              <div class="row mb-3">
                <div class="col-6">
                  <a href="" class="text-danger">
                    <i class="fas fa-chart-pie"></i>
                    Business
                  </a>
                </div>

                <div class="col-6 text-end">
                  <u> 15.07.2020</u>
                </div>
              </div>

              <!-- Article title and description -->
              <a href="" class="text-dark">
                <h5>This is title of the news</h5>

                <p>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit, iste aliquid. Sed
                  id nihil magni, sint vero provident esse numquam perferendis ducimus dicta
                  adipisci iusto nam temporibus modi animi laboriosam?
                </p>
              </a>

              <hr />

              <!-- News -->
              <a href="" class="text-dark">
                <div class="row mb-4 border-bottom pb-2">
                  <div class="col-3">
                    <img src="https://mdbootstrap.com/img/new/standard/city/031.jpg"
                        class="img-fluid shadow-1-strong rounded" alt="" />
                  </div>

                  <div class="col-9">
                    <p class="mb-2"><strong>Lorem ipsum dolor sit amet</strong></p>
                    <p>
                      <u> 15.07.2020</u>
                    </p>
                  </div>
                </div>
              </a>

              <!-- News -->
              <a href="" class="text-dark">
                <div class="row mb-4 border-bottom pb-2">
                  <div class="col-3">
                    <img src="https://mdbootstrap.com/img/new/standard/city/032.jpg"
                        class="img-fluid shadow-1-strong rounded" alt="" />
                  </div>

                  <div class="col-9">
                    <p class="mb-2"><strong>Lorem ipsum dolor sit amet</strong></p>
                    <p>
                      <u> 15.07.2020</u>
                    </p>
                  </div>
                </div>
              </a>

              <!-- News -->
              <a href="" class="text-dark">
                <div class="row mb-4 border-bottom pb-2">
                  <div class="col-3">
                    <img src="https://mdbootstrap.com/img/new/standard/city/033.jpg"
                        class="img-fluid shadow-1-strong rounded" alt="" />
                  </div>

                  <div class="col-9">
                    <p class="mb-2"><strong>Lorem ipsum dolor sit amet</strong></p>
                    <p>
                      <u> 15.07.2020</u>
                    </p>
                  </div>
                </div>
              </a>

              <!-- News -->
              <a href="" class="text-dark">
                <div class="row mb-4 border-bottom pb-2">
                  <div class="col-3">
                    <img src="https://mdbootstrap.com/img/new/standard/city/034.jpg"
                        class="img-fluid shadow-1-strong rounded" alt="" />
                  </div>

                  <div class="col-9">
                    <p class="mb-2"><strong>Lorem ipsum dolor sit amet</strong></p>
                    <p>
                      <u> 15.07.2020</u>
                    </p>
                  </div>
                </div>
              </a>
            </div>
            <!-- News block -->
          </div>

          <div class="col-lg-4 col-md-6 mb-4 mb-lg-0">
            <!-- News block -->
            <div>
              <!-- Featured image -->
              <div class="bg-image hover-overlay shadow-1-strong rounded-5 ripple mb-4" data-mdb-ripple-color="light">
                <img src="https://mdbootstrap.com/img/new/fluid/city/018.jpg" class="img-fluid" />
                <a href="#!">
                  <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
                </a>
              </div>

              <!-- Article data -->
              <div class="row mb-3">
                <div class="col-6">
                  <a href="" class="text-warning">
                    <i class="fas fa-code"></i>
                    Technology
                  </a>
                </div>

                <div class="col-6 text-end">
                  <u> 15.07.2020</u>
                </div>
              </div>

              <!-- Article title and description -->
              <a href="" class="text-dark">
                <h5>This is title of the news</h5>

                <p>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit, iste aliquid. Sed
                  id nihil magni, sint vero provident esse numquam perferendis ducimus dicta
                  adipisci iusto nam temporibus modi animi laboriosam?
                </p>
              </a>

              <hr />

              <!-- News -->
              <a href="" class="text-dark">
                <div class="row mb-4 border-bottom pb-2">
                  <div class="col-3">
                    <img src="https://mdbootstrap.com/img/new/standard/city/011.jpg"
                        class="img-fluid shadow-1-strong rounded" alt="" />
                  </div>

                  <div class="col-9">
                    <p class="mb-2"><strong>Lorem ipsum dolor sit amet</strong></p>
                    <p>
                      <u> 15.07.2020</u>
                    </p>
                  </div>
                </div>
              </a>

              <!-- News -->
              <a href="" class="text-dark">
                <div class="row mb-4 border-bottom pb-2">
                  <div class="col-3">
                    <img src="https://mdbootstrap.com/img/new/standard/city/012.jpg"
                        class="img-fluid shadow-1-strong rounded" alt="" />
                  </div>

                  <div class="col-9">
                    <p class="mb-2"><strong>Lorem ipsum dolor sit amet</strong></p>
                    <p>
                      <u> 15.07.2020</u>
                    </p>
                  </div>
                </div>
              </a>

              <!-- News -->
              <a href="" class="text-dark">
                <div class="row mb-4 border-bottom pb-2">
                  <div class="col-3">
                    <img src="https://mdbootstrap.com/img/new/standard/city/013.jpg"
                        class="img-fluid shadow-1-strong rounded" alt="" />
                  </div>

                  <div class="col-9">
                    <p class="mb-2"><strong>Lorem ipsum dolor sit amet</strong></p>
                    <p>
                      <u> 15.07.2020</u>
                    </p>
                  </div>
                </div>
              </a>

              <!-- News -->
              <a href="" class="text-dark">
                <div class="row mb-4 border-bottom pb-2">
                  <div class="col-3">
                    <img src="https://mdbootstrap.com/img/new/standard/city/014.jpg"
                        class="img-fluid shadow-1-strong rounded" alt="" />
                  </div>

                  <div class="col-9">
                    <p class="mb-2"><strong>Lorem ipsum dolor sit amet</strong></p>
                    <p>
                      <u> 15.07.2020</u>
                    </p>
                  </div>
                </div>
              </a>
            </div>
            <!-- News block -->
          </div>
        </div>
      </section>

      <nav class="my-4" aria-label="...">
        <ul class="pagination pagination-circle justify-content-center">
          <li class="page-item">
            <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
          </li>
          <li class="page-item"><a class="page-link" href="#">1</a></li>
          <li class="page-item active" aria-current="page">
            <a class="page-link" href="#">2</a>
          </li>
          <li class="page-item"><a class="page-link" href="#">3</a></li>
          <li class="page-item">
            <a class="page-link" href="#">Next</a>
          </li>
        </ul>
      </nav>
    </div>
  </base-jumbotron>
</template>

<script>
export default {
  name: 'Press',
  data () {
    return {
      news: {
        newsOfTheDay: {
          title: 'Facilis consequatur eligendi',
          image: 'https://mdbootstrap.com/img/new/slides/080.jpg',
          content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis consequatur eligendi quisquam doloremque vero ex debitis veritatis placeat unde animi laborum sapiente illo possimus, commodi dignissimos obcaecati illum maiores corporis.'
        },
        articles: [
          {
            mainTitle: 'Travels',
            createdOn: '15.07.2020',
            subtitle: 'This is title of the news',
            image: 'https://mdbootstrap.com/img/new/standard/city/041.jpg',
            content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit, iste aliquid. Sed id nihil magni, sint vero provident esse numquam perferendis ducimus dicta adipisci iusto nam temporibus modi animi laboriosam?'
          }
        ]
      }
    }
  }
}
</script>
