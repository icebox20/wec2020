const express = require('express');
const chess = require('./chess');


const router = express.Router();

router.use('/chess', chess);

router.use(function (req,res) {
    res.status(404).json({ Error: 'No API Endpoint Here' });
})

module.exports = router;
