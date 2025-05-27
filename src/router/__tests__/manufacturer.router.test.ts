import request from 'supertest';
import express from 'express';
import ManufacturerRouter from '../manufacturer.router';

const app = express();
app.use('/', ManufacturerRouter);

describe('ManufacturerRouter', () => {
  it('GET / should return "Hello World"', async () => {
    const response = await request(app).get('/');
    expect(response.status).toBe(200);
    expect(response.text).toBe('Hello World');
  });
});
