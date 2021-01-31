const express = require('express');
const { Chess } = require('../models/Chess')

const router = express.Router();

router.post('/',function (req,res){
    // console.log(req)
    console.log( req.body)
    try {
        Chess.findOne({id: '1'}, {}, {}, (err, chess) => {
            if (!chess) {
                Chess.create({
                    id: '1',
                    board: req.body
                });
                console.log("added");
            } else {
                Chess.findOneAndUpdate({id: "1"}, {
                    id: '1',
                    board: req.body.board,
                    player: req.body.player,
                }, {new: true},function (error, doc){
                    console.log("doc");
                })
                console.log("updated");
            }

        })
    }
    catch (error){
        console.log(error);
    }


    return res.json({ message: "OK" });

});

router.get('/',async function (req,res){
    await Chess.findOne({id: '1'}, {}, {}, (err, chess) => {
        if(!chess){
            return res.status(400).json({ message: "BAD" });
        }
        else
        {
            return res.json({"board":chess.board, "player":chess.player})
        }

    })
})

module.exports = router;