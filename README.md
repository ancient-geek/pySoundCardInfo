# pySoundCardInfo
Very basic python module to get a list of available cards and the current sample rate, bits and channels of a given card.
Tested on a Raspberry Pi with two sound cards

Usage:

## get_cards()
Creates a list of the available sound cards

## get_name(index)
Returns the name of a sound card given its index number

## get_state(index)
Returns a dictionary containing:
state:  "closed" or "playing"
sample_rate_hz :
number_of_channels :
bits_per_sample :

## get_index_from_name(name)
Returns the index of a card if it can find the name in the cards' name as provided by the OS
Needs get_cards() to have been run first
