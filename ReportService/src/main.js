const express = require('express')
const request=require('request');
const axios = require('axios')
const app = express()
app.get('/cv/:username/',async function (req, res) {
  try {
    const username = req.params.username
    const response =await axios.get(`http://api:8000/profile/${username}/`)
    const data={
          "template":{
              "name":"cv-template"
          },
          "data":response.data
      }
      options={
        uri:'http://jsreport:3000/api/report',
        method:'post',
        json:data
      }
      request(options).pipe(res)    
  } catch (error) {
    res.status = error.response.status
    res.send(error.response.data)
  }
  })

app.listen(3000)