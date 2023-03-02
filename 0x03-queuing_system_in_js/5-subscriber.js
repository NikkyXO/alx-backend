import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
	console.log('Redis client connected to the server');
});

client.on('error', (error) => {
	console.log(`Redis client not connected to the server: ${error.message}`);
});

//subscribe to holberton school channel
client.subscribe('holberton school channel');

//listen for messages on channel and print message when received
client.on('message', (channel, message) => {
	console.log(`Message received from channel ${channel}: ${message}`);
	if (message === 'KILL_SERVER') {

		client.unsubscribe('holberton school channel');
		//quits the client using the "quit" method
		client.quit();
		// client.end(true)
	}
});
