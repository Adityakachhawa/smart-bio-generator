// index.js
module.exports = (req, res) => {
  res.status(404).send('Not found - use POST /generate-content');
};