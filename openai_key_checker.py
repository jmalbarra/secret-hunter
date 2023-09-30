import requests

api_key_list = []
with open('secrets.txt', 'r') as file:
    api_key = file.readline()[:-1]
    while api_key:
        if len(api_key)>45:
            api_key_list.append(api_key)
        api_key = file.readline()[:-1]

print("Tenia para probar: ",len(api_key_list))

unique_secrets_list = list(set(api_key_list))

print("Voy a probar: ",len(unique_secrets_list))

with open('invalid_secrets.txt','a') as invalid_file:
    with open('valid_secrets.txt','a') as result_file:
        for api_key in api_key_list:
            # Define your API key and endpoint
            url = 'https://api.openai.com/v1/chat/completions'

            # Set up the request headers
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            }

            # Define your conversation
            conversation = [
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': 'Who won the world series in 2020?'}
            ]

            # Define a new message from the user
            new_message = {'role': 'user', 'content': 'Where was it played?'}

            # Extend the conversation with the new message
            conversation.append(new_message)

            # Make the API request
            response = requests.post(url, headers=headers, json={'messages': conversation})

            # Get the response from the API
            data = response.json()
            if response.status_code == 200 or response.status_code == 429:
                line = api_key + "," + str(response.status_code)
                result_file.writelines("%s\n" % line)
                print(f"OK!!!: {response.status_code} - {response.text}")    
            else:
                line = api_key + "," + str(response.status_code)
                invalid_file.writelines("%s\n" % line)
                print(f"Error: {response.status_code} - {response.text}")
                    
        else:
            print("Descartado por corto: ",api_key)
                
        api_key = file.readline()[:-1]



