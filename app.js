const app = require("express")(); 
const cool = require('cool-ascii-faces');

const PORT = process.env.PORT || 3000; 

app.get("", (req, res) => {
	res.send("Hello world Boys"); 
}).get('/cool', (req, res) => res.send(cool()));

app.listen(PORT, () => {
	console.log(`App up at port ${PORT}`); 
}); 
