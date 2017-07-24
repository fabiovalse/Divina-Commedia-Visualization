<template>
  <div class="app">
    <div class="topbar">
      <div class="title">La Divina<br>Commedia</div>
      <input
        placeholder="Search"
        class="search"
        type="text"
        @keyup="search()"
      />
    </div>
    <router-view></router-view>
  </div>
</template>

<script lang="coffee">

export default {
  computed:
    text_search: () -> @$store.stare.text_search

  methods:
    search: () ->
      value = document.querySelector('input.search').value
      @$store.commit 'set_text_search', if value isnt '' and value.length > 1 then value else undefined

    get_value: () ->
      if @text_search? then @text_search else ''

}
</script>

<style>
:root {
  --main-font-family: 'Roboto Slab', serif;
  --main-background-color: #fbf9e8;
  
  --text-color-1: #909090;
  --text-color-2: #708090;
  --text-color-3: #0d7074;
  --selection-color: #f75638;
  
  --topbar-height: 45px;
}

html, body {
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
  font-family: var(--main-font-family);
}

.app {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 800px;
  padding-top: var(--topbar-height);
}

.app .topbar {
  position: fixed;
  top: 0;
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 100%;
  height: var(--topbar-height);
  background: #FFF;
  box-shadow: 0 2px 4px rgba(0,0,0,0.2), 0 -1px 0px rgba(0,0,0,0.02);
  z-index: 1;
}
.app .topbar .search {
  border: none;
  outline: none;
  width: 250px;
  border-bottom: 1px solid #BBB;
  padding: 5px;
  margin: 5px 0px 9px 10px;
  font-family: var(--main-font-family);
  font-size: 15px;
  color: #BBB;
}

.app .topbar .title {
  font-size: 13px;
  text-transform: uppercase;
  padding: 0px 10px 0px 10px;
  line-height: 14px;
  text-align: center;
}

.app .topbar .search::-webkit-input-placeholder { /* Chrome/Opera/Safari */
  color: #BBB;
}
.app .topbar .search::-moz-placeholder { /* Firefox 19+ */
  color: #BBB;
}
.app .topbar .search:-ms-input-placeholder { /* IE 10+ */
  color: #BBB;
}
.app .topbar .search:-moz-placeholder { /* Firefox 18- */
  color: #BBB;
}
</style>