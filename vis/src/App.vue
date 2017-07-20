<template>
  <div class="app">
    <div class="topbar">
      <input
        placeholder="Search"
        class="search"
        type="text"
        @keyup="search()"
      />
    </div>
    <svg>
      <g class="main" :transform="'translate(' + margin + ', ' + margin + ')'">
        <g class="zoomable_layer">

          <g class="part" 
             v-for="(part, i) in poem.children"
             v-if="in_viewport(i*part_w, 0, part_w)"
             :transform="'translate(' + i*part_w + ', 0)'">
            <text class="part_title"
                  :x="w/6"
                  y="20">
              {{part.name.toUpperCase()}}
            </text>

            <g v-for="(cantos, j) in part.children"
               v-if="in_viewport((i*w/3) + (j*(w/3-10)/part.children.length), 65, (w/3-10)/part.children.length)"
               :transform="'translate(' + j*(w/3-10)/part.children.length + ', 65)'">
              <text class="cantos_title"
                    x="5"
                    y="5"
                    transform="rotate(-90)">
                {{cantos.name.split(' ')[1]}}
              </text>

              <g v-for="(tercet, k) in cantos.children"
                 :transform="'translate(-1, ' + k*12 + ')'">

                <g v-for="(line, y) in tercet.children"
                 :transform="'translate(0, ' + y*3 + ')'">
                  <line x1="0" y1="0" :x2="line.text_length/6" y2="0" @click="print(line)" :class="{selected: selected(target,line.text)}" :title="line.text"></line>
                </g>
              </g>
            </g>
          </g>
        </g>
      </g>
    </svg>
  </div>
</template>

<script lang="coffee">
import data from '../data/divina_commedia.json'
import * as d3 from 'd3'

export default {
  props: ['width', 'height']

  data: () ->
    poem: data
    x: 0
    y: 0
    margin: 10
    target: undefined

  computed:
    w: () -> @width - @margin * 2
    h: () -> @height - @margin * 2
    dx: () -> @w
    dy: () -> @h
    part_w: () -> @w/3

  mounted: () ->
    @$el.querySelector('.main').style.setProperty '--width', "#{@w}px"
    @$el.querySelector('.main').style.setProperty '--height', "#{@h}px"

  methods:
    in_viewport: (x, y, dx) -> x+dx >= @x and x <= @x+@dx

    search: () ->
      value = d3.select('input.search').node().value
      @target = if value isnt '' then value else undefined

    selected: (target, text) -> target? and text.toLowerCase().indexOf(target.toLowerCase()) >= 0

    print: (d) ->
      console.log d.text
      console.log d.text_length

}
</script>

<style>
:root {
  --main-text-color: #432621;
  --sec-text-color: rgba(0,0,0,0.54);
  --selection-color: #f75638;
}

html, body {
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
  font-family: 'Roboto Slab', serif;
}

.app {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
.app .topbar {
  width: 100%;
  height: 50px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.2), 0 -1px 0px rgba(0,0,0,0.02);
  z-index: 1;
}
.app svg {
  width: 100%;
  flex-grow: 1;
  padding-top: 5px;
  background: #fbf9e8;
}
.app svg .main {
  width: calc(var(--width) - var(--margin) * 2);
  height: calc(var(--height) - var(--margin) * 2);
}

.title {
  font-size: 18px;
}
.title, .subtitle {
  fill: var(--main-text-color);
}
.subtitle {
  fill: var(--sec-text-color);
  font-size: 14px;
}

.part {
  width: calc(var(--width) / 3);
}
.part_title {
  fill: var(--main-text-color);
  font-size: 14px;
  text-anchor: middle;
  cursor: pointer;
}
.part_title:hover {
  fill: var(--selection-color);
}

.cantos_title {
  fill: var(--main-text-color);
  font-size: 10px;
}

line {
  stroke: #432621;
  stroke-width: 1;
  shape-rendering: crispEdges;
}
line:hover {
  stroke: var(--selection-color);
  stroke-width: 3;
}

.selected {
  stroke: var(--selection-color);
  stroke-width: 3;
}

.search {
  border: none;
  outline: none;
  width: 250px;
  border-bottom: 1px solid #BBB;
  padding: 5px;
  margin: 10px;
  font-size: 15px;
  font-family: 'Roboto Slab', serif;
}

/*.viewport {
  width: calc(var(--width) - 10px);
  height: calc(var(--height) - 10px);
  stroke: blue;
  fill: transparent;
  stroke-width: 3px;
}*/

</style>