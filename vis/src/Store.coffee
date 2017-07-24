export default {
  state:
    path: undefined
    text_search: undefined
  
  mutations:
    set_path: (state, path) ->
      state.path = path

    set_text_search: (state, text_search) ->
      state.text_search = text_search
}