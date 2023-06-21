import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const client = redis.createClient();
const queue = kue.createQueue();

// promisifying the Redis set method; set number of available seats
const reserveSeat = async (number) => {
  const setAsync = promisify(client.set).bind(client);
  await setAsync('available_seats', number.toString());
};

// promisifying get method; get number of seats available, parse available seats
const getCurrentAvailableSeats = async () => {
  const getAsync = promisify(client.get).bind(client);
  const availableSeats = await getAsync('available_seats');
  return parseInt(availableSeats);
};

app.use(express.json());

// get current number of available seats; send available seats as JSON
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

// send response indicating that reservations are blocked
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  // logging an error or success message
  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      console.error('Seat reservation job failed:', err.message);
      res.json({ status: 'Reservation failed' });
    } else {
      console.log('Seat reservation job', job.id, 'completed');
      res.json({ status: 'Reservation in process' });
    }
  });
});

// sending response indicating that the queue is processing
app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });
  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    // disable further reservations if there are no seats available
    if (availableSeats === 0) {
      reservationEnabled = false;
      done(new Error('Not enough seats available'));
    } else if (availableSeats >= 1) {
    // researve a seat by decrementing the available seats count
      await reserveSeat(availableSeats - 1);
      // disable further reservations if there is only one seat left
      if (availableSeats === 1) {
        reservationEnabled = false;
      }
      done();
    }
  });
});

const initialNumberOfSeats = 50;
let reservationEnabled = true;

// starting the server and listening on port 
reserveSeat(initialNumberOfSeats).then(() => {
  app.listen(1245, () => {
    console.log('Server is listening on port 1245');
  });
});
