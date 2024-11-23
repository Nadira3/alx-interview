# 0. Star Wars API Project

This project involves writing a script that fetches and displays Star Wars characters from a specific movie using the Star Wars API. The script retrieves the character list for a movie based on its movie ID, which is passed as a command-line argument.

## Key Concepts

To successfully complete this project, you should be familiar with the following concepts:

1. **HTTP Requests in JavaScript**:
   - Making HTTP requests using the `request` module or alternatives such as `fetch` in Node.js.
   - Interacting with external services to fetch data.

2. **Working with APIs**:
   - Understanding RESTful APIs and how to interact with them.
   - Parsing JSON data returned by APIs.

3. **Asynchronous Programming**:
   - Managing asynchronous operations with callbacks, promises, and async/await syntax.
   - Ensuring the API response is handled asynchronously.

4. **Command Line Arguments**:
   - Using `process.argv` to access command-line arguments passed to a Node.js script.

5. **Array Manipulation and Iteration**:
   - Iterating over arrays and manipulating data to display it in the required format.

## Requirements

### General
- Allowed editors: vi, vim, emacs
- Your files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 10.14.x).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/node`.
- A `README.md` file at the root of the folder is mandatory.
- Your code should be semistandard compliant (Rules of Standard + semicolons on top).
- All your files must be executable.
- The length of your files will be tested using `wc`.

### Additional Instructions
- You are required to use the `request` module to interact with the Star Wars API.
- The script should print each character's name in the same order as they appear in the "characters" list from the `/films/` endpoint.

## How to Run

1. **Install Node.js**:
   If Node.js is not already installed, use the following commands to install it:
   ```bash
   $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   $ sudo apt-get install -y nodejs

2. Install Dependencies: Install the request module globally:

$ sudo npm install request --global


3. Run the Script: You can run the script as follows:
```
$ ./0-starwars_characters.js <movie_id>
```
Replace <movie_id> with the ID of the Star Wars movie (e.g., 3 for "Return of the Jedi").


### Example Usage

For example, to get the characters from "Return of the Jedi" (Movie ID 3):
```
$ ./0-starwars_characters.js 3
```
Expected Output
```
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```
### Notes

The script interacts with the Star Wars API to fetch character data based on the provided movie ID.

The names of the characters are printed in the order they are listed in the API response for the specified movie.

## Troubleshooting

If you encounter issues running the script, here are some common problems and solutions:

1. **Error: 'request' module not found**:
   - Make sure you have installed the `request` module globally using:
     ```bash
     $ sudo npm install request --global
     ```

2. **Command not found**:
   - Ensure the script has execute permission. If not, you can add execute permissions with:
     ```bash
     $ chmod +x 0-starwars_characters.js
     ```

3. **Error: Invalid Movie ID**:
   - The movie ID you provide should be a valid ID according to the Star Wars API. You can check the available movies and their IDs by accessing the `/films/` endpoint of the Star Wars API.

4. **API Response Delay**:
   - If the API is slow or not responding, it might be due to network issues or the API service being temporarily unavailable. Retry after a while.

## Project Resources

- **Star Wars API**: [https://swapi.dev/](https://swapi.dev/)
- **Request Module Documentation**: [https://www.npmjs.com/package/request](https://www.npmjs.com/package/request)
- **Node.js Documentation**: [https://nodejs.org/en/docs/](https://nodejs.org/en/docs/)
- **Asynchronous Programming in JavaScript**: [https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)

## Conclusion

By completing this project, you will have demonstrated your ability to interact with external APIs, process JSON data, and manage asynchronous operations in JavaScript. You will also have learned how to handle command-line arguments and iterate over data structures to present information in a user-friendly format.




