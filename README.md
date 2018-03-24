# Burst Vanity Address Generator

## What is it?
Have you ever wished you could have a truly great and memorable Burst Address? Now you can, with the **Burst Vanity Address Generator**. Generate custom Burst addresses using the 4 leading characters of the address after "BURST".

## Requirements
1. python3 installed
2. pip installed

## How to
1. Open a new terminal
2. Install pyburstlib with the following command `pip install pyburstlib`
3. Enter the following command `python burst-vanity-generator.py -m <YOUR DESIRED NAME>`

example: `python burst-vanity-generator.py -m USA`
eventually returns `BURST-USAB-U7JP-V2ZH-5PKKP`

## How it Works
The **Burst Vanity Address Generator** is basically a brute force address generator, it will generate 1000's of addresses from random strings until it finds one that matches your input. Then it will write the passphrase for the address to a txt file that you can use to sign into the Burst Wallet. Depending on the number of cores in your computer this can take some time.

### Time to Compute
| Characters | Est. Time |
| --- | --- |
| 1 | less than 1 second |
| 2 | 1-5 seconds |
| 3 | 10-30 seconds |
| 4 | more than a minute |

### Donate
- Andrew Scott (drownedcoast) - BURST-Q944–2MY3–97ZZ-FBWGB
<img align="right" width="298" height="120" title="Powered By Burst" src="https://raw.githubusercontent.com/PoC-Consortium/Marketing_Resources/master/Powered_By_Burst/PBB4.png"/>
