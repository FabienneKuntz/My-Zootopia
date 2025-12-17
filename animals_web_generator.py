import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def filter_animals_data(animals_data):
    """Filters the animals_data only for specific given keys"""
    for animal in animals_data:
        location_list = animal.get("locations")
        if "name" in animal:
            print(f'Name: {animal["name"]}')
        if "diet" in animal["characteristics"]:
            print(f'Diet: {animal["characteristics"]["diet"]}')
        if location_list:
            print(f'Location: {location_list[0]}')
        if "type" in animal["characteristics"]:
            print(f'Type: {animal["characteristics"]["type"]}')
        print()


def main():
    animals_data = load_data('animals_data.json')
    filter_animals_data(animals_data)

if __name__ == "__main__":
    main()
