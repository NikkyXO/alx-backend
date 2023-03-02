/* eslint-disable no-undef */

const kue = require('kue');

const queue = kue.createQueue();

const jobData = {
	phoneNumber: '5551234567',
	message: 'Hello from Kue job!'
};

//create a new job with the data specified in jobData, and save it to the push_notification_code queue.
const job = queue
	.create('push_notification_code', jobData)
	.on('complete', () => console.log('Notification job completed'))
	.on('failed', () => console.log('Notification job failed'))
	.save((err) => {
		if (!err) {
			console.log(`Notification job created: ${job.id}`);
		} else {
			console.error('Error creating job:', err);
		}
	});
