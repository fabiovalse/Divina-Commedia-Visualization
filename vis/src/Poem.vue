<template>
  <svg class="poem">
    <g class="main" :transform="'translate(' + margin + ', ' + margin + ')'">
      <g class="zoomable_layer">

        <g class="part" 
           v-for="(part, i) in poem.children"
           :transform="'translate(' + (i*part_w+5) + ', 0)'">
          <text class="part_title"
                :x="w/6"
                y="20">
            {{part.name.toUpperCase()}}
          </text>

          <g v-for="(cantos, j) in part.children"
             :transform="'translate(' + j*(w/3-10)/part.children.length + ', 60)'">
            <text class="cantos_title"
                  x="5"
                  y="6"
                  transform="rotate(-90)">
              {{cantos.name.split(' ')[1]}}
            </text>

            <g v-for="(tercet, k) in cantos.children"
               :transform="'translate(-1, ' + k*12 + ')'">

              <g v-for="(line, y) in tercet.children"
               :transform="'translate(0, ' + y*3 + ')'">
                <line :class="{selected: selected(line.text)}"
                      :title="line.text"
                      x1="0"
                      y1="0"
                      :x2="line.text_length/6"
                      y2="0"
                      @click="goto(part.name, cantos)">
                </line>
              </g>
            </g>
          </g>
        </g>
      </g>
    </g>
  </svg>
</template>

<script lang="coffee">
import data from '../data/divina_commedia.json'

export default {

  data: () ->
    poem: data
    x: 0
    y: 0
    margin: 10
    width: document.querySelector('body').getBoundingClientRect().width
    height: document.querySelector('body').getBoundingClientRect().height

  computed:
    w: () -> @width - @margin * 2
    h: () -> @height - @margin * 2
    dx: () -> @w
    dy: () -> @h
    part_w: () -> @w/3
    target: () -> @$store.state.text_search

  mounted: () ->
    @$el.querySelector('.main').style.setProperty '--width', "#{@w}px"
    @$el.querySelector('.main').style.setProperty '--height', "#{@h}px"

  methods:
    selected: (text) -> @target? and text.toLowerCase().indexOf(@target.toLowerCase()) >= 0

    goto: (book, cantos) ->
      @$store.commit 'set_path', cantos
      @$router.push
        name: 'goto_text',
        params:
          book: book
          cantos: cantos.name.replace(' ','')

}
</script>

<style scoped>
.poem {
  width: 100%;
  height: 100%;
  background: var(--main-background-color);
}
.poem .main {
  width: calc(var(--width) - var(--margin) * 2);
  height: calc(var(--height) - var(--margin) * 2);
}

.poem .part {
  width: calc(var(--width) / 3);
}
.poem .part_title {
  fill: var(--text-color-3);
  font-size: 14px;
  text-anchor: middle;
  cursor: pointer;
}

.poem .cantos_title {
  fill: var(--text-color-2);
  font-size: 10px;
}

.poem line {
  stroke: var(--text-color-1);
  stroke-width: 2;
  shape-rendering: crispEdges;
}
.poem line:hover {
  stroke: var(--selection-color);
  stroke-width: 3;
}

.poem .selected {
  stroke: var(--selection-color);
  stroke-width: 3;
}
</style>