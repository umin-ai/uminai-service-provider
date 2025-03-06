Note: This is a Typescript-based Express.js project.

## Requirement:
```bash
1. Node version 20+ and above
2. MongoDB Instance
```

## Getting Started

Installation:
```bash
npm install
```

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.

## Environment Update:
#### Usage: Rename the file .env.example to .env and update the values accordingly
```bash
# OPENAI or ANY OTHER LLM SUPPORTED OPENAI COMPLETIONS API
OPENAI_API_URL=''
OPENAI_API_KEY='';

# CHAINSAFE
CHAINSAFE_KEY='CHAINSAFE_KEY'
CHAINSAFE_API_KEY ='CHAINSAFE_API_KEY'
CHAINSAFE_BUCKET_ID='CHAINSAFE_BUCKET_ID'

# MONGODB
MONGO_URI = 'mongodb+srv://{{UPDATE_HOST}}/uminai'
```

Link to XRPL EVM Faucet: [Faucet](https://chains.tools/faucet/xrplevm)
```
