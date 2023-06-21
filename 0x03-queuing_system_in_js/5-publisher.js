import redis from 'redis';
const client = redis.createClient();

client.on("error", (err) => {
  if (err) console.log(`Redis client not connected to the server: ${err}`)
}).on('ready', () => {
    console.log('Redis client connected to the server');
});

// function to publish a message after a specified time
const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }, time);
}

// call the publishMessage function with different messages and times
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
