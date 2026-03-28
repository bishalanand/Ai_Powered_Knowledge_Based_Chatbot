import { useState } from 'react'
import UploadDocuments from './components/UploadDocuments'
import SummarySection from './components/SummarySection';
import ChatBox from './components/ChatBox';
import './App.css'

function App() {
  const [documentId, setDocumentId] = useState(null);

  return (
    <>
      <h1>AI PDF Chatbot</h1>

      <UploadDocuments setDocumentId={setDocumentId} />

      {documentId && (
        <>
          <SummarySection documentId={documentId} />
          <ChatBox documentId={documentId} />
        </>
      )}
    </>
  )
}

export default App
