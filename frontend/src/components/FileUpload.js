import React, { useState } from "react";
import API from "../api";

function FileUpload({ refreshFiles }) {
  const [file, setFile] = useState(null);

  const upload = async () => {
    if (!file) {
      alert("Select a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      await API.post("/s3/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      alert("File Uploaded Successfully");
      setFile(null);
      refreshFiles();
    } catch (err) {
      console.error(err);
      alert("Upload Failed");
    }
  };

  return (
    <div className="card">
      <h3>Upload File</h3>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br />
      <br />

      <button onClick={upload}>
        Upload
      </button>
    </div>
  );
}

export default FileUpload;
