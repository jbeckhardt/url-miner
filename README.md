# url-miner
Programmatically creates urls based on a pre-defined protocol of word elements. It then determines whether or not the URL is available for purchase and logs the status to an output file. 

# Details
Ever needed a domain, only to find that every. single. dot. com. has been purchased by some legion of unknown, rich and chortling dickheads? After lamenting that you're 15 years late to the domain-buying party, you can turn to the URl Miner. The Miner programmatically creates URLs based on a predefined protocol and then checks the URL's availability, logging the status to an output file.

## Protocol
At the top of the file, you can declare a 'protocol' which will define how a string is created. Strings can be created with a number of english language word parts. They are listed below along with their protocol abbreviation. 
 * consonant (c) 
 * vowel (v)
 * word (w)
 * stem (st)
 * syllable (sy) 
 * prefix (pr) 
 * suffix (su)
 * phoneme (ph) (A phoneme is a sound - similar to a syllable except it includes things like 'ch' and 'th')
 * phoneme consonant (phc) 
 * phoneme vowel (phv)

To define the protocol, declare each word-part as a string in a python list. For example, if you want to create strings that go 'consonant-vowel-consonant-consonsant-suffix' you would set protocol = ['c','v','c','c','su']. An example output of this protocol might be 'canting'

## Additional configurations
There are two additional variables that can be configured:
* max_domain_ength:  The maximum length of the string 
* cycles = The number of output cycles

## Output Log
The files save to a folder called 'output'. The name of the file is automatically generated to match the protocol. If the file already exists, the new output aapends to the original file. 

The output files is a csv with two fields. The first is the URL. The second is the availability of the domain. A value of 0 means the domain is unavailable. A value of 1 means the domain is available. 

## Additional Notes
The current version of this uses dictionaries and word part lists culled from the internet. Unfortunately, I did not document these at the time of discovery. We will update the documentation as we know ore.  
