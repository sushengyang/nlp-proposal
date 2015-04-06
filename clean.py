import json

with open("data.json") as json_file:
    json_data = json.load(json_file)
        
    text_file = open("Output.txt", "w")

    for dict_number in range(len(json_data)-1):
    	
    	reviews = json_data[dict_number]['reviews']
    	
    	for index in range(len(reviews)-1):
			review = reviews[index].encode("utf-8")
			text_file.write(review+"\n")

    text_file.close()