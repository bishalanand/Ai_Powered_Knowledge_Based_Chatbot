import { useState } from "react";
import { uploadPDF } from "../services/api";
import "./UploadDocuments.css";

function UploadDocument({ setDocumentId }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a PDF file");
      return;
    }

    try {
      setLoading(true);

      const response = await uploadPDF(file);

      const document_id = response.document_id;

      setDocumentId(document_id);

      alert("Document uploaded successfully!");
    } catch (error) {
      console.error("Upload failed:", error);
      alert("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-container">
      <h2 className="upload-title">Upload Document</h2>

      <input
        type="file"
        accept="application/pdf"
        onChange={handleFileChange}
        className="file-input"
      />

      <button
        onClick={handleUpload}
        disabled={loading}
        className="upload-button"
      >
        {loading ? "Uploading..." : "Upload PDF"}
      </button>
    </div>
  );
}

export default UploadDocument;