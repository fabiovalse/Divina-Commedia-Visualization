<template>
  <div class="cantos" v-if="selection !== undefined">
    <div class="tercet" v-for="(tercet, i) in selection.children">
      <div class="line"
           v-for="line in tercet.children"
           v-html="text_search !== undefined ? get_highlighted(text_search, line.text) : line.text">
      </div>
      <div class="number" v-if="tercet.children.length == 3">{{3*(i+1)}}</div>
    </div>
  </div>
</template>

<script lang="coffee">
export default {
  
  computed:
    selection: () -> @$store.state.path
    text_search: () -> @$store.state.text_search

  methods: 
    get_highlighted: (text_search, text) ->
      re = new RegExp text_search, 'gi'
      return text.replace(re, "<span class='highlighted'>#{text_search}</span>")

}
</script>

<style scoped>
.cantos {
  padding-top: 40px;
  background: var(--main-background-color);
}
.cantos .tercet {
  position: relative;
  width: 350px;
  margin: auto;
  margin-bottom: 20px;
}
.cantos .tercet .number {
  position: absolute;
  right: -15px;
  bottom: 0px;
  color: gray;
  font-size: 13px;
}
</style>
<style>
.cantos .tercet .line .highlighted {
  color: var(--selection-color);
}
</style>