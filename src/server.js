const express = require('express')
const app = express();

app.get('/', (req,res)=>{
  res.send("Wlecome to node js app");
});

app.listen(3000, function () {
  console.log("Node js web app running on port 3000");
});
