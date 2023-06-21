import kue from 'kue';

// check if the jobs parameter is an array
function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

// iterate over each job data object
  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData).save((err) => {
      if (err) {
        console.error('Failed to create job:', err);
      } else {
        console.log(`Notification job created: ${job.id}`);
      }
    });

    // listen for job completion, failure and progress events
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });
    job.on('failed', (err) => {
      console.error(`Notification job ${job.id} failed: ${err}`);
    });
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
