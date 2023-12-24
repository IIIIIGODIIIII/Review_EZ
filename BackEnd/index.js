const express = require('express');
const cors = require('cors');
const wordRouter = require("./routes/word");


const app = express();
const port = 8080;


app.use(express.json());
app.use(cors())
app.use("/word",wordRouter.router);
app.get('/',(req,res)=>{
    res.send("hi")
})

app.listen(port,()=>{
    console.log(`app listening on http://localhost:${port}`);
})