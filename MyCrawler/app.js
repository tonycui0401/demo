const express = require('express')
const app = express()
const port = 3000

const execSync = require('child_process').execSync;
// import { execSync } from 'child_process';  // replace ^ if using ES modules


app.get('/', (req, res) => {

	res.send('Hello World!')

	const output = execSync('python3 extracter.py', { encoding: 'utf-8' });  // the default is 'buffer'
console.log('Output was:\n', output);

})



app.listen(port, () => console.log(`Example app listening on port ${port}!`))