# GSOC_Organizations_Scraper!_task 3
 A scraper that would return the details of the organizations in a JSON format.
 
 Files to look for:- 
 src/lib.rs - Communicates with the server and makes a request, written in rust
 pyscraper/code.py - scrapes through the requested file, and saves into JSON format
 details.json - example information scraped from the website provided
 Cargo.toml - holds dependencies for rust program
 
//rest of the files can be ignored//

Exxplaining:

the main program  pyscraper/code.py uses calls the Rust function to make a request to the server. 
the reason Rust is used is to utilise the its safety features, which i believe is essential in tasks like server requests. Error cases are all handled at write time with so much ease. (The whole code could have been written easily in python itself... but mere ko brownie khaana hai)

code.py then takes this requested file, parses it, creates an empty dictionary with suitable keys, and parses through the file, filling up the dicitonary. it then saves the file in JSON format.
Python is used to mainly parse and write into a JSON file, because of the ease in writing and parsing.
