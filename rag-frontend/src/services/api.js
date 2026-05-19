import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000"
});

export const uploadPDF = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await API.post("/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data"
    }
  });

  return response.data;
};

export const getSummary = async (document_id) => {
  const response = await API.post("/summary", {
    document_id: document_id
  });

  return response.data;
};

export const askQuestion = async (document_id, question) => {
  const response = await API.post("/chat", {
    document_id: document_id,
    question: question
  });

  return response.data;
};