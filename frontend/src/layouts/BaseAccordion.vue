<template>
  <div :id="'accordionExample'" :class="{ 'accordion-flush': flushed }" class="accordion">
    <div v-for="(item, i) in computedItems" :key="i" class="accordion-item" @click="expandItem(item)">
      <h2 id="headingOne" class="accordion-header">
        <button :class="[{ collapsed: !item.show }]" :aria-expanded="item.show" :aria-controls="item.title" class="accordion-button" type="button">
          {{ item.title }}
        </button>
      </h2>

      <div v-if="item.show" :id="'collapseOne'" :class="{ show: item.show }" :aria-labelledby="item.title" class="accordion-collapse collapse">
        <div class="accordion-body">
          {{ item.content }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseAccordion',
  props: {
    items: {
      type: Array
    },
    flushed: {
      type: Boolean
    }
    // headerClasses: {
    //   type: String
    // }
  },
  emits: {
    click: () => true
  },
  data: () => ({
    computedItems: []
  }),
  beforeMount () {
    this.computedItems = this.items.map((item) => {
      item.show = false
      return item
    })
  },
  methods: {
    expandItem (item) {
      // this.computedItems.forEach((item) => {
      //   item.show = false
      // })
      item.show = !item.show
      this.$emit('click', item)
    }
  }
}
</script>
