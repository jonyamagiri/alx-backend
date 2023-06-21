import redis from 'redis';
const client = redis.createClient();

client.on("error", (err) => {
  if (err) console.log(`Redis client not connected to the server: ${err}`)
}).on('ready', () => {
    console.log('Redis client connected to the server');
});

// subscribing to the 'holberton school channel'
client.subscribe("holberton school channel");

// listening for incoming messages
client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    client.quit();
  }
});
