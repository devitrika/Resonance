# 🎥 **Resonance : Video Recommendation System that matches your Frequency** 📚✨  

> A hybrid recommendation engine to suggest videos and content users will love! 💡 Combines **content-based filtering** and **collaborative filtering** for smarter, more personalized recommendations.

---
## 🌍 **Live Demo**

🔗 Check out the live application [here](https://resonancevideorec.streamlit.app/).
## 🌟 **Features**  

🔍 **Content-Based Recommendations**  
- Uses video metadata like **title**, **genre**, and other features to recommend similar content.  

🤝 **Collaborative Filtering**  
- Suggests content based on user interactions and the preferences of similar users.  

🎭 **Hybrid Approach**  
- Combines content-based and collaborative filtering for improved accuracy.  

📊 **Dynamic Visualization**  
- Recommendations displayed in an engaging UI with thumbnails and details.  

---

## 🛠️ **Tech Stack**  

💻 **Programming Language**: Python  
📚 **Libraries**:  
- `pandas` for data manipulation  
- `scikit-learn` for ML operations  
- `streamlit` for interactive web interface  
- `numpy` for numerical operations  

---

## 🚀 **How It Works**  

### **1. Preprocessing** 🧹  
- Cleans and combines data from different files.  
- Normalizes numeric features (e.g., upvotes, ratings).  

### **2. Content-Based Filtering** 📜  
- Uses **TF-IDF Vectorization** to analyze text features like genres and titles.  
- Finds similar content using **Cosine Similarity**.  

### **3. Collaborative Filtering** 🤝  
- Creates a **user-item interaction matrix**.  
- Computes similarities between users to recommend popular items among peers.  

### **4. Hybrid Recommendation** ⚡  
- Merges recommendations from both content and collaborative approaches.  

### **5. Interactive UI** 🖼️  
- Displays recommendations with thumbnails and genre info.  

---

## 🧪 **Setup and Run**  

1. **Clone the Repository** 🛠️  
   ```bash
   git clone https://github.com/your-repo-name/recommendation-system.git
   cd recommendation-system

2. **Install Dependencies**
   ```bash
   pip installl -r requirements.txt
   
3. **Prepare Data**
   - Ensure all CSV files (all_posts.csv, liked_posts.csv, etc.) are in the project directory.
  
4. **Run the Streamlit App 🚀

  ```bash
  streamlit run recommendation.py
  ```
5. Open your browser at http://localhost:8501 to see the magic! 🌈



## 🧩 **Future Enhancements**

✨ Add a **Deep Learning** model for better recommendations.  
✨ Support for **multiple languages**.  
✨ Include **user authentication**.  

---

## 🤝 **Contributions**

🙌 Contributions are always welcome! Fork the repo, make your changes, and submit a pull request.  

---

## 📄 **License**

📝 This project is licensed under the **MIT License**.  

---

## ❤️ **Support**

💬 If you love this project, don’t forget to give it a star ⭐!  
