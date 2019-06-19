var nodemailer = require('nodemailer');
var JSSoup = require('jssoup').default;
var request = require('request');
var parseString = require('xml2js').parseString;
var _ = require('lodash');
request('https://retrieve.pskreporter.info/query?receiverCallsign=kc9gpj', function (error, response, body) {
//   console.log('error:', error); // Print the error if one occurred
//   console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
// console.log('body:', body); // Print the HTML for the Google homepage.


var xml = body
parseString(xml, function (err, result) {
  var json = JSON.stringify(result)
  let time = _.get(json, 'flowStartSeconds');

    console.log(time);
});

var soup = new JSSoup(body);
// console.log(soup)
// console.log(soup.findAll('receptionReport'));
});

var transporter = nodemailer.createTransport({
  host: 'smtp.mail.yahoo.com',
  port: 465,
  service:'yahoo',
  secure: false,
  auth: {
    user: 'projectemail1212@yahoo.com',
    pass: '1111asdf'
  },
  debug: false,
  logger: true 
});

var mailOptions = {
  from: 'projectemail1212@yahoo.com',
  to: 'kc9gpj12@gmail.com',
  subject: 'PSK Reporter',
  text: 'New Message',
  html: 'test'

};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }

});


