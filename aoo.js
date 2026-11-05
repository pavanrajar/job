const http = require('http');
const repl = require('repl');

function app() {
    repl.start('> ');
}
app();

const requestListener = function (req, res) {
    res.writeHead(200);
    res.end('Hello, World!');
}
const server = http.createServer(requestListener); server.listen(3000); 