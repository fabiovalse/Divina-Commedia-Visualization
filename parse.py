import json
import re

volume_index = {
  "Inferno": 0,
  "Purgatorio": 1,
  "Paradiso": 2
}

book = {
  "name": "Divina Commedia",
  "author": "Dante Alighieri",
  "children": [
    {
      "name": "Inferno",
      "type": "Volume",
      "children": []
    },
    {
      "name": "Purgatorio",
      "type": "Volume",
      "children": []
    },
    {
      "name": "Paradiso",
      "type": "Volume",
      "children": []
    }
  ]
}

canti = ["Inferno/Canto I", "Inferno/Canto II", "Inferno/Canto III", "Inferno/Canto IV", "Inferno/Canto V", "Inferno/Canto VI", "Inferno/Canto VII", "Inferno/Canto VIII", "Inferno/Canto IX", "Inferno/Canto X", "Inferno/Canto XI", "Inferno/Canto XII", "Inferno/Canto XIII", "Inferno/Canto XIV", "Inferno/Canto XV", "Inferno/Canto XVI", "Inferno/Canto XVII", "Inferno/Canto XVIII", "Inferno/Canto XIX", "Inferno/Canto XX", "Inferno/Canto XXI", "Inferno/Canto XXII", "Inferno/Canto XXIII", "Inferno/Canto XXIV", "Inferno/Canto XXV", "Inferno/Canto XXVI", "Inferno/Canto XXVII", "Inferno/Canto XXVIII", "Inferno/Canto XXIX", "Inferno/Canto XXX", "Inferno/Canto XXXI", "Inferno/Canto XXXII", "Inferno/Canto XXXIII", "Inferno/Canto XXXIV", "Purgatorio/Canto I", "Purgatorio/Canto II", "Purgatorio/Canto III", "Purgatorio/Canto IV", "Purgatorio/Canto V", "Purgatorio/Canto VI", "Purgatorio/Canto VII", "Purgatorio/Canto VIII", "Purgatorio/Canto IX", "Purgatorio/Canto X", "Purgatorio/Canto XI", "Purgatorio/Canto XII", "Purgatorio/Canto XIII", "Purgatorio/Canto XIV", "Purgatorio/Canto XV", "Purgatorio/Canto XVI", "Purgatorio/Canto XVII", "Purgatorio/Canto XVIII", "Purgatorio/Canto XIX", "Purgatorio/Canto XX", "Purgatorio/Canto XXI", "Purgatorio/Canto XXII", "Purgatorio/Canto XXIII", "Purgatorio/Canto XXIV", "Purgatorio/Canto XXV", "Purgatorio/Canto XXVI", "Purgatorio/Canto XXVII", "Purgatorio/Canto XXVIII", "Purgatorio/Canto XXIX", "Purgatorio/Canto XXX", "Purgatorio/Canto XXXI", "Purgatorio/Canto XXXII", "Purgatorio/Canto XXXIII", "Paradiso/Canto I", "Paradiso/Canto II", "Paradiso/Canto III", "Paradiso/Canto IV", "Paradiso/Canto V", "Paradiso/Canto VI", "Paradiso/Canto VII", "Paradiso/Canto VIII", "Paradiso/Canto IX", "Paradiso/Canto X", "Paradiso/Canto XI", "Paradiso/Canto XII", "Paradiso/Canto XIII", "Paradiso/Canto XIV", "Paradiso/Canto XV", "Paradiso/Canto XVI", "Paradiso/Canto XVII", "Paradiso/Canto XVIII", "Paradiso/Canto XIX", "Paradiso/Canto XX", "Paradiso/Canto XXI", "Paradiso/Canto XXII", "Paradiso/Canto XXIII", "Paradiso/Canto XXIV", "Paradiso/Canto XXV", "Paradiso/Canto XXVI", "Paradiso/Canto XXVII", "Paradiso/Canto XXVIII", "Paradiso/Canto XXIX", "Paradiso/Canto XXX", "Paradiso/Canto XXXI", "Paradiso/Canto XXXII", "Paradiso/Canto XXXIII"]

### Cleans text removing special wikitext markup
###
def clean(text):
  # Remove row numbers
  text = re.sub('{{R\|[0-9]*}}', '', text)
  
  # Remove annotations
  result = re.search('{{[^\|}]*\|[^\|}]*\|([^\|}]*)}}', text)
  
  if result != None:
    text = re.sub('{{[^\|}]*\|[^\|}]*\|([^\|}]*)}}', result.group(1), text)
  
  # Remove broken annotations
  text = re.sub('{{[^\|}]*\|[^\|}]*\|', '', text)

  # Remove markup
  text = re.sub('{{[^\|}]*\|[^\|}]*}}', '', text)

  return text

### Parsing input files
###
for canto in canti:
  file_name = canto.replace('/', "_").replace(" ", "_")

  with open('wikisource_data/'+file_name, 'r') as f:
    json_data = json.loads(f.read())
    page = json_data['query']['pages'].keys()[0]

    # Filter useless text
    text = re.split('<poem>|</poem>', json_data['query']['pages'][page]['revisions'][0]['*'])[1]

    canto_data = {
      "name": canto.split('/')[1],
      "type": "Canto",
      "children": []
    }

    # Split text into terzine
    for (i, terzina) in enumerate(text.split('\n\n')):

      terzina_data = {
        "type": "Terzina",
        "number": i+1,
        "children": []
      }
      canto_data['children'].append(terzina_data)

      terzina_cleaned = [verso for verso in terzina.split('\n') if len(verso) > 1]

      for (j, verso) in enumerate(terzina_cleaned):
        if verso == " " or verso == "":
          continue

        terzina_data['children'].append({
          "type": "Verso",
          "number": 3*i + j+1,
          "text": clean(verso),
          "text_length": len(verso)
        })

    volume = volume_index[canto.split('/')[0]]
    
    book['children'][volume]['children'].append(canto_data)

### Writing output file
###
with open('divina_commedia.json', 'w') as f:
  f.write(json.dumps(book))
