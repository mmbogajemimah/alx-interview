const request = require('request');

async function starWarsApi () {
  // request(`https://swapi-api.alx-tools.com/api/films/${num}/`, function (error, response, body) {
  //     console.error('error', error); // Print the error if one occurred
  //     console.log('statusCode', response && response.statusCode); // Print the response status code if a response was received
  //     console.log('body', body); // Print the HTML for the Google homepage.
  // });

  let characterAPI;
  const num = process.argv[2];
  const options = {
    url: `https://swapi-api.alx-tools.com/api/films/${num}/`,
    json: true
  };

  request(options, (error, response, body) => {
    // console.log('statusCode', response && response.statusCode);
    if (error) {
      console.error('Error: ', error);
    } else {
      // console.log('Character-APIs: ', body.characters);
      const charactersAPI = body.characters;
      // console.log(charactersAPI);
      for (characterAPI in charactersAPI) {
        // console.log(charactersAPI[characterAPI]);
        const character = {
          url: charactersAPI[characterAPI],
          json: true
        };
        request(character, (error, response, body) => {
          if (error) {
            console.error('Error:', error);
          } else {
            console.log('Character name:', body.name);
          }
        });
      }
    }
  });
}

starWarsApi();
