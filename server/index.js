'use strict'
const express = require('express')
const cors = require('cors');
const api = require('./api');
const db = require('./db');

// Create the express app
const app = express()
const PORT = 5000;

// Routes and middleware
// app.use(/* ... */)
// app.get(/* ... */)

// Error handlers
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cors());

const logger = (req, res, next) => {
    console.log('hit');
    next();
};

app.use(logger);

app.use('/api', api);

app.use(function fourOhFourHandler (req, res) {
  res.status(404).send()
})
app.use(function fiveHundredHandler (err, req, res, next) {
  console.error(err)
  res.status(500).send()
})



// Start server
app.listen(PORT, () => console.log('Server Started on PORT', PORT));
