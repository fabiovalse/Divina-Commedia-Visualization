import Vue from 'vue'
import App from './App.vue'
import Poem from './Poem.vue'
import Cantos from './Cantos.vue'
import Store from './Store.coffee'

import Vuex from 'vuex'
Vue.use(Vuex)

import VueRouter from 'vue-router'
Vue.use(VueRouter)

store = new Vuex.Store(Store)

router = new VueRouter({
  base: '/dist/'
  mode: 'history'
  scrollBehavior: (to, from, savedPosition) ->
    if to.name isnt 'main'
      offset = 0

      if store.state.tercet.number > 1
        offset = document.querySelectorAll('.tercet')[store.state.tercet.number-1].getBoundingClientRect().top-63

      return {x: 0, y: offset}
    else
      return {x: 0, y: 0}
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

app = new Vue
  el: '#app'
  store: store
  template: """
    <app></app>
  """
  router: router
  components:
    'app': App
