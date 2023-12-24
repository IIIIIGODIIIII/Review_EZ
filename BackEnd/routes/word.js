const express = require('express');
const { createWordCloud } = require('../controller/word');

const router = express.Router();

router.get('/',createWordCloud);

exports.router = router;