var express = require('express');
var router = express.Router();
var passport = require('passport');
var Tokens = require('csrf');
/* GET home page. */
var user={
    id: 1,
    user: 'Alice',
    password: 1321
};

var token=Tokens();
var secret = token.secretSync();
var csrfToken = token.create(secret);
var user_token={};
user_token[user.user]=csrfToken;

router.get('/', function(req, res, next) {
  res.render('login', { title: 'Registration' });

});

router.post('/login', function (req, res, next) {
    if((req.body.userName==user.user)&&(req.body.password2==user.password)){
        req.login(user, function (err) {
            if(req.body.btn=='SafeTransfer'){
                res.render('Secure',{csrfToken: csrfToken});
            }else{
                res.render('bank');
            }

        });
    } else {res.render('login')}
});



router.get('/register',function (req,res,next) {
    res.render('index')
})


router.get('/logout', function(req, res){
        req.logout();
        res.redirect('/');
    });

// bank
router.get('/bank',authenticationMiddleware(), function (req, res, next) {
    res.render('bank',{title: req.username});
});

// transfer
router.post('/transfer', authenticationMiddleware(),function (req,res,next) {
    console.log('Transfer of '+req.body.amount+"₪ to "+req.body.dest);
    res.render('bank')
});
// transfer
router.post('/tokenTransfer',authenticationMiddleware(), function (req,res,next) {
    if(user_token[req.user.user]==req.body._csrf){
        console.log('Secure Transfer of '+req.body.amount+"₪ to "+req.body.dest);
        res.render('Secure',{csrfToken: req.user.token})
    }
    else {
        console.log('Someone try to steal your money');
        res.redirect('/')
    }
});

function authenticationMiddleware() {
    return function (req, res, next) {
        console.log(req.user);
        console.log(req.isAuthenticated());
        if (req.isAuthenticated()) {
            return next()
        }
        res.redirect('/')
    }

}


passport.serializeUser(function (user, done) {
    done(null, user.id);
});

passport.deserializeUser(function (id, done) {
    var usr;
    if (typeof user !== 'undefined' && user) {

        if (id == user.id)
            usr = user;
    }
    done(null, usr);

});

module.exports = router;
