
import { createClient } from 'redis';
/* eslint-disable react/react-in-jsx-scope */
function redisConnect() {
  const client = createClient();

  client
    .on('connect', function () {
      console.log('Redis client connected to the server');
    })
    .on('error', (err) => {
      console.log(`Redis client not connected to the server: ${err}`);
    });
}

redisConnect();
