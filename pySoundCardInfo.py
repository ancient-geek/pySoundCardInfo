### Python 3 Module: pySoundCardInfo

import subprocess
cards = []


### Get a list of sound cards    
def get_cards():    
    result = subprocess.run(["ls","/proc/asound"], 
                        capture_output=True, encoding="utf-8",timeout=0.1)
    if result.returncode != 0:
        return 0
    global cards
    cards = []
    for line in result.stdout.splitlines():
        if line[0:4] == "card" and line[4].isnumeric():
            index = int(line[4])
            card = {"index":index, "name":get_name(index)}
            cards.append(card)            
    return cards
    

### Get the name of a card given its index
def get_name(index):    
    result = subprocess.run(["cat","/proc/asound/card{0}/pcm0p/info".format(index)], 
                        capture_output=True, encoding="utf-8",timeout=0.1)
    if result.returncode == 0:
        info = dict(substring.split(':') for substring in result.stdout.splitlines())
        return info["name"]
    else:
        return None
    

### Get the current state of a card given its index
def get_state(index):
    global state,sample_rate_hz, number_of_channels, bits_per_sample
    result = subprocess.run(["cat","/proc/asound/card{0}/pcm0p/sub0/hw_params".format(index)], 
                        capture_output=True, encoding="utf-8",timeout=0.1)
    if result.returncode != 0:
        return None
    d = dict();            
    if(result.stdout.lower().__contains__("closed")):
        d["state"]  = "closed"
        d["sample_rate_hz"]  = None
        d["number_of_channels"]  = None
        d["bits_per_sample"]  = None            
    else:
        info = dict(substring.split(':') for substring in result.stdout.splitlines())
        d["state"] = "playing"
        d["sample_rate_hz"]  = int(info["rate"].strip().split(' ')[0])
        d["number_of_channels"]  = int(info["channels"].strip())
        d["bits_per_sample"]  = int(info["format"].strip("S ").split('_')[0])            
    return d
    

### Get the card index number from its name
def get_index_from_name(name):
    name = name.lower()
    for i in range(len(cards)):
        if cards[i]["name"].lower().find(name) >= 0:
            return cards[i]["index"]
    return None


### Test program ###
if __name__ == "__main__": 
    cards = get_cards()
    print("Audio cards   :", cards)

    card_name = "hifiberry"
    index = get_index_from_name(card_name)
    print("index of card \"{0}\" is {1}".format(card_name,index))

    state = get_state(0)
    print("Current State: ", state)
