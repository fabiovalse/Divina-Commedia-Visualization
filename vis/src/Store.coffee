export default {
  state:
    path: undefined
    tercet: undefined
    text_search: undefined
  
  mutations:
    set_path: (state, path) ->
      state.path = path

    set_tercet: (state, tercet) ->
      state.tercet = tercet

    set_text_search: (state, text_search) ->
      state.text_search = text_search
}