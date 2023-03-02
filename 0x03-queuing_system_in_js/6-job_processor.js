/* eslint-disable no-undef */

var kue = require('kue'),
	queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
	console.log(
		`Sending notification to ${phoneNumber}, with message: ${message}`
	);
}

//create a job processor that listens for new jobs on the 'push_notification_code' queu
queue.process('push_notification_code', function (job, done) {
	sendNotification(job.data.phoneNumber, job.data.message);
	done();
});
