import Vue from 'vue'
import App from './App.vue'
import Poem from './Poem.vue'
import Cantos from './Cantos.vue'
import Store from './Store.coffee'

import VueRouter from 'vue-router'
Vue.use(VueRouter)

import Vuex from 'vuex'
Vue.use(Vuex)

router = new VueRouter({
  routes: [
    {
      name: 'main'
      path: '/'
      component: Poem
      props: true
    }
    {
      name: 'goto_text'
      path: '/:book/:cantos' #path: '/:book/:cantos/:tercet/:verse'
      component: Cantos
    }
  ]
})

store = new Vuex.Store(Store)

app = new Vue
  el: '#app'
  store: store
  template: """
    <app></app>
  """
  router: router
  components:
    'app': App
