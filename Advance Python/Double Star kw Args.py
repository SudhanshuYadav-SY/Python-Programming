def Sample(name,experience,location):
    print(name,experience,location)


d = {"name":"Sudhanshu","experience": "2 year 5 months","location":"New Delhi"}

Sample(**d)