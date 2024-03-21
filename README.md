# Rozborgen API

The rozborgen API is a very simple Flask-based web service designed as a tool to save time at school. It leverages the OpenAI API for generating structured documents about literature books. Given the name of a literature book, it returns a comprehensive, AI-generated summary and analysis, that is to be used to learn mainly czech literature to pass the czech maturita in a breeze.

I wrote this tool as a simple python project and have started on turning this into an API, so i can connect it with a [frontend interface](https://github.com/vincentsmid/rozborgen). This is not finished and will soon be rewritten in FastAPI.

## Features

- **Book Inquiry:** Submit the name of a literature book and receive a detailed, structured document about the book.
- **AI-Driven Analysis:** Utilizes OpenAI's powerful GPT4 model to generate insightful and comprehensive literature analyses.
- **Easy Integration:** Designed to be easily integrated into other applications or services requiring literary data.
