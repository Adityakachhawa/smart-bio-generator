import axios from 'axios';
import dotenv from 'dotenv';

// Load environment variables
dotenv.config();

console.log("Environment Variables:", {
  OPENROUTER_API_KEY: process.env.OPENROUTER_API_KEY ? "Exists" : "Missing",
  APP_URL: process.env.APP_URL,
  APP_TITLE: process.env.APP_TITLE,
  NODE_ENV: process.env.NODE_ENV
});

export default async function handler(req, res) {
  console.log("Request received:", req.method, req.url);
  
  try {
    if (req.method !== 'POST') {
      console.warn("Method not allowed:", req.method);
      return res.status(405).json({ message: 'Method not allowed' });
    }

    const { prompt } = req.body;
    console.log("Prompt received:", prompt);

    if (!prompt) {
      console.warn("Missing prompt");
      return res.status(400).json({ error: 'Prompt is required' });
    }

    const apiUrl = 'https://openrouter.ai/api/v1/chat/completions';
    console.log("Calling OpenRouter API:", apiUrl);
    
    const response = await axios.post(
      apiUrl,
      {
        model: "openai/gpt-3.5-turbo",
        messages: [{ role: "user", content: prompt }],
        max_tokens: 500
      },
      {
        headers: {
          'Authorization': `Bearer ${process.env.OPENROUTER_API_KEY}`,
          'Content-Type': 'application/json',
          'HTTP-Referer': process.env.APP_URL || 'https://smart-ai-bio-caption-generator.streamlit.app',
          'X-Title': process.env.APP_TITLE || 'Smart Bio Generator'
        },
        timeout: 30000
      }
    );

    console.log("OpenRouter response status:", response.status);
    const content = response.data.choices[0].message.content;
    console.log("Generated content length:", content.length);
    
    res.status(200).json({ content });
  } catch (error) {
    console.error('API Error:', error);
    console.error('Error details:', {
      message: error.message,
      code: error.code,
      response: error.response?.data
    });

    res.status(500).json({
      error: 'Content generation failed',
      details: error.message,
      stack: process.env.NODE_ENV === 'development' ? error.stack : undefined
    });
  }
}