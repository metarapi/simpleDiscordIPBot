from getIP import get_public_ip

def get_response(user_input: str) -> str:
    lowered = user_input.lower()

    if lowered == '!ip':
        return f"Public IP: {get_public_ip()}\nCoD4: {get_public_ip()}:28960\nValheim: {get_public_ip()}:2456\nMinecraft: {get_public_ip()}:25565\nFoundry VTT: http://{get_public_ip()}:30000/\n Enshrouded:{get_public_ip()}:15637"
    elif lowered == '!foundry':
        return 'Foundry VTT: http://'+ get_public_ip() +':30000/'
    elif lowered == '!valheim':
        return 'Valheim: '+ get_public_ip() +':2456'
    elif lowered == '!enshrouded':
        return 'Enshrouded: '+ get_public_ip() +':15637'

# Test  
# print(get_response('!ip'))