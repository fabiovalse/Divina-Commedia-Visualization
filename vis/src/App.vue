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
  --main-text-color: #432621;
  --main-background-color: #fbf9e8;
  --sec-text-color: rgba(0,0,0,0.54);
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
}

.app .topbar {
  width: 100%;
  height: var(--topbar-height);
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
}
</style>