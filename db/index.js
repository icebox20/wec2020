const mongoose = require('mongoose');
const dotenv = require('dotenv');

dotenv.config();

void mongoose.connect(process.env.CONNECTION_STRING || '', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    useCreateIndex: true,
    useFindAndModify: false
});

module.exports = mongoose.connection;
