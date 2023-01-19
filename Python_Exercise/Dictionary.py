paragon = {
    "name_one": "john doe",
    "name_two": "peter dury",
    "name_three": "lee_min_hoo",
    "name_four": "asake",
    "name_five": "fela",
    "name_six": "kuti"

}
paragon["name_one"] = "felix"
print(paragon["name_one"]) 
paragon["name_seven"] = "james"
name = paragon.get("name_one")
