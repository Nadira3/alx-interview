#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Define the URL for the Star Wars API, using the movieId to get the film data
const url = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to the API
request(url, function (error, response, body) {
  // Handle errors (e.g., if the movieId is invalid or if the API is down)
  if (error) {
    console.log('Error:', error);
    return;
  }

  // If the response status code is not 200, it means something went wrong
  if (response.statusCode !== 200) {
    console.log('Failed to fetch data. Status code:', response.statusCode);
    return;
  }

  // Parse the JSON response body
  const filmData = JSON.parse(body);

  // Iterate over the characters and print each one
  filmData.characters.forEach(characterUrl => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.log('Error:', error);
        return;
      }
      
      if (response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      }
    });
  });
});
