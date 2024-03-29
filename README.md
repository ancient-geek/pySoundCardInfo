# pySoundCardInfo
Very basic python module to get a list of audio cards detected by Alsa and the current state, sample rate, bits per sample and channels of a given card.
Tested on a Raspberry Pi with two sound cards

Usage:

## get_cards()
Creates a list of the available sound cards

## get_name(index)
Returns the name of a sound card given its index number

## get_state(index)
Returns a dictionary containing:

- state:  "closed" or "playing"
- sample_rate_hz :
- number_of_channels :
- bits_per_sample :

## get_index_from_name(name)
Returns the index of a card if it can find "name" in the cards' name as provided by Alsa.

Note: Needs get_cards() to have been run first


Running the file whilst playing a file using Roon yields:

```
Audio cards   : [{'index': 0, 'name': ' USB Audio'}, {'index': 1, 'name': ' HifiBerry Digi HiFi wm8804-spdif-0'}]
index of card "hifiberry" is 1
Current State:  {'state': 'playing', 'sample_rate_hz': 192000, 'number_of_channels': 2, 'bits_per_sample': 24}
```
