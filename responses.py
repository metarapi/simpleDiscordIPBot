from getIP import get_public_ip

def get_response(user_input: str) -> str:
    lowered = user_input.lower()

    if lowered == '!ip':
        return 'Public IP: ' + get_public_ip()
    elif lowered == '!foundry':
        return 'Foundry VTT: http://'+ get_public_ip() +':30000/'
    elif lowered == '!valheim':
        return 'Valheim: '+ get_public_ip() +':2456'

# Test  
# print(get_response('!ip'))