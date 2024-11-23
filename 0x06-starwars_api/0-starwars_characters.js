#!/usr/bin/node

const request = require('request');
const { promisify } = require('util');

// Convert request into a promise-based function using promisify
const requestPromise = promisify(request);

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Define the URL for the Star Wars API, using the movieId to get the film data
const url = `https://swapi.dev/api/films/${movieId}/`;

async function fetchCharacters () {
  try {
    // Fetch the movie data
    const response = await requestPromise(url);

    if (response.statusCode !== 200) {
      console.log('Failed to fetch data. Status code:', response.statusCode);
      return;
    }

    // Parse the JSON response body
    const filmData = JSON.parse(response.body);

    // Iterate over the characters and fetch their names
    for (const characterUrl of filmData.characters) {
      const characterResponse = await requestPromise(characterUrl);
      if (characterResponse.statusCode === 200) {
        const characterData = JSON.parse(characterResponse.body);
        console.log(characterData.name);
      }
    }
  } catch (error) {
    console.log('Error:', error);
  }
}

// Run the function to fetch and print the character names
fetchCharacters();
