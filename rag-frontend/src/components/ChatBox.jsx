import { useState } from "react";
import { askQuestion } from "../services/api";
import "./ChatBox.css";

function ChatBox({ documentId }) {

  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);

  // Auto expanding textarea
  const handleChange = (e) => {
    const textarea = e.target;
    textarea.style.height = "auto";
    textarea.style.height = textarea.scrollHeight + "px";
    setQuestion(textarea.value);
  };

  // Send question to backend
  const handleAsk = async () => {

    if (!question.trim()) return;

    const userMessage = {
      role: "user",
      text: question
    };

    setMessages((prev) => [...prev, userMessage]);

    try {

      const res = await askQuestion(documentId, question);

      const botMessage = {
        role: "bot",
        text: res.answer
      };

      setMessages((prev) => [...prev, botMessage]);

    } catch (error) {
      console.error("Chat error:", error);
    }

    setQuestion("");
  };

  // Enter to send | Shift+Enter new line
  const handleKeyDown = (e) => {

    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleAsk();
    }

  };

  return (
    <div className="chat-container">

      <h2>Chat with your PDF</h2>

      <div className="chat-messages">

        {messages.map((msg, index) => (

          <div
            key={index}
            className={msg.role === "user" ? "user-msg" : "bot-msg"}
          >
            {msg.text}
          </div>

        ))}

      </div>

      <div className="chat-input">

        <textarea
          value={question}
          onChange={handleChange}
          onKeyDown={handleKeyDown}
          placeholder="Ask your question..."
        />

        <button onClick={handleAsk}>
          Send
        </button>

      </div>

    </div>
  );
}

export default ChatBox;