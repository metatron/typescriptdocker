import * as Express from 'express';
import * as Web3 from 'web3';

const app = Express();

const port = 3001;

import * as bodyParser from 'body-parser';


// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));

// parse application/json
app.use(bodyParser.json());


app.get('/', (req, res) => {
    res.json({msg: "Hello World!!"});
});

// app.use('/article', article);
// app.use('/auth', auth);
// app.use('/user', user);

app.listen(port, () => {
    console.log('Listen started at port ' + port);

    var web3 = new Web3(Web3.givenProvider);

    if (web3) {
  	  console.log("=======Log1");
      console.warn("Using web3 detected from external source. If you find that your accounts don't appear or you have 0 MetaCoin, ensure you've configured that source properly. If using MetaMask, see the following link. Feel free to delete this warning. :) http://truffleframework.com/tutorials/truffle-and-metamask")
    }
});

export default app;
