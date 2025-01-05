# GlinerParser

⚠️ **IMPORTANT: Test Project Only - Not for Production Use** ⚠️

This project is a testing implementation of the Gliner model and is intended **solely for experimental and learning purposes**. It should not be used in production environments due to various limitations.

## Overview

GlinerParser is a test project that explores the capabilities of the Gliner model for parsing and processing tasks. This implementation serves as a proof of concept and demonstration tool.

## Limitations

- This is a test implementation with limited error handling
- Performance optimizations are not implemented
- Not thoroughly tested for edge cases
- May have memory management issues with large datasets
- Security features are not production-ready

## Project Structure

```
GlinerParser/
├── src/
│   ├── main.py
│   ├── utils.py
│   └── config.py
├── .env.sample
├── .env
├── Dockerfile
└── README.md
```

## Getting Started

This project is for testing and educational purposes only. There are two ways to run this project:

### Using Docker (Recommended)

1. Clone the repository
2. Build and run the Docker container:
   ```bash
   docker build -t gliner-parser .
   docker run -p 8000:8000 gliner-parser
   ```

### Manual Setup

1. Clone the repository
2. Create a new `.env` file and copy the configuration data from `.env.sample`
3. Fill in the required environment variables in `.env` file with your actual values
4. Review the source code in the `src` directory
5. Understand that this is a test implementation

## Environment Variables

Make sure to set up your environment variables before running the project:
1. Look at the configuration template in `.env.sample`
2. Create a new `.env` file and fill it with your actual values

Example `.env` structure:
```
# Provide paths to resume files
RESUMES_FILES_PATH=./resumes/

# Provide path where to store parsed resumes
PARSED_RESUMES_FILE_PATH=./parsed_resumes/candidates.json
```

## Disclaimer

This code is provided "as is" without warranty of any kind. It is not meant for production use and should only be used for testing, learning, and experimental purposes.

## Last Updated

January 5, 2025