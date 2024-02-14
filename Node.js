const mysql = require('mysql');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'webhook',
  password: 'Jasper@1998',
  database: 'apollo_contacts'
});

connection.connect((err) => {
  if (err) {
    console.error('Error connecting to MySQL:', err.stack);
    return;
  }
  console.log('Connected to MySQL as ID', connection.threadId);
});
