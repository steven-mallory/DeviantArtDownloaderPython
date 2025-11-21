let http = require('http'); //import

let pathToGetAuthCode = 'https://www.deviantart.com/oauth2/authorize
let pathToSendAuthCode = 'https://www.deviantart.com/oauth2/authorize

http.createServer(function (req, res) { //functino si a requestlistener
	res.writeHead(200, {'Content-Type': 'text/plan'});
	res.end('Hello World');
}).listen(8080);





//eventually, output our access token and refresh token
const fs = require('fs')
//async file reading
//
//
fs.readFile('TEXT.txt', 'utf8', (err, data) => {
	if (err) {
		console.error('Error reading file: ' + err);
	}
		
});
const filepath = 'tokens_txt'


ignore this

const loadFile = async () => {
	try {
		const data = await fs.promises.readFile('./test.txt', { encoding = 'utf-8' });
		console.log(data);
	} catch (error) {
		console.error(error);
	}
};

