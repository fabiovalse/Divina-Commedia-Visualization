import urllib

# The url name of every canto has been extracted from the wikisource page of the Divina Commedia
# (https://it.wikisource.org/w/api.php?action=query&titles=Divina_Commedia&prop=revisions&rvprop=content&format=json)
canti = ["Inferno/Canto I", "Inferno/Canto II", "Inferno/Canto III", "Inferno/Canto IV", "Inferno/Canto V", "Inferno/Canto VI", "Inferno/Canto VII", "Inferno/Canto VIII", "Inferno/Canto IX", "Inferno/Canto X", "Inferno/Canto XI", "Inferno/Canto XII", "Inferno/Canto XIII", "Inferno/Canto XIV", "Inferno/Canto XV", "Inferno/Canto XVI", "Inferno/Canto XVII", "Inferno/Canto XVIII", "Inferno/Canto XIX", "Inferno/Canto XX", "Inferno/Canto XXI", "Inferno/Canto XXII", "Inferno/Canto XXIII", "Inferno/Canto XXIV", "Inferno/Canto XXV", "Inferno/Canto XXVI", "Inferno/Canto XXVII", "Inferno/Canto XXVIII", "Inferno/Canto XXIX", "Inferno/Canto XXX", "Inferno/Canto XXXI", "Inferno/Canto XXXII", "Inferno/Canto XXXIII", "Inferno/Canto XXXIV", "Purgatorio/Canto I", "Purgatorio/Canto II", "Purgatorio/Canto III", "Purgatorio/Canto IV", "Purgatorio/Canto V", "Purgatorio/Canto VI", "Purgatorio/Canto VII", "Purgatorio/Canto VIII", "Purgatorio/Canto IX", "Purgatorio/Canto X", "Purgatorio/Canto XI", "Purgatorio/Canto XII", "Purgatorio/Canto XIII", "Purgatorio/Canto XIV", "Purgatorio/Canto XV", "Purgatorio/Canto XVI", "Purgatorio/Canto XVII", "Purgatorio/Canto XVIII", "Purgatorio/Canto XIX", "Purgatorio/Canto XX", "Purgatorio/Canto XXI", "Purgatorio/Canto XXII", "Purgatorio/Canto XXIII", "Purgatorio/Canto XXIV", "Purgatorio/Canto XXV", "Purgatorio/Canto XXVI", "Purgatorio/Canto XXVII", "Purgatorio/Canto XXVIII", "Purgatorio/Canto XXIX", "Purgatorio/Canto XXX", "Purgatorio/Canto XXXI", "Purgatorio/Canto XXXII", "Purgatorio/Canto XXXIII", "Paradiso/Canto I", "Paradiso/Canto II", "Paradiso/Canto III", "Paradiso/Canto IV", "Paradiso/Canto V", "Paradiso/Canto VI", "Paradiso/Canto VII", "Paradiso/Canto VIII", "Paradiso/Canto IX", "Paradiso/Canto X", "Paradiso/Canto XI", "Paradiso/Canto XII", "Paradiso/Canto XIII", "Paradiso/Canto XIV", "Paradiso/Canto XV", "Paradiso/Canto XVI", "Paradiso/Canto XVII", "Paradiso/Canto XVIII", "Paradiso/Canto XIX", "Paradiso/Canto XX", "Paradiso/Canto XXI", "Paradiso/Canto XXII", "Paradiso/Canto XXIII", "Paradiso/Canto XXIV", "Paradiso/Canto XXV", "Paradiso/Canto XXVI", "Paradiso/Canto XXVII", "Paradiso/Canto XXVIII", "Paradiso/Canto XXIX", "Paradiso/Canto XXX", "Paradiso/Canto XXXI", "Paradiso/Canto XXXII", "Paradiso/Canto XXXIII"]

for canto in canti:
  # Log
  print canto

  url = "https://it.wikisource.org/w/api.php?action=query&titles=Divina_Commedia/" + canto + "&prop=revisions&rvprop=content&format=json"
  file_name = canto.replace('/', "_").replace(" ", "_")

  with open("wikisource_data/"+file_name, 'w') as f:
    response = urllib.urlopen(url)

    f.write(response.read())
