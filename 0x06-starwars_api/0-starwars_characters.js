#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const filmAPI = 'https://swapi-api.hbtn.io/api/films/' + filmId;
let people = [];
const names = [];

const charactersAPI = async () => {
  await new Promise(resolve => request(filmAPI, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error('Error: ', error, '| StatusCode: ', response.statusCode);
    } else {
      const jsonBody = JSON.parse(body);
      people = jsonBody.characters;
      resolve();
    }
  }));
};

const characterNames = async () => {
  if (people.length > 0) {
    for (const person of people) {
      await new Promise(resolve => request(person, (error, response, body) => {
        if (error || response.statusCode !== 200) {
          console.error('Error: ', error, '| StatusCode: ', response.statusCode);
        } else {
          const jsonBody = JSON.parse(body);
          names.push(jsonBody.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: Got no characters for some reason');
  }
};

const getCharacterNames = async () => {
  await charactersAPI();
  await characterNames();

  for (const name of names) {
    if (name === names[names.length - 1]) {
      process.stdout.write(name);
    } else {
      process.stdout.write(name + '\n');
    }
  }
};

getCharacterNames();
