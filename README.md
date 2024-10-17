# RepoHub
RepoHub is an interactive tool designed to explore GitHub repositories using OpenAI's language model capabilities. This project enables users to clone repositories, index their content, and ask detailed questions to gain insights into the codebase and documentation.

# Table of Contents
* Prerequisites
* Installation
* Usage
* Features
* How It Works
* Contributing

# Prerequisites
* Before you begin, ensure you have the following:

* Python 3.6+
* Git
* OpenAI API Key (set in an environment variable as OPENAI_API_KEY)

# Installation

# 1. Clone the Repository:
git clone https://github.com/yourusername/repoquest.git
* cd repoquest
# 2. Set Up a Virtual Environment: It's recommended to create a virtual environment to manage dependencies.
python -m venv env

# 3. Activate the Virtual Environment:
.\env\Scripts\activate

# 4. Install Required Packages: Install the necessary dependencies listed in requirements.txt.
 pip install -r requirements.txt
 
# 5. Usage
To run the program, execute the following command:
* python app.py

# 6. Interactive Workflow
* 1. Enter the GitHub Repository URL: When prompted, provide the URL of the GitHub repository you want to explore.
* 2. Ask Questions: After the repository is cloned and indexed, you can ask questions related to the codebase. Type your questions in the prompt.
* 3. Exit the Application: Type exit() to terminate the program.
  4. 
# Features
* Clone GitHub Repositories: Automatically clones any public GitHub repository to your local machine.
* Document Indexing: Supports various file formats (e.g., Python, Markdown, Jupyter Notebooks) for indexing and retrieval.
* Natural Language Processing: OpenAI's GPT model is used to respond to user queries about the repository.
* Interactive Q&A: Engages users in a conversation to facilitate understanding of the codebase and documentation.
* File Type Analysis: Provides statistics on the types of files present in the repository.
* 
# How It Works
* Cloning the Repository: The program uses a subprocess to clone the repository using Git.
* Loading Documents: Files are loaded using langchain.document_loaders, handling various formats for comprehensive analysis.
* Indexing: The loaded documents are indexed using BM25 and TF-IDF methods to allow efficient retrieval based on user queries.
* Natural Language Querying: User questions are processed and sent to the OpenAI API, which generates responses based on the context of the repository.
* Returning Answers: The answers, along with relevant document snippets, are presented back to the user for clarity and context.
