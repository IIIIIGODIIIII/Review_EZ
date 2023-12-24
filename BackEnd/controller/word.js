const axios = require('axios');

exports.createWordCloud = async(req,res)=>{
    const {url} = req.query;
    console.log('url :>> ', url);
    try { 
        const response = await axios.get(`http://127.0.0.1:8000/work?url=${encodeURIComponent(url)}`, { responseType: 'arraybuffer'});
        const data = Buffer.from(response.data, 'binary').toString('base64');
        const imageSrc = `data:image/png;base64,${data}`;
    
    res.send(imageSrc); 
        console.log(url);
    } catch (error) {
        res.status(400).json(error);
    }
}