import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import umap
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

st.set_page_config(page_title="ClusterMyWords", layout="wide")

st.title("🌈 ClusterMyWords")
st.subheader("Explore how your words relate in meaning")

st.write("""
Paste a list of words below.  
ClusterMyWords will map them into a 2D meaning‑space using AI embeddings.
""")

# Input box
words_input = st.text_area("Enter words (one per line):", height=200)

if st.button("Visualize Meaning"):
    words = [w.strip() for w in words_input.split("\n") if w.strip()]

    if len(words) < 2:
        st.error("Please enter at least two words.")
    else:
        with st.spinner("Analyzing meaning…"):
            model = SentenceTransformer("all-MiniLM-L6-v2")
            embeddings = model.encode(words)

            reducer = umap.UMAP(n_components=2, random_state=42)
            points = reducer.fit_transform(embeddings)

            # Clustering
            k = min(5, len(words))
            kmeans = KMeans(n_clusters=k, n_init="auto")
            labels = kmeans.fit_predict(points)

            # Plot
            fig, ax = plt.subplots(figsize=(10, 7))
            colors = plt.cm.tab10(labels)

            ax.scatter(points[:, 0], points[:, 1], c=colors, s=120)

            for i, word in enumerate(words):
                ax.text(points[i, 0], points[i, 1], word, fontsize=12)

            ax.set_title("Semantic Map of Your Words", fontsize=16)
            ax.set_xlabel("Meaning Dimension 1")
            ax.set_ylabel("Meaning Dimension 2")

            st.pyplot(fig)

        # Insights panel
        st.header("📘 What This Means")
        st.write("""
        This map shows how your words relate in meaning.  
        Words that appear close together are semantically similar.  
        Words far apart are unrelated or opposite in meaning.
        """)

        # Nearest neighbors
        st.subheader("🔍 Nearest Neighbors")
        distances = np.linalg.norm(points[:, None] - points[None, :], axis=2)

        for i, word in enumerate(words):
            nearest = np.argsort(distances[i])[1]
            st.write(f"**{word}** is closest to **{words[nearest]}**")

        # Outliers
        st.subheader("🚀 Outliers")
        avg_dist = distances.mean(axis=1)
        outlier_idx = np.argmax(avg_dist)
        st.write(f"The biggest outlier is **{words[outlier_idx]}** — it’s the most unique word in your list.")