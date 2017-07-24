import App from './App.vue'
import Cantos from './Cantos.vue'

export default {
  routes: [
    {
      name: 'goto_text'
      path: '/:book' #path: '/:book/:cantos/:tercet/:verse'
      component: Cantos
    }
  ]
}
