lunr = require('lunr')
data = require('../data/divina_commedia.json')
fs = require('fs')

documents = []

make_id = (node) -> 
  #node.parent.parent.parent.name + ", " + node.parent.parent.name + ", Verso " + node.number
  "#{node.parent.parent.parent.parent.children.indexOf(node.parent.parent.parent)} #{node.parent.parent.parent.children.indexOf(node.parent.parent)} #{node.parent.parent.children.indexOf(node.parent)} #{node.parent.children.indexOf(node)}"

visit_tree = (node, parent) ->
  node.parent = parent

  if node.children?
    for child in node.children
      visit_tree child, node
  else
    documents.push {
      "id": make_id(node)
      "text": node.text
    }

visit_tree data, null

idx = lunr(() ->
  this.ref('id')
  this.field('text')
  this.metadataWhitelist = ['position']

  documents.forEach ((doc) ->
    this.add(doc)
  ), this
)

fs.writeFile "./index", JSON.stringify(idx), (err) ->
    if err
      console.log err

    console.log 'Index correctly created!'

# results = idx.search("ugolino")
# results.forEach (r) ->
#   console.log r
#   console.log r.matchData.metadata.ugolino.text.position