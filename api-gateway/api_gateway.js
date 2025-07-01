const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

app.use('/user', createProxyMiddleware({ target: 'http://localhost:5001', changeOrigin: true }));
app.use('/product', createProxyMiddleware({ target: 'http://localhost:5002', changeOrigin: true }));

app.listen(5000, () => {
  console.log('API Gateway running on http://localhost:5000');
});
