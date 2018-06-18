var express = require('express');
var router = express.Router();



router.get('/attack',function(req, res) {
    alert("hello!");

    res.render('massage', {user_name: req.body.user_name , pagePosts: postsDict});
});
var inputBox = document.getElementById('txtBox');
inputBox.onkeyup(function () {
    alert("hi!");
    document.getElementById('target').innerHTML = this;
});

function myFunction() {
    var x = document.getElementById('inputBox').value;
    document.getElementById('target').innerHTML = x;
}

