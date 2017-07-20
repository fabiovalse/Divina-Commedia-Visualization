import Vue from 'vue'
import App from './App.vue'

width = document.querySelector('body').getBoundingClientRect().width
height = document.querySelector('body').getBoundingClientRect().height

app = new Vue
  el: '#app'
  template: """
    <app :width='#{width}' :height='#{height}'></app>
  """
  components:
    'app': App
