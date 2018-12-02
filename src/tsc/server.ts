import * as Express from 'express';
const app = Express();

const port = 3001;

import * as bodyParser from 'body-parser';


// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));

// parse application/json
app.use(bodyParser.json());


app.get('/', (req, res) => {
    res.json({msg: "Hello World!"});
});

// app.use('/article', article);
// app.use('/auth', auth);
// app.use('/user', user);

app.listen(port, () => {
    console.log('Listen started at port ' + port);
});

export default app;
