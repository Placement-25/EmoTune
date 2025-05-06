import React, { useState } from "react";
import axios from "axios";

function App() {
  const [emotion, setEmotion] = useState(null);

  const handleImageUpload = async (e) => {
    const formData = new FormData();
    formData.append("image", e.target.files[0]);

    try {
      const res = await axios.post("http://localhost:5000/analyze", formData);
      setEmotion(res.data.emotion);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>EmoTune</h1>
      <input type="file" accept="image/*" onChange={handleImageUpload} />
      {emotion && <h2>Detected Emotion: {emotion}</h2>}
    </div>
  );
}

export default App;
