🌈 ClusterMyWords
An interactive app for exploring how words relate in meaning
ClusterMyWords is a colorful, educational web app that lets you paste in a list of words and instantly see how they cluster together in semantic space. It uses modern AI embeddings to map your words into a 2D visualization, showing which words are similar, which are different, and which ones stand out as outliers.
This app is built with Streamlit, UMAP, and Sentence Transformers, and is designed to be simple, intuitive, and fun to explore.

✨ Features
- Paste any list of words — no limits
- Interactive 2D semantic map generated using AI embeddings
- Bold, colorful visualization for easy interpretation
- Automatic clustering to reveal natural groups
- Nearest‑neighbor insights for each word
- Outlier detection to highlight the most unique word
- Educational explanations to help you understand what the map means

🚀 How to Use
- Open the app (once deployed on Streamlit Cloud).
- Paste a list of words — one per line.
- Click Visualize Meaning.
- Explore the map and read the insights panel.
The app will show you:
- Which words are closest in meaning
- How many clusters your list naturally forms
- Which word is the biggest outlier
- How the AI interprets the relationships between your words

🧠 How It Works
ClusterMyWords uses:
- SentenceTransformer model: all-MiniLM-L6-v2
- Converts each word into a high‑dimensional embedding
- UMAP:
- Reduces embeddings to 2D for visualization
- K‑Means clustering:
- Groups words into meaningful clusters
- Matplotlib:
- Draws the colorful semantic map
Words that appear close together are semantically similar.
Words far apart are unrelated or opposite in meaning.

📦 Installation (for local use)
If you want to run the app locally:
pip install -r requirements.txt
streamlit run app.py



🌐 Deployment (Streamlit Cloud)
- Upload app.py and requirements.txt to a GitHub repository.
- Go to https://streamlit.io/cloud
- Click New app
- Select your repository and choose app.py
- Deploy
Streamlit will build and host the app automatically.

🎨 Theme
ClusterMyWords uses a bold & colorful visual style to make clusters pop and make the map feel lively and intuitive.

💡 Example Use Cases
- Vocabulary exploration
- Creative writing inspiration
- Language teaching
- Brainstorming sessions
- Semantic analysis
- Word association games

