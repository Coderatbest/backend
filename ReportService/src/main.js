const express = require('express')
const request=require('request');
const app = express()
app.get('/:username/', function (req, res) {
  const username = req.params.username
  const data={
        "template":{
            "name":"cv-template"
        },
        "data":{
            "username":"alex"
        }
    }
options={
  uri:'http://jsreport:3000/api/report',
  method:'post',
  json:data
  //how to pass parameter here like uri,method. 
  }
  request(options).pipe(res)
  // res.send(`hello ${username}`)
})

app.listen(3000)