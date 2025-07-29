export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { platform, goal, tone } = req.body;

  if (!platform || !goal || !tone) {
    return res.status(400).json({ error: 'Missing parameters' });
  }

  // Mock response (replace with actual GPT logic later)
  const bio = `Here's a fun bio for your ${platform} page: "Turning ${goal} into smiles 😄!"`;

  res.status(200).json({ bio });
}
