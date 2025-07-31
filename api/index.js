import express from 'express';
const app = express();

app.use(express.json());

// Simple root handler
app.get('/', (req, res) => {
  res.send(`
    <h1>SocialCraft API</h1>
    <p>Use POST /api/generate-content to access the API</p>
    <p>Status: Running 🟢</p>
  `);
});

export default app;