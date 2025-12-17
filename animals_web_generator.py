import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def read_html_data():
    with open("animals_template.html", "r",) as file:
        html_template = file.read()
        return html_template


def filter_animals_data(animals_data):
    """Filters the animals_data only for specific given keys"""
    output = ""
    for animal in animals_data:
        location_list = animal.get("locations")
        if "name" in animal:
            output += f'Name: {animal["name"]}\n'
        if "diet" in animal["characteristics"]:
            output += f'Diet: {animal["characteristics"]["diet"]}\n'
        if location_list:
            output += f'Location: {location_list[0]}\n'
        if "type" in animal["characteristics"]:
            output += f'Type: {animal["characteristics"]["type"]}\n'

    return output

def replace_info(animals_data):
    html_template = read_html_data()
    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", filter_animals_data(animals_data))
    return new_html

def write_new_html_file(animals_data):
    new_html = replace_info(animals_data)
    with open("animals.html", "w") as file:
        file.write(new_html)

def main():
    animals_data = load_data('animals_data.json')
    print(filter_animals_data(animals_data))
    print(replace_info(animals_data))
    write_new_html_file(animals_data)


if __name__ == "__main__":
    main()
