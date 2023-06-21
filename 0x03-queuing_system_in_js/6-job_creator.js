import kue from 'kue';
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a notification message',
};

// create a job named 'push_notification_code' with job data
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// listen for job completion event
job.on('complete', () => {
  console.log('Notification job completed');
});

// listen for job failure event
job.on('failed', () => {
  console.log('Notification job failed');
});
