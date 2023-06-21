import kue from 'kue';
const queue = kue.createQueue();

// array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// function to send notification
const sendNotification = (phoneNumber, message, job, done) => {
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  job.process(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

// queue process for listening to new jobs
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
