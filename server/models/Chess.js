const mongoose = require('mongoose');

const chessScheme = new mongoose.Schema({
    id: {type: String, required: true},
    board: {type: Object, required: true},
    player: {type: Boolean},
});

const Chess = mongoose.model('session', chessScheme);

module.exports = {chessScheme, Chess}